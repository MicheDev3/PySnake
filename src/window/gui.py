from src.event import EVENT_TYPE

__all__ = ['MenuGui', 'GameGui', 'SettingsGui']


class MenuGui(object):

    def __init__(self, engine):
        self._engine = engine
        self._visible = True
        self._create_gui()

    def _create_gui(self):
        size = (100, 100)
        position = ((self._engine.screensize[0] - size[0]) // 2,
                    (self._engine.screensize[1] - size[1]) // 2
                    )
        # gui elements
        self._start_button = self._engine.make_button(
            "Start", func=self._engine.push_event, params={'event': EVENT_TYPE['START']}
        )
        self._quit_button = self._engine.make_button(
            "Quit", func=self._engine.push_event, params={'event': EVENT_TYPE['QUIT']}
        )
        self._settings_button = self._engine.make_button(
            "Settings", func=self._engine.push_event, params={'event': EVENT_TYPE['SETTINGS']}
        )
        self._box = self._engine.make_box(
            [self._start_button, self._quit_button, self._settings_button], position, size=size
        )
        self._menu = self._engine.make_menu(self._box)

    def _render_gui(self):
        self._box.blit()
        self._box.update()

    def on_event(self, event):
        self._menu.react(event)

    def on_update(self):
        if self._visible:
            self._render_gui()


class GameGui(object):

    def __init__(self, engine):
        self._engine = engine
        self._visible = False
        self._create_gui()

    def _create_gui(self):
        size = (100, 100)
        position = ((self._engine.screensize[0] - size[0]) // 2,
                    (self._engine.screensize[1] - size[1]) // 2
                    )
        # gui elements
        # TODO fix position text inside the box
        self._score_text = self._engine.make_text("")
        self._retry_button = self._engine.make_button(
            "Retry", func=self._engine.push_event, params={'event': EVENT_TYPE['START']}
        )
        self._menu_button = self._engine.make_button(
            "Menu", func=self._engine.push_event, params={'event': EVENT_TYPE['MENU']}
        )
        self._box = self._engine.make_box(
            [self._score_text, self._retry_button, self._menu_button], position, size=size
        )
        self._menu = self._engine.make_menu()

    def _render_gui(self):
        self._box.blit()
        self._box.update()

    def on_event(self, event):
        if event.type == EVENT_TYPE['DEAD']:
            self._visible = True
            self._menu = self._engine.make_menu(self._box)
            self._score_text.set_text("Score: %s" % event.score)
        if event.type == EVENT_TYPE['START']:
            self._visible = False
            self._menu = self._engine.make_menu()
        self._menu.react(event)

    def on_update(self):
        if self._visible:
            self._render_gui()


class SettingsGui(object):

    def __init__(self, engine):
        self._engine = engine
        self._visible = True
        self._create_gui()

    def _create_gui(self):
        box_size = (50, 35)
        position = ((self._engine.screensize[0] - box_size[0]) // 2, (self._engine.screensize[1] - box_size[1]) // 2)
        # gui elements
        self._back_button = self._engine.make_button(
            "Back", func=self._engine.push_event, params={'event': EVENT_TYPE['MENU']}
        )
        self._box = self._engine.make_box([self._back_button], position, size=box_size)
        self._menu = self._engine.make_menu(self._box)

    def _render_gui(self):
        self._box.blit()
        self._box.update()

    def on_event(self, event):
        self._menu.react(event)

    def on_update(self):
        if self._visible:
            self._render_gui()
