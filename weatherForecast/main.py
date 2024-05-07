from API_fetch import get_current_weather, get_weather_forecast, get_hourly_weather
from plot import plot_weather_forecast, plot_hourly_weather

def display_current_weather(city):
    weather_info = get_current_weather(city)
    if weather_info:
        location = weather_info.get('location', {})
        data = weather_info.get('data', {})
        values = data.get('values', {})
        print(f"Weather in {location.get('name')}:")
        print(f"Temperature: {values.get('temperature')}°C")
        print(f"Feels like: {values.get('temperatureApparent')}°C")
    else:
        print("Error fetching current weather data.")

def display_wether_forcast(city):
    weather_info = get_weather_forecast(city)
    if weather_info:
        timelines = weather_info.get('timelines',{})
        minutely = timelines.get('minutely',{})
        hourly = timelines.get('hourly',{})
        daily = timelines.get('daily',{})
        location = weather_info.get('location', {})
        weather_forecast = []
        for enteries in daily:
            weather_forecast_info = {
                "date" : enteries["time"][:10],
                "temperature" : enteries["values"]["temperatureAvg"]
            }
            weather_forecast.append(weather_forecast_info)
        return plot_weather_forecast(weather_forecast,city)
    else:
        print("Error fetching weather forecast data.")

def display_hourly_wether(city):
    weather_info = get_hourly_weather(city)
    if weather_info:
        timelines = weather_info.get('timelines',{})
        hourly = timelines.get('hourly',{})
        daily = timelines.get('daily',{})
        location = weather_info.get('location', {})
        hourly_weather = []
        for enteries in hourly:
            weather_forecast_info = {
                "time" : enteries["time"][11:-5],
                "temperature" : enteries["values"]["temperature"]
            }
            hourly_weather.append(weather_forecast_info)
        return plot_hourly_weather(hourly_weather,city)
    else:
        print("Error fetching hourly weather data.")

def main():
    city = input("Enter city name: ")
    display_current_weather(city)
    # display_wether_forcast(city)
    # display_hourly_wether(city)

if __name__ == "__main__":
    main()