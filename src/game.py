from src.event import EVENT_TYPE

from src.engine import PyEngine
from src.window import Window


class Game(object):

    def __init__(self, engine=PyEngine()):
        self.running = True
        self._engine = engine
        self._window = Window(self._engine)

    def on_event(self):
        for event in self._engine.events:
            self._window.on_event(event)
            if event.type == EVENT_TYPE['QUIT']:
                self.running = False

    def on_update(self):
        self._engine.screen.fill((0, 0, 0))
        self._window.on_update()
        self._engine.display.update()

    def run(self):

        while self.running:
            # TODO change game loop clock system
            self._engine.clock.tick(10)
            self.on_update()
            self.on_event()

        self._engine.on_shutdown()
