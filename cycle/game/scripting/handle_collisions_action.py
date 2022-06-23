import constants
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_player_colision(cast)
            self._handle_game_over(cast)

    def _handle_player_colision(self, cast):
        """sets the game over flag if the players collide
                Args:
            cast (Cast): The cast of Actors in the game."""

        player_red = cast.get_first_actor("red")
        player_green = cast.get_first_actor("green")
        green_trail = player_green.get_trail()[1:]
        red_trail = player_red.get_trail()[1:]

        for t in green_trail:
            if player_red.get_position().equals(t.get_position()):
                self._is_game_over = True
    
        for t in red_trail:
            if player_green.get_position().equals(t.get_position()):
                self._is_game_over = True
    
    def _handle_game_over(self, cast):
        """shows the game over message and changes colors to white
        
                Args:
            cast (Cast): The cast of Actors in the game."""


        if self._is_game_over:
            player_red = cast.get_first_actor("red")
            player_green = cast.get_first_actor("green")
            green_trail = player_green.get_trail()[1:]
            red_trail = player_red.get_trail()[1:]


            for i in green_trail:
                i.set_color(constants.WHITE)
            
            for i in red_trail:
                i.set_color(constants.WHITE)
            
            player_green.set_color(constants.WHITE)
            player_red.set_color(constants.WHITE)







