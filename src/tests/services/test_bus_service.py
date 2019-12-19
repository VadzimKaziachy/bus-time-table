import os
import unittest
from typing import NoReturn, List

from services.bus_service import BusService


class TestBusService(unittest.TestCase):

    def setUp(self) -> NoReturn:
        self.index = 0
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

    def _add_more_buses(self) -> NoReturn:
        self.service.add_bus(starting_point='point A', final_point='point D', route_number='1', time='15')
        self.service.add_bus(starting_point='point B', final_point='point C', route_number='2', time='16')
        self.service.add_bus(starting_point='point C', final_point='point B', route_number='3', time='17')
        self.service.add_bus(starting_point='point D', final_point='point A', route_number='4', time='18')

    def _test_service_repository_time(self, index: int, time: str) -> NoReturn:
        self.assertEqual(self.service.repository.buses[index].time, time)

    def _test_service_repository_route_number(self, index: int, route_number: str) -> NoReturn:
        self.assertEqual(self.service.repository.buses[index].route_number, route_number)

    def _test_service_repository_final_point(self, index: int, final_point: str) -> NoReturn:
        self.assertEqual(self.service.repository.buses[index].final_point, final_point)

    def _test_service_repository_starting_point(self, index: int, starting_point: str) -> NoReturn:
        self.assertEqual(self.service.repository.buses[index].starting_point, starting_point)

    def test_add_bus(self) -> NoReturn:
        self._add_bus()

        self.assertIsNotNone(self.service.repository.buses)
        self.assertIsInstance(self.service.repository.buses, List)

    def test_service_repository_time(self) -> NoReturn:
        self._add_bus()

        self._test_service_repository_time(index=self.index, time=self.time)

    def test_service_repository_route_number(self) -> NoReturn:
        self._add_bus()

        self._test_service_repository_route_number(index=self.index, route_number=self.route_number)

    def test_service_repository_final_point(self) -> NoReturn:
        self._add_bus()

        self._test_service_repository_final_point(index=self.index, final_point=self.final_point)

    def test_service_repository_starting_point(self) -> NoReturn:
        self._add_bus()

        self._test_service_repository_starting_point(index=self.index, starting_point=self.starting_point)

    def test_delete_bus(self) -> NoReturn:
        self._add_bus()
        self.service.delete_bus(index=self.index)

        self.assertListEqual(self.service.repository.buses, [])

    def test_edit_bus(self):
        time: str = '16'
        route_number: str = '2'
        final_point: str = 'point A'
        starting_point: str = 'point B'

        self._add_bus()
        self.service.edit_bus(
            index=self.index,
            time=time,
            route_number=route_number,
            final_point=final_point,
            starting_point=starting_point,
        )

        self._test_service_repository_time(index=self.index, time=time)
        self._test_service_repository_route_number(index=self.index, route_number=route_number)
        self._test_service_repository_final_point(index=self.index, final_point=final_point)
        self._test_service_repository_starting_point(index=self.index, starting_point=starting_point)

    def test_get_bus_by_number(self) -> NoReturn:
        self._add_bus()

        self.assertIsNotNone(self.service.get_bus_by_number(index=self.index))

        self._test_service_repository_time(index=self.index, time=self.time)
        self._test_service_repository_route_number(index=self.index, route_number=self.route_number)
        self._test_service_repository_final_point(index=self.index, final_point=self.final_point)
        self._test_service_repository_starting_point(index=self.index, starting_point=self.starting_point)

    def test_get_buses_by_point(self) -> NoReturn:
        self._add_bus()

        buses = self.service.get_buses_by_point(point=self.starting_point)

        self.assertIsNotNone(buses)
        self.assertIsInstance(buses, List)
        for index, bus in enumerate(buses):
            self._test_service_repository_starting_point(index=index, starting_point=self.starting_point)

    def test_sort_buses_reverse_true(self) -> NoReturn:
        self._add_more_buses()

        buses = self.service.sort_buses(reverse=True)

        self.assertIsNotNone(buses)
        self.assertIsInstance(buses, List)
        for index, bus in enumerate(buses):
            self.assertEqual(bus.route_number, str(len(buses) - index))

    def test_sort_buses_reverse_false(self) -> NoReturn:
        self._add_more_buses()

        buses = self.service.sort_buses(reverse=False)

        self.assertIsNotNone(buses)
        self.assertIsInstance(buses, List)
        for index, bus in enumerate(buses):
            self.assertEqual(bus.route_number, str(index + 1))

    def test_save_path_for_file_path(self) -> NoReturn:
        path = os.path.dirname(__file__)

        self.assertFalse(self.service.save_path_for_file(path=path))

    def test_save_path_for_file_txt(self) -> NoReturn:
        path = os.path.join(os.path.dirname(__file__), 'test.txt')

        self.assertFalse(self.service.save_path_for_file(path=path))

    def test_save_path_for_file_tsv(self) -> NoReturn:
        path = os.path.join(os.path.dirname(__file__), 'test.tsv')
        open(path, 'w').close()

        self.assertTrue(self.service.save_path_for_file(path=path))
        self.assertEqual(self.service.path, path)

        os.remove(path=path)


if __name__ == '__main__':
    unittest.main()
