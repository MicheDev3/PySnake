from src.engine import PyEngine
from src.scene import Scene


class Game(object):

    def __init__(self, engine=PyEngine()):
        self._engine = engine
        self._clock = self._engine.clock
        self._scene = Scene(self._engine)

    def main_loop(self):
        while True:
            # TODO change game loop clock system
            self._clock.tick(10)
            for event in self._engine.events:
                if event.type == self._engine.Event.QUIT:
                    self._engine.on_quit()
                    return
            self._scene.loop()
