"""Command-line weather and favorite-location management."""

import argparse
import os
from pathlib import Path
import sys

if __package__:
    from .favorites import FavoritesManager
    from .weather_api import WeatherAPI, format_current_weather, format_forecast
else:
    from favorites import FavoritesManager
    from weather_api import WeatherAPI, format_current_weather, format_forecast

FAVORITES_FILE = Path(__file__).with_name("favorites.json")


def load_api_key():
    key = os.environ.get("WEATHER_API_KEY")
    if key:
        return key
    try:
        if __package__:
            from .config import WEATHER_API_KEY
        else:
            from config import WEATHER_API_KEY
        return WEATHER_API_KEY if WEATHER_API_KEY != "YOUR_API_KEY_HERE" else None
    except ImportError:
        return None


def build_parser():
    parser = argparse.ArgumentParser(description="Look up weather and save favorite locations")
    commands = parser.add_subparsers(dest="command", required=True)
    current = commands.add_parser("current")
    current.add_argument("location")
    forecast = commands.add_parser("forecast")
    forecast.add_argument("location")
    forecast.add_argument("--days", type=int, choices=(1, 2, 3), default=3)
    favorites = commands.add_parser("favorites")
    actions = favorites.add_subparsers(dest="favorites_command", required=True)
    add = actions.add_parser("add")
    add.add_argument("name")
    add.add_argument("location")
    actions.add_parser("list")
    remove = actions.add_parser("remove")
    remove.add_argument("name")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    favorites = FavoritesManager(FAVORITES_FILE)
    try:
        if args.command == "favorites":
            if args.favorites_command == "list":
                for name, location in favorites.list_all().items():
                    print(f"{name}: {location}")
            elif args.favorites_command == "add":
                if not favorites.add(args.name, args.location):
                    print("Favorite already exists", file=sys.stderr)
                    return 1
            elif not favorites.remove(args.name):
                print("Favorite not found", file=sys.stderr)
                return 1
            return 0

        key = load_api_key()
        if not key:
            print("Missing API key: set WEATHER_API_KEY or config.py", file=sys.stderr)
            return 1
        client = WeatherAPI(key)
        location = favorites.get_location(args.location) or args.location
        if args.command == "current":
            data = client.get_current_weather(location)
            formatter = format_current_weather
        else:
            data = client.get_forecast(location, days=args.days)
            formatter = format_forecast
        if data is None:
            print("Weather request failed", file=sys.stderr)
            return 1
        print(formatter(data))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Unable to complete command: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
