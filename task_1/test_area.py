import unittest
import math

import constants
from main import calculator
from shapes import Circle, Triangle
from utils import (
    is_not_numeric,
    is_not_triangle,
    is_right_triangle,
    not_null_or_lower
)


class TestCalcularot(unittest.TestCase):

    def test_calculator_input_value(self):
        self.assertEqual(
           calculator('a'),
           constants.NOT_NUMERIC_MESSAGE,
           'Функция должна принимать только числовые'
           'значения и выводить соответстующее сообщение'
        )
        self.assertEqual(
           calculator(0),
           constants.NOT_POSITIVE_OR_ZERO_MESSAGE,
           'Функция должна принимать только числовые больше 0'
           'значения и выводить соответстующее сообщение'
        )
        self.assertEqual(
           calculator(-1),
           constants.NOT_POSITIVE_OR_ZERO_MESSAGE,
           'Функция должна принимать только числовые больше 0'
           'значения и выводить соответстующее сообщение'
        )
        self.assertEqual(
           calculator(1, 3, 4, 5, 76, 7),
           constants.ARGUMENTS_NOT_EXIST,
           'Функция не будет работать с непредусмотренным количество'
           'аргументов и выведет соответстуюее сообщение'
        )

    def test_calculare_area_circle(self):
        circle = Circle(5)
        area = circle.area()
        result = constants.RESPONSE_MESSAGE.format(circle, area)

        self.assertEqual(
           calculator(5),
           result,
           'Калькулятор выдаёт неверный ответ'
        )

    def test_calculare_area_triangle(self):
        triangle = Triangle(6, 8, 9)
        area = triangle.area()
        result = constants.RESPONSE_MESSAGE.format(triangle, area)

        self.assertEqual(
           calculator(6, 8, 9),
           result,
           'Калькулятор выдаёт неверный ответ'
        )


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.radius = 10
        self.circle = Circle(self.radius)

    def test_area(self):
        result = round(math.pi * self.radius ** 2, constants.ROUND)
        self.assertEqual(
            self.circle.area(),
            result,
            'Неверные рассчеты'
        )


class TestTriangle(unittest.TestCase):

    def test_area(self):
        a, b, c = 9, 7, 6
        p = (a + b + c)/2
        result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        result = round(result, constants.ROUND)

        triangle = Triangle(a, b, c)
        self.assertEqual(
            triangle.area(),
            result,
            'Неверные рассчеты'
        )
        self.assertEqual(
            str(triangle),
            'Треугольник',
            'name должно быть треугольник'
        )

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)

        self.assertEqual(
            str(triangle),
            'Прямоугольный треугольник',
            'name должно быть треугольник'
        )


class TestValidators(unittest.TestCase):

    def test_is_not_numeric(self):
        self.assertTrue(
            is_not_numeric('fvfdsdg')
        )
        self.assertFalse(
            is_not_numeric(10)
        )

    def test_not_null(self):
        self.assertTrue(
            not_null_or_lower(0)
        )
        self.assertTrue(
            not_null_or_lower(-1)
        )
        self.assertFalse(
            not_null_or_lower(10)
        )

    def test_triangle(self):
        self.assertTrue(
            is_not_triangle(1, 1, 6)
        )
        self.assertFalse(
            is_not_triangle(2, 2, 2)
        )

    def test_right_triangle(self):
        self.assertTrue(
            is_right_triangle(3, 4, 5)
        )
        self.assertFalse(
            is_right_triangle(2, 2, 2)
        )


if __name__ == "__main__":
    unittest.main()
