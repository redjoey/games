from commands import Command


class Smash(Command):

    def do(self, text: str):
        player = self.get_player()
        house = self.get_house()
        current_room = player.get_location()

        place_that_the_hole_leads_to = house.find_room_by_name('outside')
        room_that_lets_you_into_the_sword_room = house.find_room_by_name('entry room')
        room_with_a_wall_that_can_be_smashed = house.find_room_by_name('sword room')
        if current_room != room_with_a_wall_that_can_be_smashed:
            print('Smash attempt failed.')
        else:
            print('The wall has been smashed! You walk through your hole in the wall and you are outside.')
            print()
            room_with_a_wall_that_can_be_smashed.set_exits(
                [room_that_lets_you_into_the_sword_room, place_that_the_hole_leads_to])

    def is_secret(self):
        return True

    def get_description(self):
        return 'Ssshhhh.....'

    def get_aliases(self):
        return [
            'smash a wall',
            'smash the wall'
        ]
