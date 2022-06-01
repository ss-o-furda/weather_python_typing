OPENWEATHER_API_KEY = "" # you can get your api key free on openweathermap.org
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=" + \
    OPENWEATHER_API_KEY + "&lang=en&units=metric"

GEO_API_KEY = "" # you can get your api key free on locationiq.com
GEO_URL = "https://eu1.locationiq.com/v1/reverse.php?key=" + GEO_API_KEY + \
    "&lat={latitude}&lon={longitude}&accept-language=en&normalizeaddress=1&format=json"
