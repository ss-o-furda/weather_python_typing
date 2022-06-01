import json
import ssl
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from json.decoder import JSONDecodeError
from typing import Literal
from urllib.error import URLError

import config
from coordinates import Coordinates
from exceptions import ApiServiceError
from geo import City, get_city

Celsius = int


class WeatherType(Enum):
    THUNDERSTORM = "thunderstorm"
    DRIZZLE = "drizzle"
    RAIN = "rain"
    SNOW = "snow"
    CLEAR = "clear"
    FOG = "fog"
    CLOUDS = "clouds"


@dataclass
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: City


def get_weather(coordinates: Coordinates, city: City) -> Weather:
    """Get weather data from some service (openweather in this case)
    and return Weather object

    Args:
        coordinates (Coordinates): current location

    Returns:
        Weather: current weather data from location
    """
    openweather_response = _get_openweather_response(
        latitude=coordinates.latitude, longitude=coordinates.longitude)
    weather = _parse_openweather_response(openweather_response, city)
    return weather


def _get_openweather_response(latitude: float, longitude: float) -> str:
    ssl._create_default_https_context = ssl._create_unverified_context
    url = config.OPENWEATHER_URL.format(latitude=latitude, longitude=longitude)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise ApiServiceError


def _parse_openweather_response(openweather_response: str, city: City) -> Weather:
    try:
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise ApiServiceError
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, "sunrise"),
        sunset=_parse_sun_time(openweather_dict, "sunset"),
        city=city
    )


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict["main"]["temp"])


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS,
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError


def _parse_sun_time(openweaher_dict: dict, time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(openweaher_dict["sys"][time])


if __name__ == "__main__":
    print(get_weather(Coordinates(latitude=49.84, longitude=24.02), City(name="Lviv")))
