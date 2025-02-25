# Weather Forecast App

## Overview
The Weather Forecast App is a simple web-based application that provides real-time weather updates, forecasts, and hourly weather predictions for a given city. The app fetches data from an API and displays relevant weather information to the user.

## Features
- Fetch current weather information for any city.
- Get detailed weather forecasts.
- View hourly weather predictions.
- Visualize forecast data with graphical representations.

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **API Integration:** Fetches weather data from an external weather API
- **Data Visualization:** Uses Matplotlib to generate weather graphs

## Installation & Setup

### Prerequisites
- Python 3.x
- Flask
- Matplotlib
- Requests

### Steps to Run the App
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/weather-forecast-app.git
   cd weather-forecast-app
   ```

2. Install required dependencies:
   ```sh
   pip install flask matplotlib requests
   ```

3. Run the Flask server:
   ```sh
   python app.py
   ```

4. Open `index.html` in a web browser or run a local server.

## API Endpoints
- `POST /current_weather`: Fetches current weather for the given city.
- `POST /weather_forecast`: Retrieves weather forecast data.
- `POST /hourly_weather`: Provides hourly weather updates.

## Usage
1. Enter the city name in the input field.
2. Click on:
   - "Get Current Weather" to see live weather updates.
   - "Get Weather Forecast" to view future weather trends.
   - "Get Hourly Weather" to see temperature variations throughout the day.
3. The results will be displayed below the input field.

## Screenshots
(Add screenshots here if available)

## Future Enhancements
- Improve UI/UX with better styling.
- Add more weather metrics like humidity, wind speed, and precipitation.
- Implement geolocation-based weather detection.

## License
This project is licensed under the MIT License.

---
Made with ❤️ by SatanSanta17

