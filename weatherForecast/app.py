from flask import Flask, render_template, request, jsonify
from API_fetch import get_current_weather, get_weather_forecast, get_hourly_weather
from main import display_wether_forcast, display_hourly_wether
import os
from flask import send_from_directory

# Define the directory to store static files (images)
IMAGE_DIR = os.path.join(os.path.dirname(__file__), 'static/image')


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')


# Add a route to serve static files
@app.route('/static/image/<path:path>')
def serve_static(path):
    return send_from_directory(IMAGE_DIR, path)


@app.route('/current_weather', methods=['POST'])
def current_weather():
    city = request.json.get('city')
    weather_info = get_current_weather(city)
    return jsonify(weather_info)

@app.route('/weather_forecast', methods=['POST'])
def weather_forecast():
    city = request.json.get('city')
    image_path = display_wether_forcast(city)
    # Move the image file to the static directory
    static_image_path = os.path.join(IMAGE_DIR, os.path.basename(image_path))
    os.rename(image_path, static_image_path)
    image_path=os.path.join("../static/image/",os.path.basename(image_path))
    return jsonify({'image_url': image_path}), 200

@app.route('/hourly_weather', methods=['POST'])
def hourly_weather():
    city = request.json.get('city')
    image_path = display_hourly_wether(city)
    # Move the image file to the static directory
    static_image_path = os.path.join(IMAGE_DIR, os.path.basename(image_path))
    os.rename(image_path, static_image_path)
    image_path=os.path.join("../static/image/",os.path.basename(image_path))
    return jsonify({'image_url': image_path}), 200

if __name__ == '__main__':
    app.run(debug=True)
