from src.event import EVENT_TYPE

from src.factory import ObjectFactory

__all__ = ['MenuScene', 'GameScene', 'SettingsScene']


class MenuScene(object):

    def __init__(self, engine):
        self._engine = engine

    def _render_gui(self):
        pass

    def on_event(self, event):
        pass

    def on_update(self):
        pass


class GameScene(object):

    def __init__(self, engine):
        self.rows = 20
        self._dead = False
        self._engine = engine

    def _reset(self):
        self._score = 0
        self._dead = False
        self._game_objects = [ObjectFactory.create_snack(),
                              ObjectFactory.create_snake()
                              ]

    @property
    def game_objects(self):
        return self._game_objects

    @property
    def score(self):
        return self._score

    def on_event(self, event):
        if event.type == EVENT_TYPE['SNACK_EATEN']:
            self._score += 1
        if event.type == EVENT_TYPE['DEAD']:
            self._dead = True
        if event.type == EVENT_TYPE['START']:
            self._reset()

    def on_update(self):
        if self._dead:
            return

        width = self._engine.screensize[0]

        for game_object in self._game_objects:
            game_object.update(self, self._engine)
            game_object.draw(width // self.rows, self._engine)


class SettingsScene(object):

    def __init__(self, engine):
        self._engine = engine

    def on_event(self, event):
        pass

    def on_update(self):
        pass
