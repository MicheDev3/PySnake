import thorpy


class Thorpy(object):

    def __init__(self, screen):
        self.screen = screen
        self._thorpy = thorpy

    def make_text(self, text, position=None, color=(255, 255, 255), func=None, params=None):
        text = self._thorpy.OneLineText.make(text, func, params)
        text.set_font_color(color)
        if position:
            text.set_topleft(position)
        return text

    def make_button(self, text, func=None, params=None):
        return self._thorpy.make_button(text, func, params)

    def make_box(self, elements, position, size=None):
        box = self._thorpy.Box.make(elements, size)
        box.set_topleft(position)
        return box

    def make_menu(self, box=None):
        menu = self._thorpy.Menu(box)
        for element in menu.get_population():
            element.surface = self.screen
        return menu
