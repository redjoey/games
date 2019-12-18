from commands import Command


class Warp(Command):

    def do(self, text: str):
        player = self.get_player()
        house = self.get_house()

        print('OMG YOU FOUND MY BRILLIANTLY WONDERFUL SECRET!!')
        warp_room = house.find_room_by_name('warp room')
        player.set_location(warp_room)

    def is_secret(self):
        return True

    def get_description(self):
        return 'Ssshhhh.....'

    def get_aliases(self):
        return []
