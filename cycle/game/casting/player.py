from game.casting.actor import Actor
from game.shared.point import Point
import constants

class Player(Actor):
    '''Keeps track of the score for green player.

    Creates and tracks the trail of green player.
    '''

    def __init__(self):
        '''New instance of actor created
        
        attributes:
            _text: the text to display
            _player_color: the color of the player
            _is_game_over: the game over flag
            _starting_position:the starting position of the player
            _points:the number of points per player
            _trail:the trail of the cycle.
            '''

        super().__init__()
        self._text = "@"
        self.player_color = ""
        self._is_game_over = False
        self._starting_position = self.starting_position()
        self._points = 0
        self._trail = []
        self._prepare_trail()

    def get_trail(self):
        '''Creates the trail for the player'''

        return self._trail[1:]

    def get_player(self):
        '''Gets the first item for the trail list'''
        
        return self._trail[0]

    def starting_position(self):
        '''Positions green player at its point of origin'''
        pass
    #    x = ""
   #     y = ""

  #      for i in range(constants.TRAIL_LENGTH):
   #         position = Point(x, y - i * constants.CELL_SIZE)
   #         velocity = (0, constants.CELL_SIZE)
   #         text = '@' if i == 0 else '#'
#
   #         trail = Actor()
  #         trail.set_position(position)
  #          trail.set_velocity(velocity)
  ##          trail.set_text(text)
  #          trail.set_color(self.player_color)
  #          self._trail.append(trail)

    def trail_growth(self):
        '''grows the trail'''

        player = self._trail[0]
        velocity = player.get_velocity()

        trail = Actor()
        trail.set_position(position)
        trail.set_velocity(velocity)
        trail.set_text('#')
        trail.set_color(self.player_color)
        self._trail.append(trail)


    def add_points(self, points):
        '''Adds points to player'''

        self._points += points

    def _prepare_trail(self):
        x = int(constants.MAX_X/2)
        y = int(constants.MAX_Y/2)

        for i in range(constants.TRAIL_LENGTH):
            position = Point(x-i * constants.CELL_SIZE, y)
            velocity = Point(1* constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            color = self._color

            trail = Actor()
            trail.set_position(position)
            trail.set_velocity(velocity)
            trail.set_text(text)
            trail.set_color(color)
            self._trail.append(trail)

    