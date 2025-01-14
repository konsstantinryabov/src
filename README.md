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

## Установка 
- Скопировать - [SSH](git@github.com:konsstantinryabov/src.git)
- В терминале поддерживающем команды гит введите 
```
git clone git@github.com:konsstantinryabov/src.git
```

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
### Модуль ***generators.py***:
***filter_by_currency()*** принимает на вход список транзаций и возвращает
итератор транзации с заднным 'code' равный 'currency_code'
```
# Входные данные 
[
{   "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
    },
{
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD" }},
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
    },
{
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
    }, 
    ....]
    
    
# Выходные данные
[
{   "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
    },
{
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD" }},
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
    }
]
```
***transaction_descriptions()*** принимает список транзаций и возвращает
описание каждой операции по очереди.
```
# Входные данные 
[
{   "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
    },
{
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD" }},
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
    },
{
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
    }, 
    ....]
    
    
# Выходные данные
"Перевод организации"
"Перевод со счета на счет"
"Перевод со счета на счет"
"Перевод с карты на карту"
"Перевод организации"
```
***card_number_generator()*** генерирует номер карт в заданном диапазоне
от "start" до "stop" в формате "XXXX XXXX XXXX XXXX".
```
# Входные данные
1, 5


# Выходные данные
"0000 0000 0000 0001",
"0000 0000 0000 0002",
"0000 0000 0000 0003",
"0000 0000 0000 0004",
"0000 0000 0000 0005"
 ```


## Тестирование через

### Параметризация
Это запуск одного и того же теста с различными входными данными. Это позволяет проверить работу тестируемой функции в разных условиях и с разными наборами данных.

Пример параметризации (обязательный декоратор ***@pytest.mark.parametrize***):

```
@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7000 7922 8960 6361", "7000 79** **** 6361"),
    ("5995 1248 3579 2541", "5995 12** **** 2541"),
    ("5995 1248 3579", "59** **** 3579"),
    ("15489653215487984461464", "Некорректный номер карты"),
    (5995124835792541, "5995 12** **** 2541"),
    ([], "0"),
    ({}, "0"),
    ("", "0"),])
```




Функция, которая проводит на истинность соответствия:
```
def test_get_mask_card_number(card_number: Union[int, str], expected: str) -> None:
    assert get_mask_card_number(card_number) == expected
```



Пример результат тестирования после выполнения команды ***pytest***:
```
============================= test session starts =============================
collecting ... collected 19 items

test_masks.py::test_card_review_fixture PASSED                           [  5%]
test_masks.py::test_get_mask_card_number[7000792289606361-7000 79** **** 6361] PASSED [ 10%]
test_masks.py::test_get_mask_card_number[7000 7922 8960 6361-7000 79** **** 6361] PASSED [ 15%]
test_masks.py::test_get_mask_card_number[5995 1248 3579 2541-5995 12** **** 2541] PASSED [ 21%]
test_masks.py::test_get_mask_card_number[5995 1248 3579-59** **** 3579] PASSED [ 26%]
test_masks.py::test_get_mask_card_number[15489653215487984461464-\u041d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b] PASSED [ 31%]
test_masks.py::test_get_mask_card_number[5995124835792541-5995 12** **** 2541] PASSED [ 36%]
test_masks.py::test_get_mask_card_number[card_number6-0] PASSED          [ 42%]
test_masks.py::test_get_mask_card_number[card_number7-0] PASSED          [ 47%]
test_masks.py::test_get_mask_card_number[-0] PASSED                      [ 52%]
test_masks.py::test_get_mask_account[73654108430135874305-**4305_0] PASSED [ 57%]
test_masks.py::test_get_mask_account[7365 4108 4301 3587 4305-**4305] PASSED [ 63%]
test_masks.py::test_get_mask_account[5995 1248 3579 2541 7896-**7896] PASSED [ 68%]
test_masks.py::test_get_mask_account[7365410843013587430-**7430] PASSED  [ 73%]
test_masks.py::test_get_mask_account[15489653215487984461401464-\u041d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0441\u0447\u0435\u0442\u0430] PASSED [ 78%]
test_masks.py::test_get_mask_account[73654108430135874305-**4305_1] PASSED [ 84%]
test_masks.py::test_get_mask_account[card_number6-0] PASSED              [ 89%]
test_masks.py::test_get_mask_account[card_number7-0] PASSED              [ 94%]
test_masks.py::test_get_mask_account[-0] PASSED                          [100%]

============================= 19 passed in 0.07s ==============================

Process finished with exit code 0
```

### Фикстуры
Это специальные функции, которые запускаются до или после тестов.

Пример фикстур:
```
@pytest.fixture
def card_name_review() -> str:
    return "Maestro"

@pytest.fixture
def card_number_review() -> str:
    return "1596837868705199"

```
Пример функций вызова фикстур:

```
def test_mask_account_card_fixture(card_name_review: str, card_number_review: str) -> None:
    assert mask_account_card(card_name_review, card_number_review) == "Maestro 1596 83** **** 5199"

```
Пример результата выполнения проверки:
```
============================= test session starts =============================
collecting ... collected 1 item

test_widget.py::test_mask_account_card_fixture PASSED                    [100%]

============================== 1 passed in 0.04s ==============================

Process finished with exit code 0
```


### Модуль ***test_generators.py***:
- **test_filter_by_currency_fixture()** с фикстурами
- **test_transaction_descriptions_fixture()** с фикстурами
- **test_card_number_generator()** с параметризацией


### Модуль ***test_masks.py***:
- **test_card_review_fixture()**  с фикстурами
- **test_get_mask_card_number()** с параметризацией
- **test_get_mask_account()** с параметризацией


### Модуль ***test_processing.py***:
- **test_filter_by_state_fixture()** с фикстурами
- **test_filter_by_state()** с параметризацией
- **test_sort_by_date()** с параметризацией


### Модуль ***test_widget.py***:
- **test_mask_account_card_fixture()** с фикстурами
- **test_get_date_fixture()** с фикстурами
- **test_mask_account_card()** с параметризацией
- **test_get_date()** с параметризацией

