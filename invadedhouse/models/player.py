from .inventory import Inventory
from .item import Item
from .room import Room


class Player:

    def __init__(self):
        self.name = 'Joey'
        self.inventory = Inventory()
        self.location = None

    def set_name(self, name: str):
        self.name = name

    def set_location(self, location: Room):
        self.location = location
        self.location.enter(self)

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def pickup(self, item):
        self.inventory.add(item)

    def drop(self, item):
        if isinstance(item, Item):
            return self.inventory.drop(item)
        elif isinstance(item, str):
            for myitem in self.all_items():
                if myitem.get_name().lower() == item.lower():
                    return self.inventory.drop(myitem)
        return None

    def all_items(self):
        return self.inventory.all()

    def get_item(self, item_str: str):
        for item in self.all_items():
            if item.get_name().lower() == item_str.lower():
                return item
        return None

    def in_inventory(self, item):
        if isinstance(item, Item):
            return self.inventory.has(item)
        elif isinstance(item, str):
            for myitem in self.all_items():
                if myitem.get_name().lower() == item.lower():
                    return True
        return False
