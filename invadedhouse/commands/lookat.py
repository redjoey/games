from commands import Command


class LookAt(Command):

    def do(self, text: str):
        player = self.get_player()
        current_room = player.get_location()
        target = text

        if player.in_inventory(target):
            thing = player.get_item(target)
            thing.look()
        elif current_room.contains(target):
            current_room.describe(target)
        elif target == 'me':
            print(f'Here\'s looking at you, kid.')
        else:
            print(f'If only {target} was here to look at...')

    def get_description(self):
        return 'Gaze upon anything nearby.'

    def get_aliases(self):
        return [
            'examine',
            'watch',
            'inspect',
            'focus on'
        ]
