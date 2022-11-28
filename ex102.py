class Toy():
    def __init__(self):
        self._elems = []
    def add(self, new_elems):
        """new_elems is a list"""
        self._elems += new_elems
    def __len__(self):
        return len(self._elems)
    def __add__(self, other):
        new_toy = Toy()
        new_toy._elems = self._elems + other._elems
        return new_toy
    def __eq__(self, other):
        return self._elems == other._elems
    def __str__(self):
        return str(self._elems)
    def __hash__(self):
        return id(self)

