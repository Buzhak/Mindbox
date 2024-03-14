# Валидаторы

def not_null_or_lower(value: int | float) -> bool:
    '''
    Функция проверяет что полученное значения больше нуля
    '''
    return not value > 0


def is_not_numeric(value: any) -> bool:
    '''
    Функция проверяет что полученное значения числовые
    '''
    return not (isinstance(value, int) or isinstance(value, float))


def is_not_triangle(a: int | float, b: int | float, c: int | float) -> bool:
    '''
    Функция проверяет существует ли треугольник с такими сторонами
    '''
    values = [a + b <= c, a + c <= b, b + c <= a]
    return any(values)


def is_right_triangle(a: int | float, b: int | float, c: int | float) -> bool:
    values = sorted([a, b, c])
    return values[2] ** 2 == values[0] ** 2 + values[1] ** 2
