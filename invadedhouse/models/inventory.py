class Inventory:
    def __init__(self):
        self.stuff = []

    def add(self, item):
        self.stuff.append(item)

    def drop(self, item):
        self.stuff.remove(item)
        return item

    def has(self, item):
        return item in self.stuff

    def all(self):
        return self.stuff
