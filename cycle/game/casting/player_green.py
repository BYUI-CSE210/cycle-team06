from game.casting.actor import Actor
import constants

class Player_Green(Actor):
    '''Keeps track of the score for green player.

    Creates and tracks the trail of green player.
    '''

    def __init__(self):
        '''New instance of actor created'''

        super.().__init__()
        self.player_color = constants.GREEN
        self._is_game_over = False
        self._starting_position()
        self._points = 0
        self.add_points(0)

    def get_trail(self):
        '''Creates the trail for the player'''

        return self._trail[1:]

    def get_player(self):
        '''Gets the first item for the trail list'''
        
        return self._trail[0]

    def starting_position(self):
        '''Positions green player at its point of origin'''

        x = int(MAX_X / 4 * 3)
        y = int(MAX_Y / 2)

        for i in range(constants.TRAIL_LENGTH):
            position = Point(x, y - i * constants.CELL_SIZE)
            velocity = (0, constants.CELL_SIZE)
            text = '@' if i == 0 else '#'

            trail = Actor()
            trail.set_position(position)
            trail.set_velocity(velocity)
            trail.set_text(text)
            trail.set_color(self.player_color)
            self._trail.append(trail)

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
        '''Adds points to green player'''

        self._points += points
        self.score_text(f'Green Score: {self._points}')