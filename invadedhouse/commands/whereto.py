from commands import Command


class WhereTo(Command):

    def do(self, text: str):
        player = self.get_player()
        current_room = player.get_location()

        exits = current_room.get_exits()
        if not exits:
            print('Nowhere! You\'re stuck now! Mwahahaha.')
        else:
            print('Possible paths:')
            for room in exits:
                print(room)

    def get_description(self):
        return 'If you\'re lost, this will tell you where to go.'

    def get_aliases(self):
        return [
            'where',
            'w',
            'exits',
            'where can i go',
            'where can i go?',
            'where can i go from here'
        ]
