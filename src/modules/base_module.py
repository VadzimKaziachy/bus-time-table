from typing import NoReturn

from abc import ABC, abstractmethod


class BaseData(ABC):

    """
    This class describes the rules that a developer must follow when adding a new module.
    """

    @abstractmethod
    def read(self):
        ...

    @abstractmethod
    def write(self, value) -> NoReturn:
        ...
