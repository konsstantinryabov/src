from typing import Union

from src.masks import get_mask_account, get_mask_card_number

import pytest


def test_card_review(card_review: str) -> None:
    for card_number in card_review:
        if len(str(card_number)) == 16:
            assert get_mask_card_number(card_number) == "7000 79** **** 6361"
        else:
            assert get_mask_account(card_number) == "**4305"



@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7000 7922 8960 6361", "7000 79** **** 6361"),
    ("5995 1248 3579 2541", "5995 12** **** 2541"),
    ("5995 1248 3579", "59** **** 3579"),
    ("15489653215487984461464", "Введен некорректный номер карты"),
    (5995124835792541, "5995 12** **** 2541"),
    ([], "0"),
    ({}, "0"),
    ("", "0"),
])
def test_get_mask_card_number(card_number: Union[int, str], expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number, expected", [
    ("73654108430135874305", "**4305"),
    ("7365 4108 4301 3587 4305", "**4305"),
    ("5995 1248 3579 2541 7896", "**7896"),
    ("7365410843013587430", "**7430"),
    ("15489653215487984461464", "Введен некорректный номер карты"),
    (73654108430135874305, "**4305"),
    ([], "0"),
    ({}, "0"),
    ("", "0"),
])
def test_get_mask_account(card_number: Union[int, str], expected: str) -> None:
    assert get_mask_account(card_number) == expected



