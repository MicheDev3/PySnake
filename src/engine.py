import pygame
import thorpy


class PyEngine(object):

    def __init__(self):
        self._lib = pygame
        self._gui = thorpy
        self._lib.init()
        self._screensize = (500, 500)
        self._clock = self._lib.time.Clock()
        self._screen = self._lib.display.set_mode(self._screensize)

    def on_shutdown(self):
        self._lib.quit()

    @property
    def events(self):
        return self._lib.event.get()

    @property
    def keys_pressed(self):
        return self._lib.key.get_pressed()

    @property
    def clock(self):
        return self._clock

    @property
    def display(self):
        return self._lib.display

    @property
    def screensize(self):
        return self._screensize

    @property
    def screen(self):
        return self._screen

    def make_text(self, text, position=None, color=(255, 255, 255), func=None, params=None):
        text = self._gui.OneLineText.make(text, func, params)
        text.set_font_color(color)
        if position:
            text.set_topleft(position)
        return text

    def make_button(self, text, func=None, params=None):
        return self._gui.make_button(text, func, params)

    def make_box(self, elements, position, size=None):
        box = self._gui.Box.make(elements, size)
        box.set_topleft(position)
        return box

    def make_menu(self, box=None):
        menu = self._gui.Menu(box)
        for element in menu.get_population():
            element.surface = self.screen
        return menu

    def push_event(self, event, data=None):
        event = self._lib.event.Event(event, data or {})
        return self._lib.event.post(event)

    def draw_rect(self, surface, color, rect, width=0):
        self._lib.draw.rect(surface, color, rect, width)
