from .RatioObtainer import RatioObtainer
import os


class App:
    base_currency = None
    target_currency = None
    amount = None
    _cache_name = 'ratios.json'

    def __init__(self, command_arguments):
        self.amount = command_arguments[1]
        self.base_currency = command_arguments[2]
        self.target_currency = command_arguments[3]
        if not os.path.exists(self._cache_name):
            self.create_cache()

    def get_result_equation(self):
        base_currency_amount = str(self.amount) + " " + str(self.base_currency)
        target_currency_amount = str(self.get_ratio() * float(self.amount)) + " " + self.target_currency
        return base_currency_amount + " = " + target_currency_amount

    def get_ratio(self):
        obtainer = RatioObtainer(base=self.base_currency, target=self.target_currency)
        print(obtainer.was_ratio_saved_today())
        if not obtainer.was_ratio_saved_today():
            obtainer.fetch_ratio()
        return obtainer.get_matched_ratio_value()

    def create_cache(self):
        open(self._cache_name, 'w')
