from src.event import EVENT_TYPE
from src.factory.object import ObjectFactory


class Scene(object):

    def __init__(self, engine):
        self.current = "MenuScene"
        self.scenes = {"GameScene": GameScene(engine),
                       "MenuScene": MenuScene(engine),
                       "SettingsScene": SettingsScene(engine),
                       }

    def on_event(self, event):
        if event.type == EVENT_TYPE['START']:
            self.current = "GameScene"
        elif event.type == EVENT_TYPE['MENU']:
            self.current = "MenuScene"
        elif event.type == EVENT_TYPE['SETTINGS']:
            self.current = "SettingsScene"

        self.scenes[self.current].on_event(event)
        if self.scenes[self.current]._menu:
            self.scenes[self.current]._menu.react(event)

    def on_update(self):
        self.scenes[self.current].on_update()


class MenuScene(object):

    def __init__(self, engine):
        self._engine = engine
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
        pass

    def on_update(self):
        self._engine.screen.fill((0, 0, 0))

        self._render_gui()


class GameScene(object):

    def __init__(self, engine):
        self.rows = 20
        self._is_dead = False
        self._engine = engine
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

    def _render_gui(self):
        self._box.blit()
        self._box.update()

    def _reset(self):
        self._score = 0
        self._menu = None  # reset the menu object
        self._is_dead = False
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
            self._is_dead = True
            # create the menu box only when _is_dead
            # is True and delete when False, this avoid
            # rendering the box when hovering with
            # the cursor
            self._menu = self._engine.make_menu(self._box)
            self._score_text.set_text("Score: %s" % self._score)
        if event.type == EVENT_TYPE['START']:
            self._reset()

    def on_update(self):
        # rendering the scene
        self._engine.screen.fill((0, 0, 0))
        width = self._engine.screensize[0]

        if self._is_dead:
            self._render_gui()
            return

        for game_object in self._game_objects:
            game_object.update(self, self._engine)
            game_object.draw(width // self.rows, self._engine)


class SettingsScene(object):

    def __init__(self, engine):
        self._engine = engine

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
        pass

    def on_update(self):
        self._engine.screen.fill((0, 0, 0))

        self._render_gui()
