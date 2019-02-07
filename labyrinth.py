import random
import pygame
from pygame.locals import *

class Input_user:

    def __init__(self):
        self.move = ""

    def entry_user(self):
        self.move = input("Entrez ZQSD pour vous déplacer : ")
        return self.move

entry = Input_user()

class Characters:

    def __init__(self, maps):
        self.maps = maps
    
    def mc_position(self):
        position = self.maps.index("M")
        #print(position)
        return position

    def tina_position(self):
        positiontina = self.maps.index("T")
        return positiontina
#mac = Mcgyver()

class Motion:

    def __init__(self, maps, position, move, tina):
        self.maps = maps
        self.position = position
        self.move = move
        self.tina = tina

    def direction(self):
        maps = self.maps
        move = self.move
        position = self.position
        tina = self.tina

        if move == "Z" or move == "z":
            if maps[position - 16] == " " or maps[position - 16] == "X" or maps[position - 16] == "Y" or maps[position - 16] == "Z":
                maps[position - 16] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
            elif tina == True and maps[position - 16] == "T":
                maps[position - 16] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                print("YOU WIN")
            else:
                maps = "".join(maps)
                print(maps)
        if move == "S" or move == "s":
            if maps[position + 16] == " " or maps[position + 16] == "X" or maps[position + 16] == "Y" or maps[position + 16] == "Z":
                maps[position + 16] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
            elif tina == True and maps[position + 16] == "T":
                maps[position + 16] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                print("YOU WIN")
            else:
                maps = "".join(maps)
                print(maps)
        if move == "Q" or move == "q":
            if maps[position - 1] == " " or maps[position - 1] == "X" or maps[position - 1] == "Y" or maps[position - 1] == "Z":
                maps[position - 1] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
            elif tina == True and maps[position - 1] == "T":
                maps[position - 1] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                print("YOU WIN")
            else:
                maps = "".join(maps)
                print(maps)
        if move == "D" or move == "d":
            if maps[position + 1] == " " or maps[position + 1] == "X" or maps[position + 1] == "Y" or maps[position + 1] == "Z":
                maps[position + 1] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
            elif tina == True and maps[position + 1] == "T":
                maps[position + 1] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                print("YOU WIN")
            else:
                maps = "".join(maps)
                print(maps)
        return maps
        
class Items:

    def __init__(self, maps, space_list):
        self.maps = maps
        self.space_list = space_list
        
    def item_position(self):
        space_list = self.space_list
        maps = self.maps

        space_rand = random.randint(0, len(self.space_list) - 1)
        X = space_list[space_rand]
        maps[X] = "X"
        space_rand = random.randint(0, len(self.space_list) - 1)
        Y = space_list[space_rand]
        maps[Y] = "Y"
        space_rand = random.randint(0, len(self.space_list) - 1)
        Z = space_list[space_rand]
        maps[Z] = "Z"
        maps = "".join(maps)
        #print(X, Y, Z)
        return X, Y, Z
    
    #def item_coord(self):

class Collect:

    def __init__(self, position, X, Y, Z):
        self.position = position
        self.X = X
        self.Y = Y
        self.Z = Z
    
    def collect_items(self):
        position = self.position
        X = self.X
        Y = self.Y
        Z = self.Z

        if X != True or Y != True or Z != True:
            if position == X:
                X = True
                print("X collected !")
            else:
                pass
            if position == Y:
                Y = True
                print("Y collected !")
            else:
                pass
            if position == Z:
                Z = True
                print("Z collected !")
            else:
                pass
        return X, Y, Z

class Tina:

    def __init__(self, X, Y, Z, maps):
        self.X = X
        self.Y = Y
        self.Z = Z
    
    def tina_ready(self):
        X = self.X
        Y = self.Y
        Z = self.Z

        if X == True and Y == True and Z == True:
            tina = True
            print("Tina is ready to lose")
            return tina
        else:
            pass

#class Graphic:

#def __init__(self):
class Calc:
    def __init__(self, position, positiontina, X, Y, Z):
        self.position = position
        self.positiontina = positiontina
        self.X = X
        self.Y = Y
        self.Z = Z

    def coordinates_mac(self):
        position = self.position

        macy = int(position / 16)
        macx = position - 16 * macy
        maccoord = (macx, macy)

        return maccoord

    def coordinates_tina(self):
        positiontina = self.positiontina

        tinay = int((positiontina) / 16)
        tinax = positiontina - 16 * tinay
        tinacoord = (tinax, tinay)

        return tinacoord

    def coordinates_items(self):
        X = self.X
        Y = self.Y
        Z = self.Z

        XY = int(X / 16)
        XX = X - 16 * XY
        YY = int(Y / 16)
        YX = X - 16 * YY
        ZY = int(Z / 16)
        ZX = X - 16 * ZY
        Xcoord = (XX, XY)
        Ycoord = (YX, YY)
        Zcoord = (ZX, ZY)

        return Xcoord, Ycoord, Zcoord




class Pygame:

    def __init__(maccoord, tinacoord, Xcoord, Ycoord, Zcoord):
        self.maccoord = maccoord
        self.tinacoord = tinacoord
        self.Xcoord = Xcoord
        self.Ycoord = Ycoord
        self.zcoord = Zcoord

    def mapping():
        pygame.init()
        window = pygame.display.set_mode((480, 480), RESIZABLE)

def open_map():
    with open("maplabyrinthe.txt") as file:
        maps = file
        maps = maps.read()
        #print(maps)
        maps = list(maps)
        return maps

def random_count(maps):
    i = 0
    j = 0    
    space_count = 0
    space_list = []
    wall_list = []
    maps = list(maps)

    while i != len(maps):
            if maps[i] == " ":
                space_list.append(i)
                i = i + 1
            elif maps[i] == "#":
                wall_list.append(i)
                i = i + 1
            else:
                i = i + 1
    return space_list

def main():
    maps = open_map()
    space_list = random_count(maps)
    position = Characters(maps).mc_position()
    positiontina = Characters(maps).tina_position()
    X, Y, Z = Items(maps, space_list).item_position()
    #print(Items(maps, space_list).item_coord())
    print("".join(maps))
    while 1:
        move = entry.entry_user()
        position = Characters(maps).mc_position()
        tina = Tina(X, Y, Z, maps).tina_ready()
        Motion(maps, position, move, tina).direction()
        position = Characters(maps).mc_position()
        #print(position)
        X, Y, Z = Collect(position, X, Y, Z).collect_items()
        print(Calc(position, positiontina, X, Y, Z).coordinates_mac())


main()