from typing import Union

from src.alphabet import alphabet
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card: str, number_card: Union[int, str]) -> str:
    """
    Функция возвращает содержащую тип и номер карты или счет
    получает: "Visa Platinum 7000792289606361"
    возвращает: "Visa Platinum 7000 79** **** 6361"
    """
    str_account_card = ""
    if not name_card and not number_card:
        str_account_card = "Введите тип и номер карты, счета."

    else:
        for letter in str(name_card).lower():
            if letter not in alphabet:
                return "Введите сначала тип карты, а после номер"

            else:
                if len(str(number_card)) < 20:
                    number_card_mask = str(get_mask_card_number(number_card))
                    str_account_card = str(name_card.title()) + " " + str(number_card_mask)

                else:
                    number_count_mask = str(get_mask_account(number_card))
                    str_account_card = str(name_card.title()) + " " + str(number_count_mask)

            return str_account_card
    return str_account_card


def get_date(time: Union[str]) -> Union[str]:
    """Функция возвращает преобразованную строку даты и времени в дату
    получает: "2024-03-11T02:26:18.671407"
    возвращает: "11.03.2024"
    """
    if time is None or not time:
        return "Введите дату."
    else:
        data_time = (time.split("T")[0]).split("-")
        return ".".join(list(reversed(data_time)))
