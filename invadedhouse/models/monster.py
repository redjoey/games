from .item import Item
from .weapon import Weapon


class Monster:
    def __init__(
        self,
        name: str,
        description: str,
        hp: int,
        damage: int = 0
    ):
        self.name = name
        self.description = description
        self.max_hp = hp
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return self.get_name()

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_damage(self):
        return self.damage

    def gets_attacked_with(self, item: Item):
        if not isinstance(item, Weapon):
            print(f'Your attempt to damage {self} with {item} is useless and comical.')
            return

        damage = item.get_damage()
        self.hp -= damage
        print(f'{self} took {damage} damage!')
        if self.is_dead():
            print(f'You killed {self}!')
        else:
            print(f'{self} has {self.get_hp()} of {self.get_max_hp()} HP remaining.')

    def is_dead(self):
        return self.get_hp() <= 0

    def is_alive(self):
        return self.get_hp() > 0
