from typing import Generator


def filter_by_currency(transactions: list, currency_code: str) -> Generator:
    """
    Функция принимает на вход список транзаций и возвращает итератор
    транзации с заднным 'code' равный 'currency_code'
    """

    result = [filter(lambda x: x["operationAmount"]["currency"]["code"] == currency_code, transactions)]
    yield result


def transaction_descriptions(transactions: list) -> Generator:
    """
    Функция принимает список транзаций и возвращает описание
    каждой операции по очереди.
    """

    for operation in transactions:
        yield operation["description"]


def card_number_generator(start, stop):
    for i in range(start, stop):
        pass


# 3 - Использование
# for card_number in card_number_generator(1, 5):
#     print(card_number)
