import logging.config
from typing import Dict, NoReturn, List

from src.settings.logging import LOGGING

logging.config.dictConfig(LOGGING)

logger = logging.getLogger('app')


class Bus:

    def __init__(self, starting_point: str, final_point: str, route_number: str, time: str) -> NoReturn:
        self.time = time
        self.final_point = final_point
        self.route_number = route_number
        self.starting_point = starting_point

    def __str__(self) -> str:
        return 'Bus number {}, with start points `{}` and end points `{}`, travels = `{}` minutes.'.format(
            self.route_number,
            self.starting_point,
            self.final_point,
            self.time
        )

    def dict_obj(self) -> Dict:
        """
        Method converts an object to `dict`
        :return: Dict
        """
        return {
            'time': self.time,
            'final_point': self.final_point,
            'route_number': self.route_number,
            'starting_point': self.starting_point
        }

    @staticmethod
    def get_fieldnames() -> List[str]:
        return ['route_number', 'starting_point', 'final_point', 'time']


if __name__ == '__main__':
    bus = Bus(starting_point='point A', final_point='point B', route_number='1', time='15')

    logger.info(bus)
    logger.info(bus.route_number)
    logger.info(bus.starting_point)
    logger.info(bus.final_point)
    logger.info(bus.time)

    bus.route_number = 2
    logger.info(bus.route_number)

    bus.starting_point = 'point C'
    logger.info(bus.starting_point)

    bus.final_point = 'point D'
    logger.info(bus.final_point)

    bus.time = '20'
    logger.info(bus.time)

    logger.info(bus)
