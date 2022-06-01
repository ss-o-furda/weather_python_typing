import json
import ssl
import urllib.request
from json.decoder import JSONDecodeError
from typing import NamedTuple
from urllib.error import URLError

import config
from coordinates import Coordinates
from exceptions import GeoServiceError


class City(NamedTuple):
    name: str


def get_city(coordinates: Coordinates) -> City:
    """Get city or state name by coordinates and return City object

    Args:
        coordinates (Coordinates): current location

    Returns:
        City: city or state name
    """
    geo_service_response = _get_geo_response(
        latitude=coordinates.latitude, longitude=coordinates.longitude)
    city = _parse_geo_response(geo_service_response)
    return city


def _get_geo_response(latitude: float, longitude: float) -> str:
    ssl._create_default_https_context = ssl._create_unverified_context
    url = config.GEO_URL.format(latitude=latitude, longitude=longitude)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise GeoServiceError


def _parse_geo_response(geo_response: str) -> City:
    try:
        geo_response_dict = json.loads(geo_response)
    except JSONDecodeError:
        raise GeoServiceError
    return City(name=_parse_city_name(geo_response_dict))


def _parse_city_name(geo_response_dict: dict) -> str:
    try:
        city_name = geo_response_dict["address"].get(
            "city", geo_response_dict["address"]["state"])
    except KeyError:
        raise GeoServiceError
    return city_name


if __name__ == "__main__":
    print(get_city(Coordinates(latitude=49.84, longitude=24.02)))
