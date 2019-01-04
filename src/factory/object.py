from src.factory.component import *


class ObjectFactory(object):

    @staticmethod
    def create_snake():
        return Object((10, 10), (255, 0, 0), [PlayerInputComponent(), CollisionComponent()])

    @staticmethod
    def create_snack():
        return Object((5, 5), (128, 0, 0), [])


class Object(object):

    class Body(object):

        def __init__(self, pos, color):
            self._dirnx = 0
            self._dirny = 0
            self._pos = pos
            self._color = color

        @property
        def dirnx(self):
            return self._dirnx

        @property
        def dirny(self):
            return self._dirny

        def _get_pos(self):
            return self._pos

        def _set_pos(self, pos):
            self._pos = pos

        pos = property(_get_pos, _set_pos)

        def move(self, dirnx, dirny, max):
            if self._pos[0] + dirnx > max:
                pos_x = -1
            elif self._pos[0] + dirnx < 0:
                pos_x = max
            else:
                pos_x = self._pos[0]

            if self._pos[1] + dirny > max:
                pos_y = -1
            elif self._pos[1] + dirny < 0:
                pos_y = max
            else:
                pos_y = self._pos[1]

            self._dirnx = dirnx
            self._dirny = dirny
            self._pos = (pos_x + dirnx, pos_y + dirny)

    def __init__(self, pos, color, components):
        self._components = components
        self._body = [self.Body(pos, color)]

    @property
    def body(self):
        return self._body

    def update(self, scene, engine):
        for component in self._components:
            component.update(self, scene, engine)

    def is_on_screen(self, rows):
        return self._body[0]._pos[0] < rows and self._body[0]._pos[1] < rows

    def grow(self):
        dirnx, dirny = self._body[-1]._dirnx, self._body[-1]._dirny

        if dirnx == 1 and dirny == 0:
            self._body.append(self.Body((self._body[-1]._pos[0] - 1, self._body[-1]._pos[1]), self._body[-1]._color))
        elif dirnx == -1 and dirny == 0:
            self._body.append(self.Body((self._body[-1]._pos[0] + 1, self._body[-1]._pos[1]), self._body[-1]._color))
        elif dirnx == 0 and dirny == 1:
            self._body.append(self.Body((self._body[-1]._pos[0], self._body[-1]._pos[1] - 1), self._body[-1]._color))
        elif dirnx == 0 and dirny == -1:
            self._body.append(self.Body((self._body[-1]._pos[0], self._body[-1]._pos[1] + 1), self._body[-1]._color))

        self._body[-1]._dirnx = dirnx
        self._body[-1]._dirny = dirny

    def draw(self, size, engine):
        for part in self._body:
            pos_x, pos_y = part._pos
            engine.draw_rect(
                engine.screen, part._color, (pos_x * size + 1, pos_y * size + 1, size - 2, size - 2)
            )
