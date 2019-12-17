from .item import Item


class Weapon(Item):
    def __init__(
        self,
        name: str,
        description: str,
        damage: int
    ):
        super().__init__(name, description)
        self.damage = damage

    def get_damage(self):
        return self.damage
