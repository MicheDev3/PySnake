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
            self.dirnx = 0
            self.dirny = 0
            self.pos = pos
            self.color = color

        def move(self, dirnx, dirny, max):
            if self.pos[0] + dirnx > max:
                pos_x = -1
            elif self.pos[0] + dirnx < 0:
                pos_x = max
            else:
                pos_x = self.pos[0]

            if self.pos[1] + dirny > max:
                pos_y = -1
            elif self.pos[1] + dirny < 0:
                pos_y = max
            else:
                pos_y = self.pos[1]

            self.dirnx = dirnx
            self.dirny = dirny
            self.pos = (pos_x + dirnx, pos_y + dirny)

    def __init__(self, pos, color, components):
        self.components = components
        self.body = [self.Body(pos, color)]

    def update(self, scene, engine):
        for component in self.components:
            component.update(self, scene, engine)

    def is_on_screen(self, rows):
        return self.body[0].pos[0] < rows and self.body[0].pos[1] < rows

    def grow(self):
        dirnx, dirny = self.body[-1].dirnx, self.body[-1].dirny

        if dirnx == 1 and dirny == 0:
            self.body.append(self.Body((self.body[-1].pos[0] - 1, self.body[-1].pos[1]), self.body[-1].color))
        elif dirnx == -1 and dirny == 0:
            self.body.append(self.Body((self.body[-1].pos[0] + 1, self.body[-1].pos[1]), self.body[-1].color))
        elif dirnx == 0 and dirny == 1:
            self.body.append(self.Body((self.body[-1].pos[0], self.body[-1].pos[1] - 1), self.body[-1].color))
        elif dirnx == 0 and dirny == -1:
            self.body.append(self.Body((self.body[-1].pos[0], self.body[-1].pos[1] + 1), self.body[-1].color))

        self.body[-1].dirnx = dirnx
        self.body[-1].dirny = dirny

    def draw(self, size, engine):
        for part in self.body:
            pos_x, pos_y = part.pos
            engine.draw_rect(
                engine.screen, part.color, (pos_x * size + 1, pos_y * size + 1, size - 2, size - 2)
            )
