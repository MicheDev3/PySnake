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

        def __init__(self, pos, color, head=False):
            self.dirnx = 0
            self.dirny = 0
            self.pos = pos
            self.color = color
            self.head = head

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

    def grow(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(self.Body((tail.pos[0] - 1, tail.pos[1]), tail.color))
        elif dx == -1 and dy == 0:
            self.body.append(self.Body((tail.pos[0] + 1, tail.pos[1]), tail.color))
        elif dx == 0 and dy == 1:
            self.body.append(self.Body((tail.pos[0], tail.pos[1] - 1), tail.color))
        elif dx == 0 and dy == -1:
            self.body.append(self.Body((tail.pos[0], tail.pos[1] + 1), tail.color))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, screen, size, engine):
        for part in self.body:
            pos_x, pos_y = part.pos
            engine.draw_rect(
                screen, part.color, (pos_x * size + 1, pos_y * size + 1, size - 2, size - 2)
            )
