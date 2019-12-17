import sys
from termcolor import cprint

from .armor import Armor
from .inventory import Inventory
from .item import Item
from .monster import Monster
from .room import Room


class Player:

    def __init__(self, hp):
        self.name = 'Joey'
        self.inventory = Inventory()
        self.location = None
        self.max_hp = hp
        self.hp = hp

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

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def is_dead(self):
        return self.get_hp() <= 0

    def is_alive(self):
        return self.get_hp() > 0

    def gets_attacked_by(self, monster: Monster):
        if monster.get_damage() == 0:
            return

        damage = min(monster.get_damage() - self.get_total_dp(), 0)
        if damage > 0:
            self.take_damage(damage)
            print(f'You took {damage} damage!')
        else:
            print(f'{monster.get_name()} tries to attack you, but they are no match for your armor.')

    def take_damage(self, damage):
        self.hp -= damage
        print(f'You took {damage} damage!')
        print('')
        if self.is_dead():
            cprint('You died!', 'red')
            sys.exit()
        else:
            print(f'You have {self.get_hp()} of {self.get_max_hp()} HP remaining.')

    def get_total_dp(self):
        dp = 0
        for item in self.all_items():
            if isinstance(item, Armor):
                dp += item.get_dp()
        return dp

