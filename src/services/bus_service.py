import os
import logging.config
import pathlib

from typing import List, NoReturn, Dict

from repositories.bus_repository import AutobusRepository
from src.models.bus import Bus
from src.modules.tsv_module import TsvModule
from src.settings.base import BASE_DIR, DEFAULT_FILE_NAME
from src.settings.logging import LOGGING

logging.config.dictConfig(LOGGING)

logger = logging.getLogger('app')


class BusService:

    def __init__(self) -> NoReturn:
        self.path: str = BASE_DIR
        self.tsv_module = TsvModule()
        self.repository = AutobusRepository()

    def save_in_file(self) -> NoReturn:
        """
        The method is required to write data to a file.
        """
        buses = [bus.dict_obj() for bus in self.repository.buses]
        self.tsv_module.write(path=self.path, buses=buses)

    def save_path_for_file(self, path: str) -> bool:
        """
        If the file was not found then `False` otherwise the path to the file will be saved.
        """
        if self._is_check_file(path):
            self.path = path
            return True
        return False

    @staticmethod
    def is_correct_data(buses: List[Dict[str, str]]) -> bool:
        """
        This method is required to check the availability of the required fields.
        """
        return all(
            bus.get('time', None)
            and bus.get('final_point', None)
            and bus.get('route_number', None)
            and bus.get('starting_point', None)
            for bus in buses
        )

    def _is_check_file(self, path: str) -> bool:
        """
        The method is needed to check if the file exists and whether it is supported.
        """
        return os.path.isfile(path) and pathlib.Path(path).suffix == self.tsv_module.format_file

    def get_data(self) -> bool:
        """
        Receiving data from a file, moreover, a .tsv file corresponding to the module name.
        """
        if self._is_check_file(self.path):
            buses = self.tsv_module.read(path=self.path)
            if self.is_correct_data(buses):
                self.repository.buses = [
                    Bus(
                        time=bus.get('time'),
                        final_point=bus.get('final_point'),
                        route_number=bus.get('route_number'),
                        starting_point=bus.get('starting_point')
                    )
                    for bus in buses
                ]
                return True
        return False

    def sort_buses(self, reverse: bool) -> List[Bus]:
        """
        The method is intended for sorting buses by bus number.
        """
        return sorted(self.repository.buses, key=lambda bus: bus.route_number, reverse=reverse)

    def get_buses_by_point(self, point: str) -> List[Bus]:
        """
        The method is required to search for buses at the start or end stop.
        """
        return list(
            filter(lambda bus: bus.starting_point == point or bus.final_point == point, self.repository.buses)
        )

    def add_bus(self, bus: Bus) -> NoReturn:
        """
        Method is intended to add a bus to the repository.
        """
        self.repository.buses.append(bus)


def enumerate_buses(buses: List[Bus], message: str) -> NoReturn:
    """
    This function should not attract your attention, it is only needed for debugging the application.
    """
    logger.info('-----------')
    logger.info(message)
    for bus in buses:
        logger.info(bus)
    logger.info('-----------')


def main() -> NoReturn:
    service = BusService()

    service.add_bus(Bus(starting_point='point A', final_point='point B', route_number=1, time='15'))
    service.add_bus(Bus(starting_point='point B', final_point='point C', route_number=2, time='16'))
    service.add_bus(Bus(starting_point='point C', final_point='point D', route_number=3, time='17'))
    service.add_bus(Bus(starting_point='point B', final_point='point F', route_number=4, time='18'))

    service.save_in_file()

    service.path = os.path.join(BASE_DIR, '{file_name}.{format_file}'.format(file_name=DEFAULT_FILE_NAME,
                                                                             format_file='tsv'))

    service.get_data()

    buses = service.sort_buses(reverse=True)
    enumerate_buses(buses=buses, message='Sorted in descending order by bus number')

    buses = service.sort_buses(reverse=False)
    enumerate_buses(buses=buses, message='Sorted by increasing number of bus')

    point = 'point B'
    buses = service.get_buses_by_point(point=point)
    enumerate_buses(buses=buses, message='Bus information with a stop {}'.format(point))


if __name__ == '__main__':
    main()
