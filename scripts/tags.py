import json
import requests

class scryfall:
    def __init__(self):
        self.o_tags = scryfall.import_tags("oracle")
        self.art_tags = scryfall.import_tags("illustration")

    def import_tags(type):
        tags_raw = requests.get(f"https://api.scryfall.com/private/tags/{type}")
        return tags_raw.json()["data"]