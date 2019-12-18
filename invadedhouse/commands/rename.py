from commands import Command


class Rename(Command):

    def do(self, text: str):
        player = self.get_player()
        house = self.get_house()
        current_room = player.get_location()

        if text is None:
            name = input('What\'s your name? > ')
            player.set_name(name)
        else:
            player.set_name(text)

        print(f'Oh, your name is {name}? I never knew!')

    def get_description(self):
        return 'Call yourself whatever you\'d like.'

    def get_aliases(self):
        return [
            'change my name to',
            'call me',
            'i call myself',
            'my name is',
            'i go by'
        ]
