import unittest
from typing import NoReturn, List

from models.bus import Bus
from services.bus_service import BusService


class TestBusService(unittest.TestCase):

    def setUp(self) -> NoReturn:
        self.time = '15'
        self.route_number = '1'
        self.final_point = 'point B'
        self.starting_point = 'point A'

        self.service = BusService()

    def _add_bus(self) -> NoReturn:
        self.service.add_bus(
            time=self.time,
            route_number=self.route_number,
            final_point=self.final_point,
            starting_point=self.starting_point,
        )

    def test_add_bus(self) -> NoReturn:
        self._add_bus()

        self.assertIsNotNone(self.service.repository.buses)
        self.assertIsInstance(self.service.repository.buses, List)

    def test_service_repository_time(self) -> NoReturn:
        self._add_bus()

        self.assertEqual(self.service.repository.buses[0].time, self.time)

    def test_service_repository_route_number(self) -> NoReturn:
        self._add_bus()

        self.assertEqual(self.service.repository.buses[0].route_number, self.route_number)

    def test_service_repository_final_point(self) -> NoReturn:
        self._add_bus()

        self.assertEqual(self.service.repository.buses[0].final_point, self.final_point)

    def test_service_repository_starting_point(self) -> NoReturn:
        self._add_bus()

        self.assertEqual(self.service.repository.buses[0].starting_point, self.starting_point)

    def test_delete_bus(self) -> NoReturn:
        self._add_bus()
        self.service.delete_bus(index=0)

        self.assertListEqual(self.service.repository.buses, [])


if __name__ == '__main__':
    unittest.main()
