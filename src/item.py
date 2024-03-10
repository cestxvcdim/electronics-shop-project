import csv
from src.my_error.instantiate_csv_error import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        if len(name) > 10:
            name = name[:10]
        self._name = name
        self._price = price
        self._quantity = quantity
        self.all.append(self)
        super().__init__()

    def __repr__(self) -> str:
        info = f"(name={self.name}, price={self._price}, quantity={self._quantity})"
        return self.__class__.__name__ + info

    def __str__(self) -> str:
        return self._name

    def __add__(self, other):
        if isinstance(other, Item):
            return self._quantity + other.quantity
        raise ValueError

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            new_name = new_name[:10]
        self._name = new_name

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def price(self) -> float:
        return self._price

    def calculate_total_price(self) -> float:
        return self._price * self._quantity

    def apply_discount(self) -> None:
        self._price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv') -> None:
        try:
            with open(path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    for row in reader:
                        cls(row['name'], row['price'], row['quantity'])
                except:
                    raise InstantiateCSVError(path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл {path}")
        else:
            print("Инициализация экземпляров класса прошла успешно!")

    @staticmethod
    def string_to_number(str_num: str) -> int:
        return int(float(str_num))
