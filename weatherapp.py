from flask import Flask, request, jsonify, render_template
import requests
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

app = Flask(__name__)

API_KEY = "59cdc47ee76b1c77ef0db6959a061fac"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Fetch weather data
def fetch_weather_data(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    forecast = data["list"][0]
    return {
        "temperature_c": forecast["main"]["temp"],
        "temperature_f": (forecast["main"]["temp"] * 9 / 5) + 32,
        "humidity": forecast["main"]["humidity"],
        "wind_speed": forecast["wind"]["speed"],
        "weather_condition": forecast["weather"][0]["description"]
    }

# Train model
def train_model():
    # Simulated dataset
    data = {
        "wind_speed": np.random.uniform(0, 10, 100),
        "humidity": np.random.uniform(20, 100, 100),
        "temperature_c": np.random.uniform(-10, 40, 100)
    }
    df = pd.DataFrame(data)
    df["temperature_f"] = (df["temperature_c"] * 9 / 5) + 32

    X = df[["wind_speed", "humidity"]]
    Y = df[["temperature_c", "temperature_f"]]
    
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, Y_train)
    return model, scaler

model, scaler = train_model()

# Flask routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get("city")
    weather = fetch_weather_data(city)
    if not weather:
        return jsonify({"error": "City not found or API issue"}), 404
    return jsonify(weather)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    wind_speed = float(data.get("wind_speed", 0))
    humidity = float(data.get("humidity", 0))
    
    input_data = np.array([[wind_speed, humidity]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    temp_c, temp_f = prediction[0]
    
    return jsonify({"temp_c": temp_c, "temp_f": temp_f})

if __name__ == '__main__':
    app.run(debug=True)
