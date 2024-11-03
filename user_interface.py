from weather_data_fetcher import WeatherDataFetcher
from data_parser import DataParser

class UserInterface:
    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = DataParser()

    def display_weather(self, city):
        #display basic weather forecast for a city
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse_weather_data(data)
            print(weather_report)

    def get_detailed_forecast(self, city):
        #provide a detailed weather forecast for a city
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)