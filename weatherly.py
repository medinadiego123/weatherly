import requests
import matplotlib.pyplot as plt
import numpy as np

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, city, units="metric"):
        """Fetch weather data for a given city."""
        try:
            # Convert user-friendly units 'c' and 'f' to API-compatible 'metric' and 'imperial'
            units = "metric" if units == "c" else "imperial"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': units  # Get data in Celsius or Fahrenheit
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def display_weather(self, data, units="c"):
        """Display weather details."""
        if data:
            city = data['name']
            temp = data['main']['temp']
            weather = data['weather'][0]['description']
            unit_symbol = "°C" if units == "c" else "°F"
            print(f"\nWeather in {city}:")
            print(f"Temperature: {temp:.1f}{unit_symbol}")
            print(f"Description: {weather.capitalize()}")
            return temp
        else:
            print("Error: Unable to display weather data.")
            return None

    def plot_temperature(self, cities, temperatures, units="c"):
        """Generate a bar chart for temperature comparison."""
        unit_label = "Temperature (°C)" if units == "c" else "Temperature (°F)"

        plt.figure(figsize=(10, 6))
        bars = plt.bar(cities, temperatures, color=plt.cm.coolwarm(np.linspace(0.2, 0.8, len(cities))))
        
        plt.title("Temperature Comparison by City", fontsize=16, fontweight="bold")
        plt.xlabel("Cities", fontsize=12)
        plt.ylabel(unit_label, fontsize=12)

        # Temperature labels above the bars
        for bar, temp in zip(bars, temperatures):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 1, f"{temp:.1f}",
                     ha='center', va='bottom', fontsize=10, color="white")

        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

def main():
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    app = WeatherApp(api_key)

    cities = []
    temperatures = []

    print("\nWelcome to Weatherly - Your Simple Weather App!")
    units = input("Choose temperature units - type 'C' for Celsius or 'F' for Fahrenheit: ").strip().lower()
    if units not in ["c", "f"]:
        print("Invalid units, defaulting to Celsius.")
        units = "c"

    while True:
        city = input("\nEnter city name (or type 'done' to finish): ").strip()
        if city.lower() == 'done':
            break
        data = app.get_weather_data(city, units=units)
        temp = app.display_weather(data, units=units)
        if temp is not None:
            cities.append(city.title())
            temperatures.append(temp)

    if cities:
        print("\nGenerating temperature comparison chart...")
        app.plot_temperature(cities, temperatures, units=units)
    else:
        print("No cities entered. Exiting...")

if __name__ == "__main__":
    main()
