from src.event import EVENT_TYPE

from src.window.scene import *
from src.window.gui import *


class Window(object):

    SCENES = ['Menu', 'Game', 'Settings']

    def __init__(self, engine):
        self._current = "Menu"
        self._guis = dict(zip(
            self.SCENES, [MenuGui(engine), GameGui(engine), SettingsGui(engine)])
        )
        self._scenes = dict(zip(
            self.SCENES, [MenuScene(engine), GameScene(engine), SettingsScene(engine)])
        )

    def on_event(self, event):
        if event.type == EVENT_TYPE['START']:
            self._current = "Game"
        elif event.type == EVENT_TYPE['MENU']:
            self._current = "Menu"
        elif event.type == EVENT_TYPE['SETTINGS']:
            self._current = "Settings"

        self._scenes[self._current].on_event(event)
        self._guis[self._current].on_event(event)

    def on_update(self):
        self._scenes[self._current].on_update()
        self._guis[self._current].on_update()
