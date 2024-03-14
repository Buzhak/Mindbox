from shapes import Circle, Triangle

NOT_NUMERIC_MESSAGE = 'Значение должно быть числовым.'
NOT_POSITIVE_OR_ZERO_MESSAGE = (
    'Значение не может быть нулевым или отрицательным.'
)
TRIANGLE_MESSAGE_3 = (
    'Треугольника с со сторонами a = {}, b = {}, c = {} - не существует.'
)
ARGUMENTS_NOT_EXIST = 'Отсутствует действие для такого количеста аргументов'
RESPONSE_MESSAGE = '{}. S = {}'

# До какого знака округляются числа
ROUND = 2
# Словарь с количеством аргусентов и клссом фигур
SHAPE_CLASS = {1: Circle, 3: Triangle}
