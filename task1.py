import pytest

from functions import find_perimeter, find_area
from functions import calculate_mortgage_costs, calculate_savings
from functions import check_age


@pytest.mark.parametrize(
    'sq_side,expected', (
        [5, 20], 
        [7, 28], 
        [10, 40], 
        [3, 12], 
        [9, 36]
    )
)
def test_find_perimeter(sq_side: int, expected: int) -> None:
    """
    Переменные:
        sq_side (int): сторона квадрата, см
        expected (int): ожидаемый периметр квадрата, см
    """
    actual = find_perimeter(sq_side)
    assert actual == expected


@pytest.mark.parametrize(
    'sq_side,expected', (
        [5, 25], 
        [7, 49], 
        [10, 100], 
        [3, 9], 
        [9, 81]
    )
)
def test_find_area(sq_side: int, expected: int) -> None:
    """
    Переменные:
        sq_side (int): сторона квадрата, см
        expected (int): ожидаемая площадь квадрата, см^2
    """
    actual = find_area(sq_side)
    assert actual == expected


@pytest.mark.parametrize(
    'salary,percent_mortgage,expected',(
        [70000, 15, 126000], 
        [50000, 12, 72000], 
        [60000, 10, 72000],
        [85000, 13, 132600], 
        [78000, 19, 177840]
    )
)
def test_calculate_mortgage_costs(salary: int, percent_mortgage: int,
                                    expected: int) -> None:
    """
    Переменные:
        salary (int): месячная заработная плата, руб.
        percent_mortgage (int): месячные расходы на ипотеку, % от з/п
        expected (int): ожидаемые годовые затраты на ипотеку, руб. 
    """
    actual = calculate_mortgage_costs(salary, percent_mortgage)
    assert actual == expected


@pytest.mark.parametrize(
    'salary,percent_mortgage,percent_life,expected',(
        [70000, 15, 30, 38500], 
        [50000, 12, 35, 26500], 
        [60000, 10, 40, 30000], 
        [85000, 13, 37, 42500], 
        [78000, 19, 45, 28080]
    )
)
def test_calculate_savings(salary: int, percent_mortgage: int,
                        percent_life: int, expected: int) -> None:
    """
    Переменные:
        salary (int): месячная заработная плата, руб.
        percent_mortgage (int): месячные расходы на ипотеку, % от з/п
        percent_life (int): месячные расходы на жизнь, % от з/п
        expected (int): ожидаемые годовые накопления, руб. 
    """
    actual = calculate_savings(salary, percent_mortgage, percent_life) 
    assert actual == expected


@pytest.mark.parametrize(
    'age,expected',(
        [15, False],
        [12, False],
        [18, True],
        [13, False],
        [21, True]
    )
)
def test_check_age(age: int, expected: str) -> None:
    """
    Переменные:
        age (int): возраст пользователя в годах
        expected (bool): ожидаемый доступ пользователя на сайт
        (True - доступ разрешен, False - доступ запрещен)
    """
    actual = check_age(age)
    assert actual == expected


if __name__ == '__main__':
    pytest.main(["-v", "task1.py"])