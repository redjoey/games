from commands import Command


class Enter(Command):

    def do(self, text: str):
        player = self.get_player()
        house = self.get_house()
        current_room = player.get_location()
        location = text

        # Step 1:
        #   check to see if there is a room with the same name
        #   as location
        room = house.find_room_by_name(location)
        if room is None:
            print(f'Hey silly. The room \'{location}\' does not exist.')
            print('Try typing in a REAL room!')
            return

        # Step 2:
        #   check if there is a door linked to location FROM the
        #   player's current location
        if current_room.can_player_travel_to(room):
            player.set_location(room)
        else:
            print(f'Hey silly. You can\'t go to {location} from here.')

    def get_description(self):
        return 'Travel to the room specified.'

    def get_aliases(self):
        return [
            'go to',
            'travel to',
            'walk to',
            'mosey on over to',
            'crawl to',
            'skip to',
            'run to',
            'head to',
            'head over to'
        ]
