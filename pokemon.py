from tkinter import *
from tkinter.font import Font
from move import Move
from PIL import ImageTk, Image, ImageOps

# Pokemon class for keeping track of the statuses the 6 characters (you,
# tia, maggie, amyg, squirrel, gs)


class Pokemon(object):
    def __init__(
            self,
            name,
            health,
            avatar,
            nameb_img,
            nameblvl_img,
            namew_img,
            attack1_img,
            attack2_img,
            attack3_img,
            attack4_img):
        self.name = name
        self.health = health
        self.avatar = avatar
        self.nameb_img = nameb_img
        self.nameblvl_img = nameblvl_img
        self.namew_img = namew_img
        self.attack1_img = attack1_img
        self.attack2_img = attack2_img
        self.attack3_img = attack3_img
        self.attack4_img = attack4_img
        self.move_list = []

    def add_move(self, name, damage, desc1, desc2):
        move = Move(name, damage, desc1, desc2)
        self.move_list.append(move)
