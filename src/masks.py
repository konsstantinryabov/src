from typing import Union


def get_mask_card_number(card_number: Union[int | str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    string_number_cart = str(card_number)
    mask_number_card = ""

    if card_number is None or not card_number:
        mask_number_card = "0"

    elif 12 <= len(str(card_number)) <= 20:
        string_num_card_mask = ""
        review_numbers = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
        for letter in string_number_cart:
            if letter in review_numbers:
                string_num_card_mask += letter
            else:
                continue

        if len(str(string_num_card_mask)) == 16:
            mask_number_card = (
                f"{string_num_card_mask[0:4]} {string_num_card_mask[4:6]}** **** {string_num_card_mask[-4:]}"
            )
        elif len(str(string_num_card_mask)) == 12:
            mask_number_card = f"{string_num_card_mask[0:2]}** **** {string_num_card_mask[-4:]}"

    else:
        mask_number_card = "Некорректный номер карты"

    return mask_number_card


def get_mask_account(card_number: Union[int, str]) -> Union[str]:
    """Функция принимает на вход номер счета и возвращает его маску"""

    string_number_cart = str(card_number)
    if card_number is None or not card_number:
        return "0"

    elif 16 <= len(str(card_number)) <= 24:
        string_number_cart_account = ""
        number_review = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
        for letter in string_number_cart:

            if letter not in number_review:
                continue

            else:
                string_number_cart_account += letter

        return f"**{string_number_cart_account[-4:]}"
    else:
        return "Некорректный номер счета"
