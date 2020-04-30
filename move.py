class Move(object):
    def __init__(self, name, damage, atck, defense, speed):
        self.name = name
        self.damage = damage
        self.atck = atck
        self.defense = defense
        self.speed = speed

    def printName(self):
        print(self.name)

if __name__ == "__main__":
    move = Move()