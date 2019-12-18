from termcolor import cprint

from commands import Command


class StartOver(Command):

    def do(self, text: str):
        player = self.get_player()

        cprint('Do you really want to give up? You\'re doing so good!', 'red')
        are_you_sure = input('> ')
        if are_you_sure in ('yes', 'y'):
            cprint('Okay, starting over.', 'red')
            player.take_damage(player.get_hp())
        elif are_you_sure in ('no', 'n'):
            cprint('Okay, great! I thought you wouldn\'t want to start over!', 'green')
            print()
        else:
            print('That\'s not an option. Continue playing.')
            print()

    def is_secret(self):
        return True

    def get_description(self):
        return 'Ssshhh....'

    def get_aliases(self):
        return [
            'give up'
        ]
