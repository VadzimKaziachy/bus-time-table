from typing import List

from models.autobus import Autobus


class AutobusRepository:
    """
    This class is the repository class for the Autobus class.
    """

    def __init__(self):
        self.buses: List[Autobus] = list()
