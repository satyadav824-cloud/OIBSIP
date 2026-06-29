import requests
from datetime import datetime
import time

# ==============================
# OpenWeather API Key
# ==============================
API_KEY = "65c58b45008944391f9a2cf1e6223a71"


def banner():
    print("=" * 65)
    print("🌦️           LIVE WEATHER DASHBOARD 2.0")
    print("=" * 65)


def loading():
    print("\nFetching Weather Data", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")


def get_weather_emoji(weather):
    weather = weather.lower()

    if "clear" in weather:
        return "☀️"
    elif "cloud" in weather:
        return "☁️"
    elif "rain" in weather:
        return "🌧️"
    elif "drizzle" in weather:
        return "🌦️"
    elif "thunderstorm" in weather:
        return "⛈️"
    elif "snow" in weather:
        return "❄️"
    elif "mist" in weather or "fog" in weather or "haze" in weather:
        return "🌫️"
    else:
        return "🌍"


while True:

    banner()

    city = input("\n🏙️ Enter City Name : ")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={API_KEY}&units=metric"
    )

    loading()

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            weather = data["weather"][0]["description"]
            emoji = get_weather_emoji(weather)

            sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset = datetime.fromtimestamp(data["sys"]["sunset"])

            now = datetime.now()

            print("=" * 65)
            print("📅 Date :", now.strftime("%d-%m-%Y"))
            print("🕒 Time :", now.strftime("%I:%M:%S %p"))
            print("=" * 65)

            print(f"📍 City          : {data['name']}")
            print(f"🌍 Country       : {data['sys']['country']}")
            print(f"📌 Coordinates   : {data['coord']['lat']}, {data['coord']['lon']}")
            print(f"🌡️ Temperature   : {data['main']['temp']} °C")
            print(f"🤗 Feels Like    : {data['main']['feels_like']} °C")
            print(f"🔺 Max Temp      : {data['main']['temp_max']} °C")
            print(f"🔻 Min Temp      : {data['main']['temp_min']} °C")
            print(f"💧 Humidity      : {data['main']['humidity']} %")
            print(f"📊 Pressure      : {data['main']['pressure']} hPa")
            print(f"👀 Visibility    : {data['visibility']/1000} km")
            print(f"💨 Wind Speed    : {data['wind']['speed']} m/s")
            print(f"☁️ Cloud Cover   : {data['clouds']['all']} %")
            print(f"{emoji} Weather      : {weather.title()}")
            print(f"🌅 Sunrise       : {sunrise.strftime('%I:%M:%S %p')}")
            print(f"🌇 Sunset        : {sunset.strftime('%I:%M:%S %p')}")

            print("=" * 65)

        elif response.status_code == 404:
            print("❌ City not found. Please enter a valid city.")

        elif response.status_code == 401:
            print("❌ Invalid API Key.")

        else:
            print("⚠️ Something went wrong.")

    except requests.exceptions.ConnectionError:
        print("❌ No Internet Connection.")

    except Exception as e:
        print("❌ Error:", e)

    again = input("\n🔄 Search another city? (yes/no): ").lower()

    if again != "yes":
        print("\n🙏 Thank you for using Weather Dashboard 2.0")
        print("👋 Have a Great Day!")
        break