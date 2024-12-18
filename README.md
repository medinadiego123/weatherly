# Weatherly - Your Simple Weather App 🌤️

## Overview
Weatherly is a simple, user-friendly weather application that fetches real-time weather data from the OpenWeatherMap API. The app allows users to check the temperature and weather conditions of multiple cities and compare their temperatures using a visually appealing bar graph.

---

## Features
- **Real-time Weather Data**: Fetches weather conditions for any city in the world.
- **Celsius/Fahrenheit Support**: Choose your preferred temperature unit.
- **Bar Graph Visualization**: Compare temperatures of multiple cities.
- **User-Friendly Interface**: Easy inputs and clear outputs.

---

## Requirements
1. **Python 3.x** installed.
2. **OpenWeatherMap API Key**:
   - Get a free API key by signing up at [OpenWeatherMap](https://openweathermap.org/api).
3. Install the following Python libraries:
   - `requests`
   - `matplotlib`
   - `numpy`

---

## Project Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/weatherly.git
   cd weatherly
2. Install dependencies: pip install requests matplotlib numpy
3. Create a free OpenWeatherMap API key: Visit: https://openweathermap.org/api
Copy the API key.
4. Run the program: python weatherly.py

## How to Use
Start the App:

Enter your OpenWeatherMap API Key when prompted.
Choose Temperature Unit:

Type C for Celsius or F for Fahrenheit.
Enter City Names:

Type any city name to fetch its weather.
Type done to stop and view the temperature graph.
View Results:

The app displays the temperature and weather description.
A bar chart compares the temperatures of all entered cities.

## Example run
Welcome to Weatherly - Your Fancy Weather App!
Choose temperature units - type 'C' for Celsius or 'F' for Fahrenheit: C

Enter city name (or type 'done' to finish): Tokyo
Weather in Tokyo:
Temperature: 23.5°C
Description: Clear sky

Enter city name (or type 'done' to finish): New York
Weather in New York:
Temperature: 19.1°C
Description: Few clouds

Enter city name (or type 'done' to finish): done

Generating temperature comparison chart...

# A bar graph will appear, visually comparing the temperatures of the entered cities.

## Notes
1. Ensure your internet connection is active.
2. If you receive a 401 Unauthorized error, double-check your API key.
3. API Key Security: Do not hardcode your API key in the code if you are uploading it publicly.