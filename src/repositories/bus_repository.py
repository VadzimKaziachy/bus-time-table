from typing import List

from models.Bus import Bus


class BusRepository:
    """
    This class is the repository class for the Autobus class.
    """

    def __init__(self):
        self.buses: List[Bus] = list()
