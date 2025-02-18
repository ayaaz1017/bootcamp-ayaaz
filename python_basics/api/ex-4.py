import requests
import argparse

# Function to fetch weather data from OpenWeatherMap
def fetch_weather(city, api_key):
    # URL for the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Send a request to the API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extract weather details
        city_name = data.get("name", "Unknown City")
        temp = data["main"].get("temp", "N/A")
        description = data["weather"][0].get("description", "No description available")
        humidity = data["main"].get("humidity", "N/A")
        wind_speed = data["wind"].get("speed", "N/A")

        # Display weather details
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        print("Possible reasons: Invalid API key, exceeded limit, or incorrect request format.")

# Set up command-line argument parsing
def main():
    parser = argparse.ArgumentParser(description="Fetch weather details for a city.")
    parser.add_argument("city", type=str, help="The name of the city to fetch the weather for.")
    parser.add_argument("api_key", type=str, help="Your OpenWeatherMap API key.")
    args = parser.parse_args()

    # Fetch weather data
    fetch_weather(args.city, args.api_key)

if __name__ == "__main__":
    main()
