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
