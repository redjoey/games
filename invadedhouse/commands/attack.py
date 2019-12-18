from commands import Command


class Attack(Command):

    def do(self, text: str):
        player = self.get_player()
        current_room = player.get_location()
        monster_to_attack = text

        item_to_use = input('What item do you attack with? > ')
        if not player.in_inventory(item_to_use):
            print('You don\'t got dis item in yo inventory! You go '
                  'type in an item in yo inventory and '
                  'dis attack command will do dat attack fo you!')
        else:
            item_obj = player.get_item(item_to_use)
            if not monster_to_attack:
                monster_to_attack = input('What monster do you want to attack? > ')

            if current_room.contains(monster_to_attack):
                monster_obj = current_room.get_monster(monster_to_attack)
                monster_obj.gets_attacked_with(item_obj)
                if monster_obj.is_dead():
                    current_room.remove_monster(monster_obj)

                # TODO: Monsters fight back!!
            else:
                print(f'Where do you see {monster_to_attack}??')

    def get_description(self):
        return 'Enter a battle with a nearby monster.'

    def get_aliases(self):
        return [
            'fight',
            'maime',
            'injure',
            'battle',
            'kick',
            'punch',
            'hurt',
            'kill'
        ]
