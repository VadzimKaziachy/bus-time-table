import os
import pathlib
from typing import NoReturn

from abc import ABC, abstractmethod


class BaseData(ABC):
    """
    This class describes the rules that a developer must follow when adding a new module.
    """

    @abstractmethod
    def read(self, path: str):
        ...

    @abstractmethod
    def write(self, path: str, value) -> NoReturn:
        ...

    @staticmethod
    def get_file_path(path: str, file_name: str, format_file: str) -> str:
        """
        If there is a file in the path, then the path is returned, otherwise, the path from the parameters is collected.
        """
        if not os.path.isfile(path):
            path = os.path.join(path, '{file_name}{format_file}'.format(file_name=file_name, format_file=format_file))
        return path
