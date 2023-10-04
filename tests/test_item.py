import pytest
from src.item import Item


test_item = Item('Test', 9000, 3)
test_item.pay_rate = 0.9


def test_calculate_total_price():
    assert test_item._price * test_item.quantity == test_item.calculate_total_price()


def test_apply_discount():
    native_price = test_item._price * test_item.pay_rate
    test_item.apply_discount()
    price = test_item._price
    assert native_price == price


def test_name():
    test_item.name = 'new_name'
    assert test_item.name == 'new_name'
    test_item.name = '123456789qqqqqqqq'
    assert test_item.name == '123456789q'


def test_string_to_number():
    assert 89 == test_item.string_to_number('89.9992')


def test_magic_str():
    test_item.name = 'Test'
    assert str(test_item) == test_item.name
    assert str(test_item) == 'Test'


def test_magic_repr():
    assert repr(test_item) == f'Item(name=Test, price=8100.0, quantity=3)'
