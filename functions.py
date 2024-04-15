# Задание «Площадь и периметр квадрата» 
# (занятие «Python. Знакомство с консолью»)

def find_perimeter(sq_side: int) -> int:
    """
    Переменные:
        sq_side (int): сторона квадрата, см
    Вывод:
        perimeter (int): периметр квадрата, см
    """
    perimeter = sq_side * 4
    return perimeter


def find_area(sq_side: int) -> int:
    """
    Переменные:
        sq_side (int): сторона квадрата, см
    Вывод:
        area (int): площадь квадрата, см^2
    """
    area = sq_side**2
    return area


# Задание «Приложение для финансового планирования»
# (занятие «Python. Знакомство с консолью»)

def calculate_mortgage_costs(salary: int, percent_mortgage: int) -> int:
    """
    Переменные:
        salary (int): месячная заработная плата, руб.
        percent_mortgage (int): месячные расходы на ипотеку, % от з/п
    Вывод:
        mortgage (int): годовые затраты на ипотеку, руб. 
    """
    mortgage = int(12 * salary * (percent_mortgage/100))
    return mortgage


def calculate_savings(salary: int, percent_mortgage: int,
                        percent_life: int) -> int:
    """
    Переменные:
        salary (int): месячная заработная плата, руб.
        percent_mortgage (int): месячные расходы на ипотеку, % от з/п
        percent_life (int): месячные расходы на жизнь, % от з/п
    Вывод:
        savings (int): годовые накопления, руб. 
    """
    savings = int(salary - salary * ((percent_mortgage + percent_life)/100))
    return savings


# Задание «Проверка возраста»
# (занятие «Условные конструкции. Операции сравнения»)

def check_age(age: int):
    """
    Переменные:
        age (int): возраст пользователя в годах
    Вывод:
        result (bool): доступ пользователя на сайт
        (True - доступ разрешен, False - доступ запрещен)
    """
    if age >= 18:
        return True
    else:
        return False