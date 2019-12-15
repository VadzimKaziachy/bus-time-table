from typing import List

from models.bus import Bus


class BusRepository:
    """
    This class is the repository class for the Autobus class.
    """

    def __init__(self):
        self.buses: List[Bus] = list()
