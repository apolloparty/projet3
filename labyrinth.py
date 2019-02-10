import random
import pygame
from pygame.locals import *

class Input_user:

    def __init__(self):
        self.move = ""

    def entry_user(self):
        move = self.move
        move = input("Entrez ZQSD pour vous déplacer : ")
        return move

    def entry_raw(self):
        move = self.move
        passing = 1
        while passing == 1:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        move = "s"
                        return move
                    if event.key == K_z:
                        move = "z"
                        return move
                    if event.key == K_d:
                        move = "d"
                        return move
                    if event.key == K_q:
                        move = "q"
                        return move
                if event.type == QUIT:
                    passing = 0

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
                direction = (0, 0)
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
        print(X, Y, Z)
        return X, Y, Z

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
        maccoord = (macx * 32, macy * 32)

        return maccoord

    def coordinates_tina(self):
        positiontina = self.positiontina

        tinay = int((positiontina) / 16)
        tinax = positiontina - 16 * tinay
        tinacoord = (tinax * 32, tinay * 32)

        return tinacoord

    def coordinates_items(self):
        X = self.X
        Y = self.Y
        Z = self.Z

        XY = int(X / 16)
        XX = X - 16 * XY
        YY = int(Y / 16)
        YX = Y - 16 * YY
        ZY = int(Z / 16)
        ZX = Z - 16 * ZY
        Xcoord = (XX * 32, XY * 32)
        Ycoord = (YX * 32, YY * 32)
        Zcoord = (ZX * 32, ZY * 32)

        return Xcoord, Ycoord, Zcoord

class Pygame:

    def __init__(self, maps, maccoord, tinacoord, Xcoord, Ycoord, Zcoord):
        self.maps = maps
        self.maccoord = maccoord
        self.tinacoord = tinacoord
        self.Xcoord = Xcoord
        self.Ycoord = Ycoord
        self.Zcoord = Zcoord
        self.mapping()

    def mapping(self):
        maps = self.maps
        i = 0
        j = 0

        pygame.init()
        window = pygame.display.set_mode((480, 480), RESIZABLE)
        space = pygame.image.load("ressource/espace.png").convert()
        position_space = space.get_rect()
        wall = pygame.image.load("ressource/mur.png").convert()
        position_wall = wall.get_rect()
        while i != 239:
            if maps[i] == " ":
                window.blit(space, ((i - (16 * j)) * 32, j * 32))
                #pygame.display.flip()
                i = i + 1
            elif maps[i] == "#":
                window.blit(wall, ((i - (16 * j)) * 32, j * 32))
                #pygame.display.flip()
                i = i + 1
            elif maps[i] == "\n":
                j = j + 1
                i = i + 1
            else:
                i = i + 1
        return window, space

    def item_display(self, window):
        Xcoord = self.Xcoord
        Ycoord = self.Ycoord
        Zcoord = self.Zcoord

        itemX = pygame.image.load("ressource/item1.png").convert_alpha()
        disX = itemX.get_rect()
        window.blit(itemX, Xcoord)
        itemY = pygame.image.load("ressource/item2.png").convert_alpha()
        disY = itemY.get_rect()
        window.blit(itemY, Ycoord)
        itemZ = pygame.image.load("ressource/item3.png").convert_alpha()
        disZ = itemZ.get_rect()
        window.blit(itemZ, Zcoord)
        pygame.display.flip()
    
    def mac_display(self, window, space):
        maccoord = self.maccoord

        mac = pygame.image.load("ressource/MacGyver.png").convert_alpha()
        mactemp = mac.get_rect()
        window.blit(space, mactemp)
        mactemp = mactemp.move(0, 32)
        window.blit(mac, mactemp)
        pygame.display.flip()

        #return position_space, position_wall, disX, disY, disZ
    
    #def graphics(self, position_space, position_wall, disX, disY, disZ):



def open_map():
    with open("maplabyrinthe.txt") as file:
        maps = file
        maps = maps.read()
        #print(maps)
        maps = list(maps)
        return maps

def random_count(maps):
    i = 0
    #j = 0    
    #space_count = 0
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
    return space_list, wall_list

def main():
    maps = open_map()
    space_list, wall_list = random_count(maps)
    position = Characters(maps).mc_position()
    positiontina = Characters(maps).tina_position()
    X, Y, Z = Items(maps, space_list).item_position()
    Xcoord, Ycoord, Zcoord = Calc(position, positiontina, X, Y, Z).coordinates_items()
    maccoord = Calc(position, positiontina, X, Y, Z).coordinates_mac()
    tinacoord = Calc(position, positiontina, X, Y, Z).coordinates_tina()
    window, space = Pygame(maps, maccoord, tinacoord, Xcoord, Ycoord, Zcoord).mapping()
    #print(Items(maps, space_list).item_coord())
    print("".join(maps))
    while 1:
        #move = Input_user().entry_user()
        Pygame(maps, maccoord, tinacoord, Xcoord, Ycoord, Zcoord).mac_display(window, space)
        Pygame(maps, maccoord, tinacoord, Xcoord, Ycoord, Zcoord).item_display(window)
        #Pygame(maps, maccoord, tinacoord, Xcoord, Ycoord, Zcoord).item_display(window)
        move = Input_user().entry_raw()
        position = Characters(maps).mc_position()
        tina = Tina(X, Y, Z, maps).tina_ready()
        direction = Motion(maps, position, move, tina).direction()
        position = Characters(maps).mc_position()
        #print(position)
        X, Y, Z = Collect(position, X, Y, Z).collect_items()
        print(Calc(position, positiontina, X, Y, Z).coordinates_mac())


main()