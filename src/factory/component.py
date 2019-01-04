import random

from src.event import EVENT_TYPE

__all__ = ['PlayerInputComponent', 'CollisionComponent']


class PlayerInputComponent(object):

    def __init__(self):
        self._dirnx = 0
        self._dirny = 0
        self._turns = {}

    def update(self, game_object, scene, engine):
        keys = engine.keys_pressed
        if game_object.is_on_screen(scene.rows):
            if keys[EVENT_TYPE['UP']] and self._dirny != 1:
                self._dirnx = 0
                self._dirny = -1
            if keys[EVENT_TYPE['DOWN']] and self._dirny != -1:
                self._dirnx = 0
                self._dirny = 1
            if keys[EVENT_TYPE['LEFT']] and self._dirnx != 1:
                self._dirnx = -1
                self._dirny = 0
            if keys[EVENT_TYPE['RIGHT']] and self._dirnx != -1:
                self._dirnx = 1
                self._dirny = 0

        self._turns[game_object.body[0].pos[:]] = [self._dirnx, self._dirny]
        for index, part in enumerate(game_object.body):
            p = part.pos[:]
            if p in self._turns:
                turn = self._turns[p]
                part.move(turn[0], turn[1], scene.rows)
                if index == len(game_object.body) - 1:
                    self._turns.pop(p)
                continue
            part.move(part.dirnx, part.dirny, scene.rows)


class CollisionComponent(object):

    @staticmethod
    def _detect_collision(pos, body):
        return len(list(filter(lambda z: z.pos == pos, body))) > 0

    def update(self, game_object, scene, engine):
        body = game_object.body
        for obj in scene.game_objects:
            if obj is game_object:
                if len(body) > 1:
                    head, body = body[0], body[1:]
                    if self._detect_collision(head.pos, body) > 0:
                        engine.push_event(EVENT_TYPE['DEAD'], {'score': scene.score})
                continue
            # detecting collision with other objects
            if self._detect_collision(obj.body[-1].pos, body):
                engine.push_event(EVENT_TYPE['SNACK_EATEN'])
                while True:
                    pos = (random.randrange(scene.rows), random.randrange(scene.rows))
                    if self._detect_collision(pos, body) > 0:
                        continue

                    game_object.grow()
                    # TODO do it in an other way
                    obj.body[-1].pos = pos
                    break
