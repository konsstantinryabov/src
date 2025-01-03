import pytest

# Фикстура test_masks
@pytest.fixture
def card_review() -> list[str | int]:
    return ["7000792289606361", "73654108430135874305", 7000792289606361, 73654108430135874305]