import random
import pygame
from pygame.locals import *
from itertools import chain

class Input_user:
    def __init__(self):
        pass

    def entry_user(self):
        move = input("Entrez ZQSD pour vous déplacer : ")
        return move

    def entry_raw(self):
        pygame.init()
        move = ""
        passing = 1
        while passing == 1:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        move = "s"
                    if event.key == K_z:
                        move = "z"
                    if event.key == K_d:
                        move = "d"
                    if event.key == K_q:
                        move = "q"
                    return move
                if event.type == QUIT:
                    quit()

class Character:
    def __init__(self):
        pass

    def mcgyver(self, maps):
        mcgyver_position = []
        macX = 0
        macY = 0
        x = 0
        y = 0
        continuer = 1

        while continuer == 1:
            if maps[y][x] != "M":
                if y == 14 and x == 14:
                    break
                if x == 14:
                    x = 0
                    y = y + 1
                else:
                    x = x + 1
            if maps[y][x] == "M":
                macX = x
                macY = y
                mcgyver_position.insert(0, ((macX, macY)))
                continuer = 0
        mcgyver_position = mcgyver_position[0]
        print(mcgyver_position)
        return mcgyver_position, macX, macY

class Motion:
    def __init__(self):
        pass
    
    def check_direction(self, move, macY, macX, maps, collect):
        if move == "z":
            if macY == 0:
                pass
            elif maps[macY - 1][macX] == "X" or maps[macY - 1][macX] == "Y" or maps[macY - 1][macX] == "Z":
                maps[macY][macX] = " "
                maps[macY - 1][macX] = "M"
            elif maps[macY - 1][macX] == " ":
                maps[macY][macX] = " "
                maps[macY - 1][macX] = "M"
        if move == "s":
            if macY == 14:
                pass
            elif maps[macY + 1][macX] == "X" or maps[macY + 1][macX] == "Y" or maps[macY + 1][macX] == "Z":
                maps[macY][macX] = " "
                maps[macY + 1][macX] = "M"
            elif maps[macY + 1][macX] == " ":
                maps[macY][macX] = " "
                maps[macY + 1][macX] = "M"
        if move == "q":
            if macX == 0:
                pass
            elif maps[macY][macX - 1] == "X" or maps[macY][macX - 1] == "Y" or maps[macY][macX - 1] == "Z":
                maps[macY][macX] = " "
                maps[macY][macX - 1] = "M"
            elif maps[macY][macX - 1] == "T":
                if collect == [1, 1, 1]:
                    maps[macY][macX] = " "
                    maps[macY][macX - 1] = "M"
            elif maps[macY][macX - 1] == " " and maps[macY][macX - 1] != "T":
                maps[macY][macX] = " "
                maps[macY][macX - 1] = "M"
        if move == "d":
            if macX == 14:
                pass
            elif maps[macY][macX + 1] == "X" or maps[macY][macX + 1] == "Y" or maps[macY][macX + 1] == "Z":
                maps[macY][macX] = " "
                maps[macY][macX + 1] = "M"
            elif maps[macY][macX + 1] == " ":
                maps[macY][macX] = " "
                maps[macY][macX + 1] = "M"
        for line in maps:
            print(line)
            
            
class Labyrinth:
    def __init__(self):
        pass

    def open_map(self):
        maps = []
        x = 0
        y = 1
        with open("maplabyrinthe.txt") as file:
            for line in file:
                map_line = []
                for char in line:
                    if char != "\n":
                        map_line.append(char)
                        x = x + 1
                    else:
                        y = y + 1
                maps.append(map_line)
        #for line in maps:
           #print(line)
        return maps

    def register_fixed(self, maps):
        space_list = []
        wall_list = []
        tina_position = []
        continuer = 1
        x = 0
        y = 0

        while continuer == 1:
            if maps[y][x] == " ":
                if x == 14 and x != 0 and y != 14:
                    space_list.append((x, y))
                    y = y + 1
                    x = 0
                if maps[y][x] == " ":
                    space_list.append((x, y))
                if maps[y][x] == "#":
                    wall_list.append((x, y))
                x = x + 1
            if maps[y][x] == "#":
                if x == 14 and x != 0 and y != 14:
                    wall_list.append((x, y))
                    y = y + 1
                    x = 0
                if maps[y][x] == "#":
                    wall_list.append((x, y))
                if maps[y][x] == " ":
                    space_list.append((x, y))
                x = x + 1
            if maps[y][x] == "T":
                tina_position.append((x, y))
                x = x + 1
            if maps[y][x] == "M":
                x = x + 1
            if y == 14 and x == 14:
                wall_list.append((x, y))
                continuer = 0
        return space_list, wall_list, tina_position

