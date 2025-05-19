import requests

def fetch_weather(city_name, api_key):
    """Fetches weather data for a given city using OpenWeatherMap API."""
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad response codes
        data = response.json()

        # Extract weather information
        city = data["name"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Print weather report
        print(f"\n🌤️ Weather Report for {city}")
        print("-" * 30)
        print(f"Temperature     : {temperature} °C")
        print(f"Condition       : {weather.title()}")
        print(f"Humidity        : {humidity}%")
        print(f"Wind Speed      : {wind_speed} m/s")

    except requests.exceptions.HTTPError:
        print("❌ Error: City not found or invalid API key.")
    except requests.exceptions.ConnectionError:
        print("❌ Network Error: Please check your internet connection.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

# ------------------ Main Program ------------------

if __name__ == "__main__":
    print("=== Weather App ===")
    city = input("Enter city name: ")
    api_key = "baee44366bc5884d2ca94645125edb08"  # Your working API key
    if not api_key:
        print("❌ API key is missing.")
    else:
        fetch_weather(city, api_key)
