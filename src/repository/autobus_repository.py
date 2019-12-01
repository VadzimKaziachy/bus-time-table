import os
import logging.config

from typing import List, NoReturn, Dict

from src.models.autobus import Autobus
from src.modules.tsv_module import TsvModule
from src.settings.base import FILE_NAME
from src.settings.logging import LOGGING

logging.config.dictConfig(LOGGING)

logger = logging.getLogger('app')


class AutobusRepository:

    def __init__(self, path: str) -> NoReturn:
        self.tsv_module = TsvModule(path)
        self.buses: List[Autobus] = list()

    def save_in_file(self) -> NoReturn:
        """
        The method is required to write data to a file.
        :return: no return
        """
        buses = [bus.dict_obj() for bus in self.buses]
        self.tsv_module.write(buses)

    @staticmethod
    def is_correct_data(buses: List[Dict[str, str]]) -> bool:
        """
        This method is required to check the availability of the required fields.
        :param buses: List[Dict[str, str]]
        :return: bool
        """
        return all(
            bus.get('time', None)
            and bus.get('final_point', None)
            and bus.get('route_number', None)
            and bus.get('starting_point', None)
            for bus in buses
        )

    def get_data(self) -> NoReturn:
        """
        Receiving data from a file, moreover, a .tsv file corresponding to the module name.
        :return: no return
        """
        buses = self.tsv_module.read()
        if self.is_correct_data(buses):
            self.buses = [
                Autobus(
                    time=bus.get('time'),
                    final_point=bus.get('final_point'),
                    route_number=bus.get('route_number'),
                    starting_point=bus.get('starting_point')
                )
                for bus in buses
            ]

    def sort_buses(self, reverse: bool) -> List[Autobus]:
        """
        The method is intended for sorting buses by bus number.
        :param reverse: bool
        :return: List[Autobus]
        """
        return sorted(self.buses, key=lambda bus: bus.route_number, reverse=reverse)

    def get_buses_by_point(self, point: str) -> List[Autobus]:
        """
        The method is required to search for buses at the start or end stop.
        :param point: str
        :return: List[Autobus]
        """
        return list(
            filter(lambda bus: bus.starting_point == point or bus.final_point == point, self.buses)
        )


def enumerate_buses(buses: List[Autobus], message: str) -> NoReturn:
    """
    This function should not attract your attention, it is only needed for debugging the application.
    :param buses: List[Autobus]
    :param message: str
    :return: no return
    """
    logger.info('-----------')
    logger.info(message)
    for bus in buses:
        logger.info(bus)
    logger.info('-----------')


def main() -> NoReturn:
    repository = AutobusRepository(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), FILE_NAME))

    repository.buses.append(Autobus(starting_point='point A', final_point='point B', route_number=1, time='15'))
    repository.buses.append(Autobus(starting_point='point B', final_point='point C', route_number=2, time='16'))
    repository.buses.append(Autobus(starting_point='point C', final_point='point D', route_number=3, time='17'))
    repository.buses.append(Autobus(starting_point='point B', final_point='point F', route_number=4, time='18'))

    repository.save_in_file()

    repository.get_data()

    buses = repository.sort_buses(reverse=True)
    enumerate_buses(buses=buses, message='Sorted in descending order by bus number')

    buses = repository.sort_buses(reverse=False)
    enumerate_buses(buses=buses, message='Sorted by increasing number of bus')

    point = 'point B'
    buses = repository.get_buses_by_point(point=point)
    enumerate_buses(buses=buses, message='Bus information with a stop {}'.format(point))


if __name__ == '__main__':
    main()
