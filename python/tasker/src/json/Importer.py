import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open('taski.json', 'r', encoding='utf-8') as file:
            decode_json = json.load(file)
            return decode_json

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        decode_tasks = self.read_tasks()
        return decode_tasks
