# Название проекта
Серверная часть виджета банковских операций.

Цель: разработать виджет, который будет иметь возможности отображать операции клиента.


## Технологии
- [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows)
- [Python](https://www.python.org/downloads/)
- flake8
- mypy
- black
- isort


## Использование
На данном этапе разработки виджет ***src*** виджет имеет несколько модулей и выполняет следующие операции: 

### Модуль ***masks.py***:
***get_mask_card_number()*** принимает на вход номер карты и возвращает ее маску

```
7000792289606361                    # входной аргумент
7000 79** **** 6361                 # выход функции
```
***get_mask_account*** принимает на вход номер счета и возвращает его маску.
```
73654108430135874305                # входной аргумент
**4305                              # выход функции
```
### Модуль ***widget.py***:

***mask_account_card()***, обрабатывает информацию о картах и о счетах.
```
# Пример для карты
Visa Platinum 7000792289606361      # входной аргумент
Visa Platinum 7000 79** **** 6361   # выход функции

# Пример для счета
Счет 73654108430135874305           # входной аргумент
Счет **4305                         
```
***get_date()***, преобразует один формат времени в другой.
```
"2024-03-11T02:26:18.671407"        # входной аргумент
"11.03.2024"                        # выход функции
```

### Модуль ***processing.py***:
***filter_by_state()*** принимает список словарей и значение для ключа 
state (по умолчанию 'EXECUTED'), возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению.
```
# Входные данные 
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
***sort_by_date()*** принимает список словарей и необязательный параметр,
задающий порядок сортировки (по умолчанию — убывание). Функция должна
возвращать новый список, отсортированный по дате (date)
```
# Входные данные 
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```


### Установка 
- Скопировать - [SSH](git@github.com:konsstantinryabov/src.git)
- В терминале поддерживающем команды гит введите 
```
git clone git@github.com:konsstantinryabov/src.git
```
- Приятного ознакомления)
