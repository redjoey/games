from commands import Command


class Look(Command):

    def do(self, text: str):
        player = self.get_player()
        current_room = player.get_location()

        current_room.look(player)

    def get_description(self):
        return 'Open your eyes and remember what\'s around.'

    def get_aliases(self):
        return [
            'look around',
            'what\'s here',
            'l'
        ]
