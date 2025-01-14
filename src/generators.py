from typing import Generator, Iterator


def filter_by_currency(transactions: list, currency_code: str) -> Iterator[dict]:
    """
    Функция принимает на вход список транзаций и возвращает итератор
    транзации с заднным 'code' равный 'currency_code'
    """
    result = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency_code, transactions))
    yield result

def transaction_descriptions(transactions: list) -> Generator:
    """
    Функция принимает список транзаций и возвращает описание
    каждой операции по очереди.
    """

    for operation in transactions:
        yield operation["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """
    Функция генерирует номер карт в заданном диапазоне от "start" до "stop"
    в формате "XXXX XXXX XXXX XXXX".
    """

    if type(start) is int and type(stop) is int and start < stop:
        card_number = "0" * 16
        for number in range(start, stop + 1):
            len_card_number = len(card_number) - len(str(number))
            result = card_number[:len_card_number] + str(number)
            yield f"{result[:4]} {result[4:8]} {result[8:12]} {result[12:]}"
    else:
        yield "Введены некорректные данные"
