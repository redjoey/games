from commands import Command

from models import Chest


class Loot(Command):

    def do(self, text: str):
        player = self.get_player()
        current_room = player.get_location()
        target = text

        if current_room.can_player_pickup(target):
            chest = current_room.get_item(target)
        elif player.in_inventory(target):
            chest = player.get_item(target)
        else:
            print('Can\'t loot. Try to loot a different loot.')
            return

        if not isinstance(chest, Chest):
            print('Who are you to think this is a chest??')
            return
        if chest.is_not_empty():
            loot_items = chest.loot()
            for item in loot_items:
                player.pickup(item)
            print(f'You looted items from {target}!')
            if player.in_inventory(target):
                player.drop(chest)
                print(f'You dropped {target} because who needs that anymore?!')
        else:
            print(f'{target} is empty - nothing to loot!')

    def get_description(self):
        return 'Grab all the stuff from a chest!'

    def get_aliases(self):
        return [
            'plunder'
        ]
