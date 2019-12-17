from commands import CommandInterpreter
from models.house import House
from models.player import Player

"""
             Welcome to...
   ____                       __         __  __ __                   
  /  _/___   _  __ ___  _ ___/ /___  ___/ / / // /___   __ __ ___  ___ 
 _/ / / _ \\| |/ // _  `// _  // -_)/ _  / / _  // _ \\/ // /(_-</  -_)
/___//_//_/ |___/ \\_,_/ \\_,_/ __/\\_,_/ /_//_/ ___/ \\_,_//___/\\__/ 
                                                                  

             Storyline by:  @redjoey
        Code Architecture:  @jsoconnell                               
"""


def main():
    player = Player()
    house = House()
    player.set_location(house.get_starting_location())
    game = CommandInterpreter(player, house)
    
    game.run()


main()
