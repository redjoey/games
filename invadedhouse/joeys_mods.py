from termcolor import cprint

from models.armor import Armor
from models.chest import Chest
from models.player import Player
from models.weapon import Weapon
from models.house import House
from models.monster import Monster
from models.player import Player
from models.item import Item
from models.room import Room

# Create pocket.

class Pocket(Item):

    def __init__(self, name: str,
        description: str,
    ):
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

# Create pocket armor.

class PocketArmor(Armor, Pocket):
    def __init__(self, name: str,
        description: str,
        dp: int
    ):
        self.stuff = []
        super().__init__(name, description)
        self.dp = dp

    def add(self, item):
        self.stuff.append(item)

    def drop(self, item):
        self.stuff.remove(item)
        return item

    def has(self, item):
        return item in self.stuff

    def all(self):
        return self.stuff
    
    def get_dp(self):
        return self.dp

    def look(self):
        super().look()
        print(f'Provides {self.get_dp()} points of protection.')