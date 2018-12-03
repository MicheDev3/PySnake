import enum
import pygame


class PyEngine(object):

    class Input(enum.IntEnum):
        # TODO add mapping key with some settings page
        UP = pygame.K_UP
        DOWN = pygame.K_DOWN
        LEFT = pygame.K_LEFT
        RIGHT = pygame.K_RIGHT

    class Event(enum.IntEnum):
        QUIT = pygame.QUIT

    def __init__(self):
        self._lib = pygame
        self._lib.init()
        self._clock = self._lib.time.Clock()

    def on_quit(self):
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

    def push_event(self, event, data=None):
        event = self._lib.event.Event(event, data or {})
        return self._lib.event.post(event)

    def draw_line(self, surface, color, start_pos, end_pos, width=1):
        self._lib.draw.line(surface, color, start_pos, end_pos, width)

    def draw_rect(self, surface, color, rect, width=0):
        self._lib.draw.rect(surface, color, rect, width)

    def draw_circle(self, surface, color, pos, radius, width=0):
        self._lib.draw.circle(surface, color, pos, radius, width)
