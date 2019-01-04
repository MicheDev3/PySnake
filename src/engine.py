from src.vendor import PyGame, Thorpy


class PyEngine(object):

    def __init__(self):
        self._screensize = (500, 500)
        self._lib = PyGame(self._screensize)
        self._gui = Thorpy(self._lib.screen)

    def on_shutdown(self):
        self._lib.quit()

    @property
    def events(self):
        return self._lib.events

    @property
    def keys_pressed(self):
        return self._lib.keys_pressed

    @property
    def clock(self):
        return self._lib.clock

    @property
    def display(self):
        return self._lib.display

    @property
    def screensize(self):
        return self._screensize

    @property
    def screen(self):
        return self._lib.screen

    def make_text(self, text, position=None, color=(255, 255, 255), func=None, params=None):
        return self._gui.make_text(text, position, color, func, params)

    def make_button(self, text, func=None, params=None):
        return self._gui.make_button(text, func, params)

    def make_box(self, elements, position, size=None):
        return self._gui.make_box(elements, position, size)

    def make_menu(self, box=None):
        return self._gui.make_menu(box)

    def push_event(self, event, data=None):
        self._lib.push_event(event, data)

    def draw_rect(self, surface, color, rect, width=0):
        self._lib.draw_rect(surface, color, rect, width)
