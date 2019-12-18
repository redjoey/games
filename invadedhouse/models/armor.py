from .item import Item


class Armor(Item):
    def __init__(
        self,
        name: str,
        description: str,
        dp: int
    ):
        super().__init__(name, description)
        self.dp = dp

    def get_dp(self):
        return self.dp

    def look(self):
        super().look()
        print(f'Provides {self.get_dp()} points of protection.')
