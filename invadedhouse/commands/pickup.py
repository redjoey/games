from commands import Command


class Pickup(Command):

    def do(self, text: str):
        player = self.get_player()
        current_room = player.get_location()
        item_str = text

        if current_room.can_player_pickup(item_str):
            item = current_room.remove_item(item_str)
            player.pickup(item)
            print(f'Picked up {item}!')
        else:
            print('You can\'t pick that up.')

    def get_description(self):
        return 'Pickup any items that are lying around.'

    def get_aliases(self):
        return [
            'pick up',
            'take',
            'grab',
            'get',
            'acquire',
            'steal',
            'give me'
        ]
