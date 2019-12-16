from .chest import Chest
from .item import Item
from .monster import Monster
from .room import Room
from .weapon import Weapon


class House:
    def __init__(self):
        self.starting_location = None
        self.room_directory = None
        self.build_house()

    def build_house(self):
        # set up the rooms
        bedroom = Room(
            'Bedroom',
            'You\'re in a room with a chest, and a door.'
        )
        entry = Room(
            'Entry Room',
            'You\'re in a very empty room, except for a set of stairs '
            'and a door. Behind the door you hear monstrous screams.'
        )
        monster_room = Room(
            'Monster Room',
            'You are in a narrow room containing a screaming, hungry '
            'monster.'
        )
        sword_room = Room(
            'Sword Room',
            'You\'re in a small room obviously containing a sword.'
        )
        teleporter_room = Room(
            'Teleporter Room',
            'All there is here is a teleporter going to who knows where.'
        )
        pumpkin_room = Room(
            'Pumpkin Room',
            'You are in a very large room containing a basket of pumpkins.'
            'You could probably make pie...'
        )
        boss_room = Room(
            'Boss Room',
            'THERE\'S A GIANT SCREAMING MONSTER IN HERE OH MY GOD!!!'
        )
        laser_room = Room(
            'Laser Room',
            'You are in a narrow room, there\'s a teleporter, but also a laser '
            'gun. Maybe you should pick that up first...'
        )
        finale_room = Room(
            'FINALE ROOM',
            'This is it. You are in a narrow room, containing a fat golden monster \
            that probably doesn\'t even know what the word \'attack\' means, \
            and behind it a special wall that a laser gun could break through. \
            You can do this, {player_name}. Just kill that monster and \
            break through that wall and you\'re out of this Invaded House... \
            Let\'s go.'
        )
        end_room = Room(
            'The End',
            'You did it, {player_name}! You escaped the '
            'Invaded House! Thanks for playing, look out for our next project: '
            'Invaded House Maker!'
        )
        warp_room = Room(
            'Warp Room',
            'Nobody drew this on the map... Well, you can warp somewhere. Didn\'t see this on'
            ' the map. Just sayin\'.'
        )

        # set up the items
        sword = Weapon(
            'Sword',
            'What a sharp blade! This does 5 damage. If you find a '
            'better sword, it will do more.',
            5
        )
        pumpkin = Item(
            'Pumpkin',
            'Let\'s make pie.'
        )
        super_sword = Weapon(
            'Special Sword',
            'This is a more advanced version of a sword which does more damage.',
            20
        )
        key = Item(
            'Key',
            'Unlocks a door.'
        )
        apple = Item(
            'Apple',
            'This is an apple, which will restore 5 HP'
        )
        laser_gun = Weapon(
            'Laser Gun',
            'This laser gun might be able to break through a special wall...',
            40
        )
        boss_key = Item(
            'Boss Key',
            'This key will unlock the door to get past the Boss Room.'
        )
        gold_sword = Weapon(
            'Gold Sword',
            'Wow... Shiny! This beautiful sword can kill a fat, golden monster.',
            50
        )
        trash_can = Chest(
            'Trash Can',
            'The most disgusting thing to grab items out of.',
            3
        )
        trash_can.place(sword)
        trash_can.place(apple)
        trash_can.place(key)

        # set up the monsters
        screaming_monster = Monster(
            'Screaming Monster',
            'You get the sense that this monster is mad and hungry.',
            10
        )
        boss_monster = Monster(
            'Boss',
            'This dude is big, and also hungry like Screaming Monster. Hopefully you\'ve met him.',
            100
        )
        gold_monster = Monster(
            'Gold Monster',
            'Fat, strong, pretty, and only killed with a Gold Sword.',
            1000
        )

        # set up all the exits and items and monsters for each room
        bedroom.set_exits([entry])
        bedroom.set_items([trash_can])

        entry.set_exits([bedroom, monster_room, sword_room])
        sword_room.set_exits([entry])
        sword_room.set_items([super_sword])
        monster_room.set_exits([entry, teleporter_room])
        monster_room.set_monsters([screaming_monster])
        teleporter_room.set_exits([monster_room, pumpkin_room])
        pumpkin_room.set_exits([teleporter_room, boss_room])
        pumpkin_room.set_items([pumpkin, pumpkin, pumpkin])
        boss_room.set_exits([pumpkin_room, laser_room])
        boss_room.set_items([boss_key, gold_sword])
        boss_room.set_monsters([boss_monster])
        laser_room.set_exits([boss_room, finale_room])
        laser_room.set_items([laser_gun])
        finale_room.set_exits([laser_room, end_room])
        finale_room.set_monsters([gold_monster])
        warp_room.set_exits([boss_room, bedroom, laser_room])

        self.starting_location = bedroom

        # the room directory has all of the rooms listed inside.
        self.room_directory = {
            'bedroom': bedroom,
            'entry room': entry,
            'monster room': monster_room,
            'sword room': sword_room,
            'teleporter room': teleporter_room,
            'pumpkin room': pumpkin_room,
            'boss room': boss_room,
            'laser room': laser_room,
            'finale room': finale_room,
            'end room': end_room,
            'warp room': warp_room
        }

        # this is a faster way to do what's written above:
        # self.setup_directory(bedroom, entry, monster_room)

    # Dad's fancy way of setting up the directory
    def setup_directory(self, *args):
        for room in args:
            self.room_directory.update({
                room.name.lower(): room
            })

    def get_starting_location(self):
        return self.starting_location

    def find_room_by_name(self, name: str):
        room = self.room_directory.get(name)
        return room
