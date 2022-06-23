from game.casting.actor import Actor
from game.casting.player import Player
import constants
from game.shared.point import Point



class Player_Red(Player):
    '''Keeps track of the score for red player.

    Creates and tracks the trail of red player.
    '''

    def __init__(self):
        '''New instance of actor created
        
        
        Attributes:
            _trail(list): the player's trail
            _player_color(color): the color of the player
            _score_text: the text to be displayed as the score
            _starting_position: the position at which the player starts
            '''


        x = int(constants.MAX_X / 4)
        y = int(constants.MAX_Y / 2)

        super().__init__()
        self._trail = []
        self._player_color = constants.RED
        self._score_text = (f'Red Score: {self._points}')
        self._starting_position = Point(x,y)
