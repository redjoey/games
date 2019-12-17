import sys
from termcolor import cprint

from models.chest import Chest
from models.house import House
from models.player import Player
from models.room import Room
from models.item import Item
from models.weapon import Weapon


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

    @staticmethod
    def get_next_command() -> str:
        cmd = input('> ')
        return cmd

    def interpret_command(self, cmd: str):
        if cmd in ('exit', 'bye', 'i\'m leaving', 'i\'m gonna exit', 'end game', 'quit', 'goodbye', 'leave', 'leave so soon', 'delete my progress', 'get outta here', 'skedaddle',
        'let me out', 'stop', 'end', 'avengers endgame', 'im scared of this place i wanna go home', 'i wanna go home', 'i want my mommy', 'i want my daddy', 'im out', 'goodbye',
        'this game is trash', 'i dont like this game', 'i dont like this', 'stop running run.py', f'go from {self.player.get_location()} to my house', 'walk into the strange portal that is on the wall that leads to my home',
        'when is this going to end', f'create a portal to my house in {self.player.get_location()}', 'i hate you', 'exit the game'):
            print(f'Leaving so soon, {self.player.get_name()}?? Ok, bye!')
            sys.exit()
        elif cmd.startswith('enter '):
            location = cmd.replace('enter ', '')
            
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
            print('loot - Grab all the stuff from a chest!')

            print('Secret commands not included here!')
        elif cmd.startswith('pickup '):
            item_str = cmd.replace('pickup ', '')
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
            item_str = cmd.replace('drop ', '')
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
                for room in exits:
                    print(room)
        elif cmd == 'attack':
            item_to_use = input('What item do you attack with? > ')
            if not self.player.in_inventory(item_to_use):
                print('You don\'t got dis item in yo inventory! You go '
                      'type in an item in yo inventory and '
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
            thing_str = cmd.replace('look at ', '')
            thing = None

            if self.player.in_inventory(thing_str):
                thing = self.player.get_item(thing_str)
                thing.look()
            elif self.player.get_location().contains(thing_str):
                self.player.get_location().describe(thing_str)
            elif thing_str == 'me':
                print(f'Here\'s looking at you, kid.')
            else:
                print(f'If only {thing_str} was here to look at...')
        elif cmd == 'warp':
            print('OMG YOU FOUND MY BRILLIANTLY WONDERFUL SECRET!!')
            warp_room = self.house.find_room_by_name('warp room')
            self.player.set_location(warp_room)
        elif cmd.startswith('loot '):
            item_str = cmd.replace('loot ', '')
            if self.player.get_location().can_player_pickup(item_str):
                chest = self.player.get_location().get_item(item_str)
                if not isinstance(chest, Chest):
                    print('Who are you to think this is a chest??')
                    return
                if chest.is_not_empty():
                    loot_items = chest.loot()
                    for item in loot_items:
                        self.player.pickup(item)
                    print(f'You looted items from {item_str}!')
                else:
                    print(f'{item_str} is empty - nothing to loot!')
            else:
                print('Can\'t loot. Try to loot a different loot.')
        elif cmd == 'smash a wall' or cmd == 'smash the wall':
            place_that_the_hole_leads_to = self.house.find_room_by_name('outside')
            room_that_lets_you_into_the_sword_room = self.house.find_room_by_name('entry room')
            room_with_a_wall_that_can_be_smashed = self.house.find_room_by_name('sword room')
            if not self.player.get_location() == room_with_a_wall_that_can_be_smashed:
                print('Smash attempt failed.')
                return
            else:
                print('The wall has been smashed! You walk through your hole in the wall and you are outside.')
                print('')
                room_with_a_wall_that_can_be_smashed.set_exits([room_that_lets_you_into_the_sword_room, place_that_the_hole_leads_to])
        elif cmd in('stab me', 'stab myself'):
            cprint('Do you really want to stab yourself?', 'red')
            are_you_sure = input('> ')
            if are_you_sure in('yes', 'y'):
                cprint('Okay...', 'red')
                self.player.take_damage(self.player.get_hp())
            elif are_you_sure in('no', 'n'):
                cprint('I thought so. Continue playing.', 'green')
                print('')
                return
            else:
                print('That\'s not an option. Continue playing.')
                print('')
                return
            
        else:
            print('Sorry, I don\'t recognize that command.')
