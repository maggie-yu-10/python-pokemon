from move import Move
from PIL import ImageTk, Image, ImageOps
class Pokemon(object):
    def __init__(self, name, level, basehealth, health, atck, defense, speed):
        self.name = name
        self.level = level
        self.basehealth = basehealth
        self.health = health
        self.atck = atck
        self.defense = defense
        self.speed = speed
        self.move_list = []

    def getName(self):
        return name

    def add_move(self, name, damage, atck, defense, speed):
        move = Move(name, damage, atck, defense, speed)
        self.move_list.append(move)

    def get_atck_img(self):
        return self.atck_img
