from meteostat import Point, Daily
import pandas as pd
from datetime import datetime
import os

csv_path = "regensburg_weather.csv"

# Create CSV file with historical data if not exists
if not os.path.exists(csv_path):
    # City: Regensburg, Germany
    # Coordinates: 49.0151° N, 12.1016° E
    regensburg = Point(49.0151, 12.1016, 350)
    # Time Range
    # Start: 1973-01-01 
    start = datetime(1973, 1, 1)
    end = datetime(2024, 12, 31)

    # Download daily data
    # Daily data includes temperature, precipitation, wind speed, etc.
    # Fetch daily data for the specified time range
    data = Daily(regensburg, start, end)
    data = data.fetch()

    # Save the data to a CSV file 
    print(data.head())
    data.to_csv("C:/projects/python/ML/weather/regensburg_weather.csv")