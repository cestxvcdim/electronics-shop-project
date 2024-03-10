class InstantiateCSVError(Exception):
    def __init__(self, path=None):
        if path:
            self.message = f'Файл {path} поврежден'
        else:
            self.message = 'Файл поврежден'
        super().__init__(self.message)
