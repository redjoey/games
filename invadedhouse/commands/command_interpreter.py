from .attack import Attack
from .drop import Drop
from .enter import Enter
from .exit import Exit
from .help import Help
from .inventory import Inventory
from .look import Look
from .lookat import LookAt
from .loot import Loot
from .pickup import Pickup
from .rename import Rename
from .smash import Smash
from .startover import StartOver
from .warp import Warp
from .whereto import WhereTo

from models import House
from models import Player


class CommandInterpreter:
    """
    Processes commands input by player at command prompt.
    """
    def __init__(self, player: Player, house: House):
        self.player = player
        self.house = house

        help_command = Help('help', player, house)
        self.commands = [
            Attack('attack', player, house),
            Drop('drop', player, house),
            Enter('enter', player, house),
            Exit('exit', player, house),
            help_command,
            Inventory('inventory', player, house),
            Look('look', player, house),
            LookAt('look at', player, house),
            Loot('loot', player, house),
            Pickup('pickup', player, house),
            Rename('change my name', player, house),
            Smash('smash', player, house),
            StartOver('start over', player, house),
            Warp('warp', player, house),
            WhereTo('where to', player, house)
        ]
        help_command.set_all_commands(self.commands)

    def run(self):
        while True:
            cmd = self.get_next_command()
            self.interpret_command(cmd)

    @staticmethod
    def get_next_command() -> str:
        cmd = input('> ')
        return cmd

    def interpret_command(self, command_str: str):
        command_str = command_str.lower()
        words = command_str.split()
        matched_command_str = ''
        text = ''
        matched_command = None

        for word in words:
            if matched_command:
                if len(text) > 0:
                    text += ' '
                text += word
            else:
                if len(matched_command_str) > 0:
                    matched_command_str += ' '
                matched_command_str += word
                for cmd in self.commands:
                    if cmd.matches(matched_command_str):
                        matched_command = cmd

        if matched_command:
            matched_command.do(text)
        else:
            print('Sorry, I don\'t recognize that command.')
