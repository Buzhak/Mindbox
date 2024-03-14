from abc import ABC, abstractclassmethod
import math

import constants
from utils import is_not_triangle, is_right_triangle


class Shape(ABC):

    def __init__(self):
        super().__init__()

    @abstractclassmethod
    def area(self):
        pass

    def __str__(self):
        return self._name


class Circle(Shape):
    '''
    Круг
    '''
    def __init__(self, r: int | float):
        self._name = 'Круг'
        self._radius = r

    def area(self) -> float | str:
        '''
        Вычисление площади круга через радиус r.
        '''
        return round(math.pi * self._radius ** 2, constants.ROUND)


class Triangle(Shape):
    '''
    Треугольник
    '''
    def __init__(self, a, b, c):
        if is_not_triangle(a, b, c):
            raise ValueError(constants.TRIANGLE_MESSAGE_3.format(a, b, c))
        if is_right_triangle(a, b, c):
            self._name = 'Прямоугольный треугольник'
        else:
            self._name = 'Треугольник'

        self._a = a
        self._b = b
        self._c = c

    def area(self) -> int | float | str:
        '''
        Вычисление площади треугольника по трем сторонам a, b, c.
        '''
        p = (self._a + self._b + self._c)/2
        area = (p * (p - self._a) * (p - self._b) * (p - self._c)) ** 0.5

        return round(area, constants.ROUND)