class Items:
    def __init__(self):
        pass

    def items_position(self, space_list, maps):
        item_list = []

        space_rand = random.randint(0, len(space_list) - 1)
        item_list.append(space_list[space_rand])
        space_rand = random.randint(0, len(space_list) - 1)
        item_list.append(space_list[space_rand])
        space_rand = random.randint(0, len(space_list) - 1)
        item_list.append(space_list[space_rand])
        item_coord = list(chain.from_iterable(item_list))
        list1, list2 = zip(*item_list)
        maps[list2[0]][list1[0]] = "X"
        maps[list2[1]][list1[1]] = "Y"
        maps[list2[2]][list1[2]] = "Z"
        item_coord = item_list[1]

        return item_list, maps

class Collect:
    def __init__(self):
        pass

    def check_items(self, item_list, mcgyver_position, tina_position, collect):
        if mcgyver_position == item_list[0]:
            collect[0] = 1
        if mcgyver_position == item_list[1]:
            collect[1] = 1
        if mcgyver_position == item_list[2]:
            collect[2] = 1
        print(collect)

        return collect

    def check_win(self, mcgyver_position, tina_position, window):
        ending = pygame.image.load("ressource/Victoire.png").convert()
        victory = ending.get_rect()
        if tuple(mcgyver_position) == tuple(tina_position[0]):
            print("YOU WON")
            while 1:
                for event in pygame.event.get():
                    window.blit(ending, (0, 0))
                    pygame.display.flip()
                    if event.type == KEYDOWN:
                        if event.key == K_q:
                            quit()

class Pygame:
    def init(self):
        pass

    def unmovable(self, maps, wall_list, space_list):
        i = 0
        j = 0

        pygame.init()
        window = pygame.display.set_mode((480, 480), RESIZABLE)
        wall = pygame.image.load("ressource/mur.png").convert()
        pwall = wall.get_rect()
        while i != len(wall_list):
            window.blit(wall, tuple(32*x for x in wall_list[i]))
            i = i + 1
        space = pygame.image.load("ressource/espace.png").convert()
        pspace = space.get_rect()
        while j != len(space_list):
            window.blit(space, tuple(32*x for x in space_list[j]))
            j = j + 1
        pygame.display.flip()
        return window, space
    
    def movable(self, window, maps, item_list, tina_position):
        itemX = pygame.image.load("ressource/item1.png").convert_alpha()
        pX = itemX.get_rect()
        window.blit(itemX, tuple(32*x for x in item_list[0]))
        itemY = pygame.image.load("ressource/item2.png").convert_alpha()
        pY = itemY.get_rect()
        window.blit(itemY, tuple(32*x for x in item_list[1]))
        itemZ = pygame.image.load("ressource/item3.png").convert_alpha()
        pZ = itemZ.get_rect()
        window.blit(itemZ, tuple(32*x for x in item_list[2]))
        itemtina = pygame.image.load("ressource/Gardien.png").convert_alpha()
        ptina = itemtina.get_rect()
        window.blit(itemtina, tuple(32*x for x in tina_position[0]))
        pygame.display.flip()
    
    def display_mac(self, window, mcgyver_position, space):
        mac = pygame.image.load("ressource/MacGyver.png").convert()
        pmac = mac.get_rect()
        window.blit(mac, tuple(32*x for x in mcgyver_position))
        pygame.display.flip()
        window.blit(space, tuple(32*x for x in mcgyver_position))

def main():
    collect = [0, 0, 0]
    maps = Labyrinth().open_map()
    space_list, wall_list, tina_position = Labyrinth().register_fixed(maps)
    item_list, maps = Items().items_position(space_list, maps)
    window, space = Pygame().unmovable(maps, wall_list,space_list)
    Pygame().movable(window, maps, item_list, tina_position)
    for line in maps:
        print(line)
    while 1:
        mcgyver_position, macX, macY = Character().mcgyver(maps)
        Collect().check_win(mcgyver_position, tina_position, window)
        Pygame().display_mac(window, mcgyver_position, space)
        move = Input_user().entry_raw()
        collect = Collect().check_items(item_list, mcgyver_position, tina_position, collect)
        Motion().check_direction(move, macY, macX, maps, collect)

main()