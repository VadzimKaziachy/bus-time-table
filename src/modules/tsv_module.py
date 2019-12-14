import csv
from typing import Dict, NoReturn, List

from src.models.Bus import Bus
from src.modules.base_module import BaseData
from settings.base import DEFAULT_FILE_NAME


class TsvModule(BaseData):

    """
    One of the modules that allows you to work with .tsv files.
    """

    def __init__(self):
        self.format_file: str = '.tsv'
        self.data: List[Dict] = list()
        self.default_file_name: str = DEFAULT_FILE_NAME

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding='utf8') as tsv:
            self.data = [obj for obj in csv.DictReader(tsv, dialect='excel-tab', delimiter=',')]
        return self.data

    def write(self, path: str, buses: List[Dict]) -> NoReturn:
        if all(isinstance(bus, dict) for bus in buses):
            path = self.get_file_path(path=path, file_name=self.default_file_name, format_file=self.format_file)
            with open(path, 'w', newline='') as tsv:
                tsv_file = csv.DictWriter(tsv, delimiter=',', fieldnames=Bus.get_fieldnames())
                tsv_file.writeheader()
                tsv_file.writerows(buses)
