from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.

    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.

        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        player_red = cast.get_first_actor("red")
        player_green = cast.get_first_actor("green")
        green_trail = player_green.get_trail()
        red_trail = player_red.get_trail()

        self._video_service.clear_buffer()
        self._video_service.draw_actor(player_green)
        self._video_service.draw_actor(player_red)
        self._video_service.draw_actors(green_trail)
        self._video_service.draw_actors(red_trail)

        self._video_service.flush_buffer()
