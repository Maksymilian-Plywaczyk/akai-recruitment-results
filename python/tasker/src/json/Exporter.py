import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        # TODO zapisz taski do pliku tutaj
        with open('taski.json', 'w', encoding='utf-8') as file:
            json.dump(tasks, file, ensure_ascii=False)
