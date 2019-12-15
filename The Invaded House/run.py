
from commands import CommandInterpreter
from player import Player
from rooms import House, Room


# Welcome to our awesome game:
#
#      THE ADVENTURE OF THE INVADED HOUSE!
#
# Storyline by:
#   Joey O'Connell
#
# Code architecture by:
#   Dad O'Connell
#
#
def main():
    player = Player()
    house = House()
    player.set_location(house.get_starting_location())
    game = CommandInterpreter(player, house)
    
    game.run()

def old_main():
    current_room = bed_room
    turn = 1
    while(turn <= 5):
        current_room.enter()
        cmd = input("> ")
        turn += 1
        print("Sorry, I don\'t understand that command yet.")

main()
