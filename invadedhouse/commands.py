import sys

from player import Player
from rooms import House


class CommandInterpreter:
    """
    Processes commands input by player at command prompt.
    """

    def __init__(self, player: Player, house: House):
        self.player = player
        self.house = house

    def run(self):
        while True:
            cmd = self.get_next_command()
            self.interpret_command(cmd)

    def get_next_command(self) -> str:
        cmd = input('> ')
        return cmd

    def interpret_command(self, cmd: str):
        if cmd == 'exit':
            print(f'Leaving so soon, {self.player.get_name()}?? Ok, bye!')
            sys.exit()
        elif cmd.startswith('enter '):
            location = cmd.replace('enter ','')
            
            # Step 1:
            #   check to see if there is a room with the same name
            #   as location
            room = self.house.find_room_by_name(location.lower())
            if room is None:
                print(f'Hey silly. The room \'{location}\' does not exist.')
                print('Try typing in a REAL room!')
                return

            # Step 2:
            #   check if there is a door linked to location FROM the
            #   player's current location
            if self.player.get_location().can_player_travel_to(room):
                self.player.set_location(room)
            else:
                print(f'Hey silly. You can\'t go to {location} from here.')
        elif cmd == 'change my name':
            name = input('What\'s your name? > ')
            self.player.set_name(name)
            print(f'Oh, your name is {name}? I never knew!')
        elif cmd == 'help':
            print("  Available Commands")
            print("exit - Exits the game.")
            print("enter - Transports to a room.")
            print("help - Dude, you\'re USING that command right now!")
            print("change my name - Just in case \'Joey\' isn\'t your name.")
            print('pickup - Pickup any items that are lying around.')
            print('drop - Drop an item from your inventory.')
            print('show inventory - In case you forget what you\'re holding.')
            print('where to - If you\'re lost, this will tell you where to go.')
            print('look - Open your eyes and remember what\'s around.')
            print('look at - Gaze upon anything nearby.')
            print('attack - enter a battle with a nearby monster.')

            print('Secret commands not included here!')
        elif cmd.startswith('pickup '):
            item_str = cmd.replace('pickup ','')
            if self.player.get_location().can_player_pickup(item_str):
                item = self.player.get_location().remove_item(item_str)
                self.player.pickup(item)
                print(f'Picked up {item}!')
            else:
                print('You can\'t pick that up.')
        elif cmd == 'show inventory':
            print('Inventory:')
            if not self.player.all_items():
                print('Nothing')
            for item in self.player.all_items():
                print(item)
        elif cmd.startswith('drop '):
            item_str = cmd.replace('drop ','')
            if not self.player.in_inventory(item_str):
                print('How are you supposed to drop that if you don\'t HAVE it?')
            else:
                item = self.player.drop(item_str)
                self.player.get_location().add_item(item)
                print(f'You dropped your {item_str}!')
        elif cmd.lower() == 'where can i go?' or cmd == 'where to':
            exits = self.player.get_location().get_exits()
            if not exits:
                print('Nowhere! You\'re stuck now! Mwahahaha.')
            else:
                print('Possible paths:')
                for exit in exits:
                    print(exit)
        elif cmd == 'attack':
            item_to_use = input('What item do you attack with? > ')
            if not self.player.in_inventory(item_to_use):
                print('You don\'t got dis item in yo inventory! You go '\
                      'type in an item in yo inventory and '\
                      'dis attack command will do dat attack fo you!')
            else:
                item_obj = self.player.get_item(item_to_use)
                monster_to_attack = input('What monster do you want to attack? > ')
                if self.player.get_location().contains(monster_to_attack):
                    monster_obj = self.player.get_location().get_monster(monster_to_attack)
                    monster_obj.gets_attacked_with(item_obj)
                else:
                    print(f'Where do you see {monster_to_attack}??')
        elif cmd == 'look' or cmd == 'look around':
            self.player.get_location().look(self.player)
        elif cmd.startswith('look at '):
            thing = cmd.replace('look at ','')
            if self.player.get_location().contains(thing):
                self.player.get_location().describe(thing)
            elif self.player.in_inventory(thing):
                item_obj = self.player.get_item(thing)
                print(item_obj.get_description())
            elif thing == 'me':
                print(f'Here\'s looking at you, kid.')
            else:
                print(f'If only {thing} was here to look at...')
        elif cmd == 'warp':
            print('OMG YOU FOUND MY BRILLIANTLY WONDERFUL SECRET!!')
            warp_room = self.house.find_room_by_name('warp room')
            self.player.set_location(warp_room)
            
        else:
            print('Sorry, I don\'t recognize that command.')
