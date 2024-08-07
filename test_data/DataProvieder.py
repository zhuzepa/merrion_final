import json


class DataProvider:
    def __init__(self, filename: str) -> None:
        with open(filename) as filename:
            self.data = json.load(filename)

    def get(self, key):
        return self.data.get(key)
