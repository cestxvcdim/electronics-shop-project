from src.item import Item


class Mixin:
    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Item, Mixin):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        
    def __str__(self):
        return super().__str__()

    @property
    def language(self) -> str:
        return self._language
