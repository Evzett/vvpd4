"""Вариант 2"""
from datetime import datetime
from math import ceil
def deadline_score (pass_date: str, deadline_date: str) -> int:
    try:
        pass_date = datetime.strptime(pass_date, "%d.%m.%Y")
        deadline_date = datetime.strptime(deadline_date, "%d.%m.%Y")
        timedelta=deadline_date-pass_date
        if 0<timedelta.days<=7:
            return 5
        elif abs(timedelta.days)>=36:
            return 0
        else:
            number_of_week=ceil(abs(timedelta.days)/7)
            current_mark=5-number_of_week
            return current_mark
    except ValueError:
        return 'Введенные вами данные не соответствуют формату'

def late_list (grades: dict, deadline_date: str) -> list[str]:
    turned_in_late_students=[]
    for student,pass_date in grades.items():
        if datetime.strptime(pass_date, "%d.%m.%Y")>datetime.strptime(deadline_date, "%d.%m.%Y"):
            turned_in_late_students.append(student)
            return turned_in_late_students
print(late_list({"Иванов": "03.09.2020", "Петров":
"01.09.2020"},"02.09.2020"))

