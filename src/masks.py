from typing import Union


def get_mask_card_number(card_number: Union[int]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    mask = f"{str(card_number)[:6]}******{str(card_number)[-4:]}"
    return " ".join([mask[i : i + 4] for i in range(0, len(mask), 4)])


def get_mask_account(account: Union[int]) -> Union[str]:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{str(account)[-4:]}"
