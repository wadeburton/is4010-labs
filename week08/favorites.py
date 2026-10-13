"""Save named locations in a JSON file."""

import json
from pathlib import Path


class FavoritesManager:
    def __init__(self, filename):
        self.filename = Path(filename)
        try:
            data = json.loads(self.filename.read_text(encoding="utf-8"))
            self.favorites = {
                name.casefold(): location for name, location in data.items()
                if isinstance(name, str) and isinstance(location, str)
            } if isinstance(data, dict) else {}
        except (OSError, ValueError):
            self.favorites = {}

    def _save(self):
        self.filename.write_text(json.dumps(self.favorites, indent=2), encoding="utf-8")

    def add(self, name, location):
        name = name.casefold()
        if name in self.favorites:
            return False
        self.favorites[name] = location
        self._save()
        return True

    def remove(self, name):
        name = name.casefold()
        if name not in self.favorites:
            return False
        del self.favorites[name]
        self._save()
        return True

    def list_all(self):
        return self.favorites.copy()

    def get_location(self, name):
        return self.favorites.get(name.casefold())
