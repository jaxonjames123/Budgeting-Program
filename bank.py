class Bank:

    def __init__(self, name, location):
        self._users = []
        self._name = name
        self._location = location

    def __str__(self):
        return f'Bank: {self._name}\nLocation: {self._location}'

    @property
    def users(self):
        return self._users

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location