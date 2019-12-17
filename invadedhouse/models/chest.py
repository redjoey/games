from .item import Item


class Chest(Item):

    def __init__(
        self,
        name: str,
        description: str,
        capacity: int = 2
    ):
        super().__init__(name, description)
        self.capacity = capacity
        self.contents = []

    def place(self, item: Item):
        if len(self.contents) == self.capacity:
            print(f'{self.name} is already full.')
            return
        self.contents.append(item)

    def loot(self) -> [Item]:
        """
        Loots this chest (removes all items contained inside)

        :return: set of Items that were in this chest (empty set if nothing was inside)
        """
        items = self.contents
        self.contents = []
        return items

    def contains(self, thing):
        return thing in self.get_contents()

    def get_contents(self) -> [Item]:
        """
        Returns the contents of the chest WITHOUT removing them.

        :return: set of Items that are in this chest (empty set if nothing is inside)
        """
        return self.contents

    def is_empty(self):
        if not self.contents:
            return True
        else:
            return False

    def is_not_empty(self):
        if not self.contents:
            return False
        else:
            return True

    def look(self):
        print(self.get_name() + ':')
        print()
        print(self.get_description())
        print()

        print(f'Holds up to {self.capacity} items.')
        items_message = 'Currently inside: '
        if self.is_empty():
            items_message += 'Nothing.'
        else:
            items_message += ', '.join([item.get_name() for item in self.contents])
        print(items_message)
