from meteostat import Point, Daily
import pandas as pd
from datetime import datetime

# Місце: Регенсбург
regensburg = Point(49.0151, 12.1016, 350)

# Часовий діапазон
start = datetime(1973, 1, 1)
end = datetime(2024, 12, 31)

# Завантажити щоденні дані
data = Daily(regensburg, start, end)
data = data.fetch()

# Зберегти у CSV


print(data.head())


data.to_csv("C:/projects/python/ML/weather/regensburg_weather.csv")