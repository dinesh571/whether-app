# Weather Forecast App

A Python and Flask weather application prototype for looking up a city and exploring weather forecasts. The supplied project archive includes experimental time-series forecasting modules using ARIMA and Support Vector Regression (SVR/SVM), alongside a web interface and a command-line runner.

## Features in the supplied project

- Flask web interface and JSON endpoints for city lookup and forecast requests
- City geocoding and daily weather data from Open-Meteo
- Experimental ARIMA and SVR-based forecast visualizations and data tables
- Command-line entry point for running either forecasting method or both

## Project files

The supplied archive contains `weatherapp.py`, `logone.py`, `logtwo.py`, `city.py`, and `templates/index.html`. The current GitHub repository contains only `weatherapp.py` and `index.html`; the additional modules and the `templates/` directory have not been uploaded, so the complete app may not run from this repository yet.

## Requirements

The supplied Python files use Flask, requests, pandas, matplotlib, statsmodels, scikit-learn, and NumPy. A dependency manifest is not included in the archive; install compatible package versions in a virtual environment before running the full project.

## Running locally

From the project directory, after installing the dependencies and adding the missing project files:

```bash
python weatherapp.py
```

Open `http://127.0.0.1:5000/` in a browser. To run forecasts from the command line:

```bash
python city.py
```

The application uses external weather/geocoding services and requires an API key for the city lookup endpoint. Configure API credentials outside source control, such as with environment variables; never commit real keys.

## Important

Forecasts are experimental and are not a substitute for official weather warnings or professional advice. External API availability, terms, and rate limits apply.