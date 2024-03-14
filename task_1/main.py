import constants
from utils import (
    not_null_or_lower,
    is_not_numeric,
)


def calculator(*args: int | float) -> str:
    '''
    Функция выбирает фигуру по количетству передаваемых аргументов.
    Создаёт инстанс класса выбранной фигуры, вызывает метод класса
    который производит вычисления и возвращает ответ в виде строки.
    Если что-то идёт не так - возвращает текст ошибки.
    '''
    count_args = len(args)
    if any(is_not_numeric(i) for i in args):
        return constants.NOT_NUMERIC_MESSAGE
    if any(not_null_or_lower(i) for i in args):
        return constants.NOT_POSITIVE_OR_ZERO_MESSAGE
    if count_args in constants.SHAPE_CLASS:
        try:
            shape = constants.SHAPE_CLASS.get(count_args)(*args)
            return constants.RESPONSE_MESSAGE.format(shape, shape.area())
        except Exception as e:
            return e
    return constants.ARGUMENTS_NOT_EXIST


if __name__ == '__main__':
    print(calculator(10))
    print(calculator(5, 6, 7))
    print(calculator(3, 4, 5))
