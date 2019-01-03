import pygame


class PyGame(object):

    def __init__(self, screensize):
        self._pygame = pygame
        self._pygame.init()
        self._clock = self._pygame.time.Clock()
        self._screen = self._pygame.display.set_mode(screensize)

    def quit(self):
        self._pygame.quit()

    @property
    def events(self):
        return self._pygame.event.get()

    @property
    def keys_pressed(self):
        return self._pygame.key.get_pressed()

    @property
    def clock(self):
        return self._clock

    @property
    def display(self):
        return self._pygame.display

    @property
    def screen(self):
        return self._screen

    def push_event(self, event, data=None):
        event = self._pygame.event.Event(event, data or {})
        return self._pygame.event.post(event)

    def draw_rect(self, surface, color, rect, width=0):
        self._pygame.draw.rect(surface, color, rect, width)
