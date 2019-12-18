from commands import Command


class Inventory(Command):

    def do(self, text: str):
        player = self.get_player()

        print('Inventory:')
        if not player.all_items():
            print('Nothing.')
        for item in player.all_items():
            print(item)

    def get_description(self):
        return 'In case you forget what you\'re holding.'

    def get_aliases(self):
        return [
            'show inventory',
            'what am i holding',
            'what do i have',
            'my stuff',
            'my items',
            'i',
            'list my inventory',
            'list my stuff',
            'list my items'
        ]
