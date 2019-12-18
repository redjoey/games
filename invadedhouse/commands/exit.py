import sys

from commands import Command


class Exit(Command):

    def do(self, text: str):
        player = self.player
        print(f'Leaving so soon, {player.get_name()}?? Ok, bye!')
        sys.exit()

    def get_description(self):
        return 'Exits the game.'

    def get_aliases(self):
        return [
            'bye',
            'i\'m leaving',
            'i\'m gonna exit',
            'end game', 'quit',
            'goodbye',
            'leave',
            'leave so soon',
            'delete my progress',
            'get outta here',
            'skedaddle',
            'let me out',
            'stop',
            'end',
            'avengers endgame',
            'im scared of this place i wanna go home',
            'i wanna go home',
            'i want my mommy',
            'i want my daddy',
            'im out',
            'goodbye',
            'this game is trash',
            'i dont like this game',
            'i dont like this',
            'stop running run.py',
            f'go from {self.player.get_location()} to my house',
            'walk into the strange portal that is on the wall that leads to my home',
            'when is this going to end',
            f'create a portal to my house in {self.player.get_location()}',
            'i hate you',
            'exit the game'
        ]
