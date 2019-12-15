import unittest
from typing import NoReturn

from models.bus import Bus


class TestBus(unittest.TestCase):

    def setUp(self) -> NoReturn:
        self.time = '15'
        self.route_number = '1'
        self.final_point = 'point B'
        self.starting_point = 'point A'

        self.bus = Bus(
            time=self.time,
            route_number=self.route_number,
            final_point=self.final_point,
            starting_point=self.starting_point,
        )

    def test_field_time(self) -> NoReturn:
        self.assertEqual(self.time, self.bus.time)

    def test_field_route_number(self) -> NoReturn:
        self.assertEqual(self.route_number, self.bus.route_number)

    def test_field_final_point(self) -> NoReturn:
        self.assertEqual(self.final_point, self.bus.final_point)

    def test_field_starting_point(self) -> NoReturn:
        self.assertEqual(self.starting_point, self.bus.starting_point)

    def test_change_time(self) -> NoReturn:
        self.bus.time = '20'

        self.assertEqual('20', self.bus.time)

    def test_change_rout_number(self) -> NoReturn:
        self.bus.route_number = 2

        self.assertEqual(2, self.bus.route_number)

    def test_change_final_point(self) -> NoReturn:
        self.bus.final_point = 'point D'

        self.assertEqual('point D', self.bus.final_point)

    def test_change_starting_point(self) -> NoReturn:
        self.bus.starting_point = 'point C'

        self.assertEqual('point C', self.bus.starting_point)

    def test_get_fieldnames(self) -> NoReturn:
        self.assertListEqual(['route_number', 'starting_point', 'final_point', 'time'], self.bus.get_fieldnames())

    def test_dict_obj(self) -> NoReturn:
        self.assertDictEqual(
            {
                'time': self.time,
                'final_point': self.final_point,
                'route_number': self.route_number,
                'starting_point': self.starting_point
            },
            self.bus.dict_obj()
        )

    def test__str__(self) -> NoReturn:
        self.bus.time = self.time
        self.bus.final_point = self.final_point
        self.bus.route_number = self.route_number
        self.bus.starting_point = self.starting_point

        self.assertEqual(
            'Bus number {}, with start points `{}` and end points `{}`, travels = `{}` minutes.'.format(
                self.route_number,
                self.starting_point,
                self.final_point,
                self.time
            ),
            self.bus.__str__()
        )


if __name__ == '__main__':
    unittest.main()
