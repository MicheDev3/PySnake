from src.factory.object import ObjectFactory


class Scene(object):

    def __init__(self, engine, screensize=(500, 500)):
        self.engine = engine

        self.current = "GameScene"
        # TODO add more scenes (Intro, Settings)
        self.scenes = {'GameScene': GameScene()}

        self.screensize = screensize
        self.screen = self.engine.display.set_mode(screensize)

    def loop(self):
        self.scenes[self.current].loop(
            self.engine, self.screen, self.screensize
        )
        self.engine.display.update()


class GameScene(object):

    def __init__(self):
        self.rows = 20
        self._game_objects = [ObjectFactory.create_snack(), ObjectFactory.create_snake()]

    @property
    def game_objects(self):
        return self._game_objects

    def loop(self, engine, screen, screensize):
        # rendering the scene
        screen.fill((0, 0, 0))
        # drawing the grid
        x, y, width = 0, 0, screensize[0]
        size = width // self.rows
        # remove the # in order to see the grid
        # for r in range(self.rows):
        #     x, y = x + size, y + size
        #     engine.draw_line(screen, (255, 255, 255), (x, 0), (x, width))
        #     engine.draw_line(screen, (255, 255, 255), (0, y), (width, y))

        for game_object in self._game_objects:
            game_object.update(self, engine)        # updating the game objects
            game_object.draw(screen, size, engine)  # rendering the game objects
