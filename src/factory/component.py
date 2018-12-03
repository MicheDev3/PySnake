import random

__all__ = ['PlayerInputComponent', 'CollisionComponent']


class PlayerInputComponent(object):

    def __init__(self):
        self.dirnx = 0
        self.dirny = 0
        self.turns = {}

    def update(self, game_object, scene, engine):
        keys = engine.keys_pressed
        if keys[engine.Input.UP] and self.dirny != 1:
            self.dirnx = 0
            self.dirny = -1
        if keys[engine.Input.DOWN] and self.dirny != -1:
            self.dirnx = 0
            self.dirny = 1
        if keys[engine.Input.LEFT] and self.dirnx != 1:
            self.dirnx = -1
            self.dirny = 0
        if keys[engine.Input.RIGHT] and self.dirnx != -1:
            self.dirnx = 1
            self.dirny = 0

        self.turns[game_object.body[0].pos[:]] = [self.dirnx, self.dirny]
        for index, part in enumerate(game_object.body):
            p = part.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                part.move(turn[0], turn[1], scene.rows)
                if index == len(game_object.body) - 1:
                    self.turns.pop(p)
                continue
            part.move(part.dirnx, part.dirny, scene.rows)


class CollisionComponent(object):

    @staticmethod
    def detect_collision(pos, body):
        return len(list(filter(lambda z: z.pos == pos, body))) > 0

    def update(self, game_object, scene, engine):
        body = game_object.body
        for obj in scene.game_objects:
            if obj is game_object:
                continue
            # detecting collision with other objects
            if self.detect_collision(obj.body[-1].pos, body):
                while True:
                    pos = (random.randrange(scene.rows), random.randrange(scene.rows))
                    if self.detect_collision(pos, body) > 0:
                        continue

                    game_object.grow()
                    # TODO do it in an other way
                    obj.body[-1].pos = pos
                    break

        # detecting collision with it self
        if len(body) > 1:
            head, body = body[0], body[1:]
            if self.detect_collision(head.pos, body) > 0:
                event = engine.Event.QUIT
                engine.push_event(event)