import pytest
from src.keyboard import Keyboard

keyboard = Keyboard('Test', 12_000, 19)


def test_name():
    assert str(keyboard) == 'Test'


def test_change_lang():
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'

