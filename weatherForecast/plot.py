import matplotlib.pyplot as plt 
import tempfile
import os

def plot_weather_forecast(data, city):
    dates = [entry['date'] for entry in data]
    temperatures = [entry['temperature'] for entry in data]
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temperatures, marker='o', linestyle='-')
    plt.title(f'Temperature data, {city}')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    # plt.show()

     # Save the graph as an image file
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        image_path = temp_file.name
        plt.savefig(image_path)
    
    plt.close()
    return image_path


def plot_hourly_weather(data, city):
    hours = [entry['time'] for entry in data]
    temperatures = [entry['temperature'] for entry in data]
    plt.figure(figsize=(10, 6))
    plt.plot(hours, temperatures, marker='o', linestyle='-')
    plt.title(f'Temperature data, {city}')
    plt.xlabel('Hour')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    # plt.show()

     # Save the graph as an image file
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        image_path = temp_file.name
        plt.savefig(image_path)
    
    plt.close()
    return image_path

    