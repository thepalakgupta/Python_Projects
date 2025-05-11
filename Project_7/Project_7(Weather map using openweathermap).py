import requests

API_KEY = "9791065bf3d3f9b728b6d105224b9e88" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'City': data['name'],
            'Temperature': f"{data['main']['temp']} °C",
            'Description': data['weather'][0]['description'],
            'Humidity': f"{data['main']['humidity']}%",
            'Wind Speed': f"{data['wind']['speed']} m/s"
        }
        return weather
    else:
        return None

def main():
    print("🌤️ Weather App - OpenWeatherMap")
    city = input("Enter city name: ")

    weather = get_weather(city)

    if weather:
        print("\n📍 Weather Info:")
        for key, value in weather.items():
            print(f"{key}: {value}")
    else:
        print("City not found or API error.")

# Run the app
main()
