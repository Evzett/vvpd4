
![pctr_cat](https://raw.githubusercontent.com/Evzett/vvpd4/task%231/photo_2023-12-21_23-15-54.jpg)
# VVPD4
Этот репозиторий был создан в образовательных целях в качестве практической работы по предмету "Введение в проффесиональную деятельность".

Здесь находится `маленький проектик` по вычислениям дедлайнов.

В модуле *practice.py* содержатся две функции:
* **Первая: deadline_score()** вычисляет какую оценку 
    получит студент, в зависимости от даты сдачи работы и даты дедлайна или обрабатывает исключение, если
    введенные данные не соответствуют шаблону: «DD.MM.YYYY».
    За каждую неделю задержки итоговая оценка уменьшается на 1 балл.
    Оценка за работу варьируется `от 5 до 0 баллов`, отрицательной
    она быть не может.
* **Вторая: late_list()** определяет сколько студентов из списка сдали работу
    позже назначенного срока.

В проекте также используются библиотеки [math](https://docs.python.org/3/library/math.html) и [datetime](https://docs.python.org/3/library/datetime.html)

**Использованная формула в  функции deadline_score()**
```
number_of_week = math.ceil(abs(timedelta.days)/7)
current_mark = 5-number_of_week
```
timedelta - разница в днях между датой сдачи работы и датой дедлайна.

 В модулях *started_window.py*, *scoring_window.py* и *students_in_late_window.py* реализован небольшой графический интерфейс с помощью библиотеки [PyQt5](https://pypi.org/project/PyQt5/).


### Как загрузить библиотеку
```
pip install PyQt5
```
### Пример кода
```
>>>deadline_score('11.12.2023','12.12.2023')
5
>>>late_list({'Иванов': '13.12.2023', 'Петров': '11.12.2023'}, '12.12.2023')
['Иванов']
```

### Запуск проекта
```
python main.py
```
### Как делалась эта работа:
- [X] Использование костылей
- [X] Отбор мемов для файла(неудачный)

![сложный выбор](https://raw.githubusercontent.com/Evzett/vvpd4/task%231/import%20numpy.jpg)
>>>>>>> 25e9b0a984c3880eb224ad467ec8726ac265d788
