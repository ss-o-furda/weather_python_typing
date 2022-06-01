from geo import City
from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Formatting weather data in human view, making some nice text

    Args:
        weather (Weather): raw weather data

    Returns:
        str: A beautiful string that describes the current weather
    """
    return (f"It is {weather.weather_type.value} in {weather.city.name} now, "
            f"the temperature is about {weather.temperature}°C.\n"
            f"The sun rose at {weather.sunrise.strftime('%H:%M')}, "
            f"and will set at {weather.sunset.strftime('%H:%M')}.")


if __name__ == "__main__":
    from datetime import datetime

    from weather_api_service import WeatherType
    print(format_weather(Weather(
        temperature=25,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2022-06-01 04:00:00"),
        sunset=datetime.fromisoformat("2022-06-01 21:20:00"),
        city=City(name='Lviv')
    )))
