from termcolor import cprint

from .item import Item
from .monster import Monster


class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.exits = []
        self.items = []
        self.monsters = []

    def __str__(self):
        return self.get_name()

    def get_description(self) -> str:
        return self.description

    def get_name(self) -> str:
        return self.name

    def enter(self, player):
        self.look(player)

    def look(self, player):
        cprint(self.get_name() + ':', 'cyan')
        print()
        print(self.get_description().format(player_name=player.get_name()))

        if self.get_items():
            print()
            item_message = 'Items in this room: '
            item_message += ', '.join(self.get_items_as_strings())
            print(item_message)

        if self.get_monsters():
            print()
            monster_message = 'Monsters in this room: '
            monster_message += ', '.join(self.get_monsters_as_strings())
            print(monster_message)

    def set_exits(self, exits):
        self.exits = exits

    def get_exits(self):
        return self.exits

    def can_player_travel_to(self, other_room):
        if other_room in self.get_exits():
            return True
        else:
            return False

    def set_items(self, items):
        self.items = items

    def get_items(self):
        return self.items

    def get_item(self, item_str):
        for item in self.get_items():
            if item.get_name().lower() == item_str.lower():
                return item

    def add_item(self, item):
        if item:
            self.get_items().append(item)

    def remove_item(self, item_str):
        for item in self.get_items():
            if item.get_name().lower() == item_str.lower():
                self.get_items().remove(item)
                return item
        return None

    def get_items_as_strings(self):
        str_list = []
        for item in self.get_items():
            str_list.append(item.get_name())
        return str_list

    def can_player_pickup(self, item_str):
        for item in self.get_items():
            if item.get_name().lower() == item_str.lower():
                return True
        return False

    def set_monsters(self, monsters):
        self.monsters = monsters

    def get_monsters(self):
        return self.monsters

    def get_monster(self, monster_str):
        for monster in self.get_monsters():
            if monster.get_name().lower() == monster_str.lower():
                return monster
        return None

    def remove_monster(self, monster):
        if self.contains(monster):
            self.get_monsters().remove(monster)

    def get_monsters_as_strings(self):
        str_list = []
        for monster in self.get_monsters():
            str_list.append(monster.get_name())
        return str_list

    def contains(self, thing):
        if isinstance(thing, Item):
            return thing in self.get_items()
        elif isinstance(thing, Monster):
            return thing in self.get_monsters()
        elif isinstance(thing, str):
            if thing.lower() in [s.lower() for s in self.get_items_as_strings()]:
                return True
            elif thing.lower() in [s.lower() for s in self.get_monsters_as_strings()]:
                return True
        return False

    def describe(self, thing_str):
        monster = self.get_monster(thing_str)
        if monster:
            print(monster.get_description())
        else:
            item = self.get_item(thing_str)
            if item:
                item.look()
