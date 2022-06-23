from game.casting.actor import Actor
from game.casting.player import Player
from game.shared.point import Point
import constants

class Player_Green(Player):
    '''Keeps track of the score for green player.

    Creates and tracks the trail of green player.
    '''

    def __init__(self):
        '''New instance of actor created
        
        
        Attributes:
            _trail(list): the player's trail
            _player_color(color): the color of the player
            _score_text: the text to be displayed as the score
            _starting_position: the position at which the player starts
            '''

        super().__init__()
        self._trail = []
        self.player_color = constants.GREEN
        self.score_text = (f'Green Score: {self._points}')
        x = int(constants.MAX_X / 4*3)
        y = int(constants.MAX_Y / 2)
        self._starting_position = Point(x,y)

