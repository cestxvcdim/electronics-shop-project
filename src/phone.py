from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, sim_cards) -> None:
        super().__init__(name, price, quantity)
        if sim_cards < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._sim_cards = sim_cards

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        info = f"('{self.name}', {self._price}, {self._quantity}, {self._sim_cards})"
        return self.__class__.__name__ + info

    @property
    def sim_cards(self):
        return self._sim_cards

    @sim_cards.setter
    def sim_cards(self, other):
        if isinstance(other, int) and other > 0:
            self._sim_cards = other
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
