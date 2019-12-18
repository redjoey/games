from commands import Command

from models import House
from models import Player


class Help(Command):

    def __init__(
        self, name: str,
        player: Player, house: House
    ):
        super().__init__(name, player, house)
        self.commands = []
        self.keys_alpha = []
        self.map = {}

    def set_all_commands(self, commands: [Command]):
        keys = []
        cmd_idx = {}
        for cmd in commands:
            if not cmd.is_secret():
                keys.append(cmd.get_name())
            cmd_idx.update({
                cmd.get_name(): cmd
            })
        self.keys_alpha = sorted(keys)
        self.map = cmd_idx

    def do(self, text: str):
        for key in self.keys_alpha:
            print(f'{key} - {self.map[key].get_description()}')

    def get_description(self):
        return 'Dude, you\'re USING that command right now!'

    def get_aliases(self):
        return [
            'help me',
            'what can i do',
            '?',
            'h',
            'i don\'t know what to do',
            'what should i do'
            'commands',
            'list commands'
        ]
