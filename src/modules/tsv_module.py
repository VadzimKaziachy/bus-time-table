import csv
from typing import Dict, NoReturn, List

from src.models.autobus import Autobus
from src.modules.base_module import BaseData


class TsvModule(BaseData):

    """
    One of the modules that allows you to work with .tsv files.
    """

    def __init__(self, path: str):
        self.path: str = path
        self.data: List[Dict] = list()

    def read(self) -> List[Dict]:
        with open(self.path, encoding='utf8') as tsv:
            self.data = [obj for obj in csv.DictReader(tsv, dialect='excel-tab', delimiter=',')]
        return self.data

    def write(self, buses: List[Dict]) -> NoReturn:
        if all(isinstance(bus, dict) for bus in buses):
            with open(self.path, 'w', newline='') as tsv:
                tsv_file = csv.DictWriter(tsv, delimiter=',', fieldnames=Autobus.get_fieldnames())
                tsv_file.writeheader()
                tsv_file.writerows(buses)
