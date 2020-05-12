# class for creating new moves. There are four moves assigned to each Pokemon.
class Move(object):
    def __init__(self, name, damage, desc1, desc2):
        self.name = name
        self.damage = damage
        self.desc1 = desc1
        self.desc2 = desc2


if __name__ == "__main__":
    move = Move()