import json
import requests
from datetime import datetime
import os
from . import App


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self) -> bool:
        # TODO
        with open(App.App.CACHE_NAME, 'r') as file:
            currency_data = json.load(file)
        for rate in currency_data:
            # Assign to variable to better visualization and quick change if it is necessary
            check_currency = rate['base_currency'] == self.base and rate['target_currency'] == self.target
            if check_currency and rate['date_fetched'] != str(datetime.today().date()):
                return False
            elif not check_currency and rate['date_fetched'] != str(datetime.today().date()):
                return False
        return True

        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        url = f"https://api.exchangerate.host/convert?from={self.base}&to={self.target}"
        response = self.getRequest(url=url)
        data = response.json()
        ratio = {"base_currency": data['query']['from'], "target_currency": data['query']['to'],
                 "date_fetched": data['date'], "ratio": data['info']['rate']}
        self.save_ratio(ratio=ratio)

    def save_ratio(self, ratio: dict):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        if os.path.getsize(App.App.CACHE_NAME) == 0:
            exchange_list = [ratio]
            with open('ratios.json', 'w') as file:
                json.dump(exchange_list, file)

        with open(App.App.CACHE_NAME, 'r') as file:
            data = json.load(file)
        for day in data:

            if day['base_currency'] == ratio['base_currency'] and day['target_currency'] == ratio['target_currency']:
                day['ratio'] = ratio['ratio']
                day['date_fetched'] = ratio['date_fetched']
            if ratio not in data:
                data.append(ratio)
        with open(App.App.CACHE_NAME, 'w') as file:
            json.dump(data, file)

    def get_matched_ratio_value(self) -> float:
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        with open(App.App.CACHE_NAME, 'r') as file:
            data = json.load(file)
        for ratio in data:
            if ratio['base_currency'] == self.base and ratio['target_currency'] == self.target:
                return ratio['ratio']

    @staticmethod
    def getRequest(url) -> requests.Response:
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
        return response
