from models import House
from models import Player


class Command:
    def __init__(
        self, name: str,
        player: Player, house: House
    ):
        self.name = name.lower()
        self.player = player
        self.house = house
        self.description = None
        self.aliases = [a.lower() for a in self.get_aliases()]

    def get_name(self):
        return self.name

    def get_description(self):
        return ''

    def get_aliases(self):
        return []

    def is_secret(self):
        return False

    def get_player(self):
        return self.player

    def get_house(self):
        return self.house

    def matches(self, cmd: str) -> bool:
        cmd = cmd.lower()
        return cmd == self.name or cmd in self.aliases

    def do(self, text: str):
        print(f'You found the un-implemented command \'{self.name}\'')
