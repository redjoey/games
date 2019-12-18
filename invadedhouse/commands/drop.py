from commands import Command


class Drop(Command):

    def do(self, text: str):
        player = self.get_player()
        current_room = player.get_location()
        item_str = text

        if item_str in ('all', 'everything', 'all my belongings', 'everything i own'):
            count = 0
            for item in player.all_items():
                count += 1
                player.drop(item)
                current_room.add_item(item)
                dots = '.' * count
                print(f'Dropped {item.get_name()}{dots}')
        elif not player.in_inventory(item_str):
            print('How are you supposed to drop that if you don\'t HAVE it?')
        else:
            item = player.drop(item_str)
            current_room.add_item(item)
            print(f'You dropped your {item_str}!')

    def get_description(self):
        return 'Drop an item from your inventory.'

    def get_aliases(self):
        return [
            'get rid of',
            'throw',
            'place',
        ]
