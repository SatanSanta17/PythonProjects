function fetchCurrentWeather() {
	var city = document.getElementById("city-input").value;
	fetch("/current_weather", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ city: city }),
	})
		.then((response) => response.json())
		.then((data) => {
			console.log(data);
			let output = `
				<p>Weather in ${data.location.name}:</p>
				<p>Temperature: ${data.data.values.temperature}°C</p>
				<p>Feels like: ${data.data.values.temperatureApparent}°C</p>
			`;
			document.getElementById("weather-output").innerHTML = output;
		})
		.catch((error) => {
			console.error("Error:", error);
		});
}

// Similarly, define fetchWeatherForecast() and fetchHourlyWeather() functions

function fetchWeatherForecast() {
	var city = document.getElementById("city-input").value;
	// Make AJAX request to fetch weather forecast data for the city
	// Update the UI with the fetched data
	fetch("/weather_forecast", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ city: city }),
	})
		.then((response) => {
			if (!response.ok) {
				throw new Error("Network response was not ok");
			}
			return response.json();
		})
		.then((data) => {
			const imageUrl = data.image_url;
			console.log(imageUrl);
			// Display the image in an <img> tag
			document.getElementById(
				"weather-output"
			).innerHTML = `<img class="graph" src="${imageUrl}" alt="Hourly Weather">`;
		})
		.catch((error) => {
			console.error("Error during fetch request:", error);
		});
}

function fetchHourlyWeather() {
	var city = document.getElementById("city-input").value;
	fetch("/hourly_weather", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ city: city }),
	})
		.then((response) => {
			if (!response.ok) {
				throw new Error("Network response was not ok");
			}
			return response.json();
		})
		.then((data) => {
			const imageUrl = data.image_url;
			console.log(imageUrl);
			// Display the image in an <img> tag
			document.getElementById(
				"weather-output"
			).innerHTML = `<img class="graph" src="${imageUrl}" alt="Hourly Weather">`;
		})
		.catch((error) => {
			console.error("Error during fetch request:", error);
		});
}
