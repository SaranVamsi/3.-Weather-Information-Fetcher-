import requests

def fetch_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    try:
        # API request
        params = {"q": city_name, "appid": api_key, "units": "metric"}
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extracting relevant weather information
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        # Displaying weather details
        print(f"\nWeather in {city_name.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("City not found. Please enter a valid city name.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    print("Weather Information Fetcher")
    while True:
        city_name = input("\nEnter city name (or type 'exit' to quit): ").strip()
        if city_name.lower() == "exit":
            print("Goodbye!")
            break
        fetch_weather(city_name, api_key)

if _name_ == "_main_":
    main()
