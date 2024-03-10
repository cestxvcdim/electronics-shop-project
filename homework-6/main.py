from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('../src/unknown.csv')
    # FileNotFoundError: Отсутствует файл ../src/unknown.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv('../src/my_error/harmed_item.csv')
    # InstantiateCSVError: Файл поврежден
