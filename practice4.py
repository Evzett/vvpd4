"""Вариант 2"""
from datetime import datetime
from math import ceil


def deadline_score(pass_date: str, deadline_date: str) -> int:
    """В зависимости от переданных данных вычисляет какую оценку
    получит студент или обрабатывает исключение, если
    введенные данные не соответствуют шаблону: «DD.MM.YYYY»
    За каждую неделю задержки итоговая оценка уменьшается на 1 балл.
    Оценка за работу варьируется от 5 до 0 баллов, отрицательной
    она быть не может (пропустил три месяца – всё равно студент получает
    0 баллов).

    :param pass_date:str, дата в формате «DD.MM.YYYY»,
    когда студент сдал свою работу.
    :param deadline_date:str, дата дедлайна работы
    в формате «DD.MM.YYYY»
    :return:int, оценка за работу (от 5 до 0)
    или строка с сообщением об ошибке.
     Example:
        deadline_score('11.12.2023','12.12.2023')
        5

        deadline_score('13.12.2023','12.12.2023')
        4

        deadline_score('01.05.2024','12.12.2023')
        0

        deadline_score('12/12/2023','12/12/2023')
        'Введенные вами данные не соответствуют формату'

    """
    try:
        pass_date = datetime.strptime(pass_date, "%d.%m.%Y")
        deadline_date = datetime.strptime(deadline_date, "%d.%m.%Y")
        timedelta = deadline_date-pass_date
        if timedelta.days >= 0:
            return 5
        elif abs(timedelta.days>=36) and timedelta.days<0:
            return 0
        else:
            number_of_week = ceil(abs(timedelta.days)/7)
            current_mark = 5-number_of_week
            return current_mark
    except ValueError:
        return 'Введенные вами данные\n не соответствуют формату'

def late_list (grades: dict, deadline_date: str) -> list[str]:
    """Определяет сколько студентов из списка сдали работу
    позже назначенного срока.
    Если таких студентов нет, возвращает строку "тут нет студентов".


    :param grades: dict, словарь, где ключи - фамилии студентов,
    а значения - дата сдачи работы. Например: {"Иванов": "12.12.2023"}
    :param deadline_date: deadline_date: str, дата дедлайна работы в формате
    «DD.MM.YYYY»
    :return: list[str], список строк с фамилиями студентов или строка
    "тут нет студентов", если студентов, сдавших работу после дедлайна нет.
    Example:
        late_list({'Иванов': '13.12.2023', 'Петров': '11.12.2023'}, '12.12.2023')

        ['Иванов']

    """
    turned_in_late_students=[]
    for student,pass_date in grades.items():
        if datetime.strptime(pass_date, "%d.%m.%Y")>datetime.strptime(deadline_date, "%d.%m.%Y"):
            turned_in_late_students.append(student)
    if turned_in_late_students:
        return sorted(turned_in_late_students)
    else:
        return "тут нет студентов"
