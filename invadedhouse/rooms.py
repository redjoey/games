class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.exits = []
        self.items = []
        self.monsters = []

    def __str__(self):
        return self.get_name()

    def get_description(self) -> str:
        return self.description

    def get_name(self) -> str:
        return self.name

    def enter(self, player):
        self.look(player)

    def look(self, player):
        print(self.get_name() + ':')
        print()
        print(self.get_description().format(player_name=player.get_name()))

        if self.get_items():
            print()
            item_message = 'Items in this room: '
            item_message += ', '.join(self.get_items_as_strings())
            print(item_message)

        if self.get_monsters():
            print()
            monster_message = 'Monsters in this room: '
            monster_message += ', '.join(self.get_monsters_as_strings())
            print(monster_message)

    def set_exits(self, exits):
        self.exits = exits

    def get_exits(self):
        return self.exits

    def can_player_travel_to(self, other_room):
        if other_room in self.get_exits():
            return True
        else:
            return False

    def set_items(self, items):
        self.items = items

    def get_items(self):
        return self.items

    def get_item(self, item_str):
        for item in self.get_items():
            if item.get_name().lower() == item_str.lower():
                return item

    def add_item(self, item):
        if item:
            self.get_items().append(item)

    def remove_item(self, item_str):
        for item in self.get_items():
            if item.get_name().lower() == item_str.lower():
                self.get_items().remove(item)
                return item
        return None
    
    def get_items_as_strings(self):
        str_list = []
        for item in self.get_items():
            str_list.append(item.get_name())
        return str_list

    def can_player_pickup(self, item_str):
        for item in self.get_items():
            if item.get_name().lower() == item_str.lower():
                return True
        return False

    def set_monsters(self, monsters):
        self.monsters = monsters

    def get_monsters(self):
        return self.monsters

    def get_monster(self, monster_str):
        for monster in self.get_monsters():
            if monster.get_name().lower() == monster_str.lower():
                return monster
        return None

    def remove_monster(self, monster):
        if self.contains(monster):
            self.get_monsters().remove(monster)

    def get_monsters_as_strings(self):
        str_list = []
        for monster in self.get_monsters():
            str_list.append(monster.get_name())
        return str_list

    def contains(self, thing):
        if isinstance(thing, Item):
            return thing in self.get_items()
        elif isinstance(thing, Monster):
            return thing in self.get_monsters()
        elif isinstance(thing, str):
            if thing.lower() in [s.lower() for s in self.get_items_as_strings()]:
                return True
            elif thing.lower() in [s.lower() for s in self.get_monsters_as_strings()]:
                return True
        return False

    def describe(self, thing_str):
        monster = self.get_monster(thing_str)
        if monster:
            print(monster.get_description())
        else:
            item = self.get_item(thing_str)
            if item:
                print(item.get_description())


class Item:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return self.get_name()

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name


class Weapon(Item):

    def __init__(
        self,
        name: str,
        description: str,
        damage: int
    ):
        super().__init__(name, description)
        self.damage = damage

    def get_damage(self):
        return self.damage


class Chest(Item):

    def __init__(
        self,
        name: str,
        description: str,
        capacity: int = 2
    ):
        super().__init__(name, description)
        self.capacity = capacity
        self.contents = []

    def place(self, item: Item):
        if len(self.contents) == self.capacity:
            print(f'{self.name} is already full.')
            return
        self.contents.append(item)

    def loot(self) -> [Item]:
        """
        Loots this chest (removes all items contained inside)

        :return: set of Items that were in this chest (empty set if nothing was inside)
        """
        items = self.contents
        self.contents = []
        return items

    def contains(self, thing):
        return thing in self.get_contents()

    def get_contents(self) -> [Item]:
        """
        Returns the contents of the chest WITHOUT removing them.

        :return: set of Items that are in this chest (empty set if nothing is inside)
        """
        return self.contents

    def is_empty(self):
        if not self.contents:
            return True
        else:
            return False

    def is_not_empty(self):
        if not self.contents:
            return False
        else:
            return True

    def look(self):
        print(self.get_name() + ':')
        print()
        print(self.get_description())
        print()

        print(f'Holds up to {self.capacity} items.')
        items_message = 'Currently inside: '
        if self.is_empty():
            items_message += 'Nothing.'
        else:
            items_message += ', '.join([item.get_name() for item in self.contents])
        print(items_message)


class Monster:

    def __init__(
        self,
        name: str,
        description: str,
        hp: int
    ):
        self.name = name
        self.description = description
        self.max_hp = hp
        self.hp = hp

    def __str__(self):
        return self.get_name()

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def gets_attacked_with(self, item: Item):
        if not isinstance(item, Weapon):
            print(f'Your attempt to damage {self} with {item} is useless and comical.')
            return

        damage = item.get_damage()
        self.hp -= damage
        print(f'{self} took {damage} damage!')
        if self.is_dead():
            print(f'You killed {self}!')
        else:
            print(f'{self} has {self.get_hp()} of {self.get_max_hp()} HP remaining.')

    def is_dead(self):
        return self.get_hp() <= 0

    def is_alive(self):
        return self.get_hp() > 0
        

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
        bedroom.set_items([sword, key, apple])

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
