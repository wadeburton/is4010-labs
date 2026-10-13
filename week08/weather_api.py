"""WeatherAPI requests and readable weather summaries."""

import requests


class WeatherAPI:
    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _request(self, endpoint, location, **extra):
        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}",
                params={"key": self.api_key, "q": location, **extra},
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

    def get_current_weather(self, location):
        return self._request("current.json", location)

    def get_forecast(self, location, days=3):
        if days not in (1, 2, 3):
            raise ValueError("Forecast days must be between 1 and 3")
        return self._request("forecast.json", location, days=days)


def format_current_weather(data):
    location, current = data["location"], data["current"]
    return (
        f"{location['name']}, {location['country']}: "
        f"{current['temp_f']}°F, {current['condition']['text']}"
    )


def format_forecast(data):
    return "\n".join(
        f"{entry['date']}: high {entry['day']['maxtemp_f']}°F, "
        f"low {entry['day']['mintemp_f']}°F, {entry['day']['condition']['text']}"
        for entry in data["forecast"]["forecastday"]
    )
