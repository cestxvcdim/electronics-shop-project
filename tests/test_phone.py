import pytest
from src.phone import Phone

phone = Phone("Test", 90_000, 8, 2)


def test_magic_str():
    assert str(phone) == "Test"


def test_magic_repr():
    assert repr(phone) == "Phone('Test', 90000, 8, 2)"


def test_sim_cards():
    assert phone.sim_cards == 2
    phone.sim_cards = 1
    assert phone.sim_cards == 1
