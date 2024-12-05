from src import masks
from typing import Union
def mask_account_card(card_number: Union[str]) -> Union[str]:


    """
    Функция возвращает содержащую тип и номер карты или счет
    получает: "Visa Platinum 7000792289606361"
    возвращает: "Visa Platinum 7000 79** **** 6361"
    """

    data_card = card_number.split()
    if data_card[0] == "Счет":
        return f"{data_card[0]} {masks.get_mask_account(int(data_card[-1]))}"
    else:
        return f'{" ".join(data_card[:-1])} {masks.get_mask_card_number(int(data_card[-1]))}'


def get_date(time: Union[str]) -> Union[str]:



    """Функция возвращает преобразованную строку даты и времени в дату
    получает: "2024-03-11T02:26:18.671407"
    возвращает: "11.03.2024"
    """

    data_time = (time.split("T")[0]).split("-")
    return ".".join(list(reversed(data_time)))



