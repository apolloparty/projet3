import random

class Map_init:
    
    def __init__(self, maps, space_list):
            self.maps = maps
            self.space_list = space_list
    
    def items_position(self):
        space_rand = random.randint(0, len(self.space_list) - 1)
        X = self.space_list[space_rand]
        self.maps[X] = "X"
        space_rand = random.randint(0, len(self.space_list) - 1)
        Y = self.space_list[space_rand]
        self.maps[Y] = "Y"
        space_rand = random.randint(0, len(self.space_list) - 1)
        Z = self.space_list[space_rand]
        self.maps[Z] = "Z"
        #item_position = [value_x, value_y, value_z]
        self.maps = "".join(self.maps)
        #self.maps = list(self.maps)
        print(self.maps)

class Motion:

    def __init__(self, move, maps):
        self.move = move
        self.maps = maps

    def input_user(self):
        if self.move == "Z" or self.move == "z":
            if self.maps[position - 16] == " ":
                self.maps[position - 16] = "M"
                self.maps[position] = " "
                self.maps = "".join(self.maps)
                print(self.maps)
                self.maps = list(self.maps)
            elif self.maps[position - 16] == self.maps[X] or self.maps[position - 16] == self.maps[Y] or self.maps[position - 18] == self.maps[Z]:
                self.maps[position - 16] = "M"
                self.maps[position] = " "
                self.maps = "".join(self.maps)
                print(self.maps)
                self.maps = list(self.maps)
            else:
                self.maps = "".join(self.maps)
                print(self.maps)
                self.maps = list(self.maps)

    def mac(self):
        position = maps.index("M")

def open_map():
        with open("maplabyrinthe.txt") as m:
            maps = m.read()
            return maps

def random_count(maps):
    i = 0
    f = 0    
    space_count = 0
    space_list = ""
    space_list = list(space_list)
    maps = list(maps)
    while i != 239:
            if maps[i] == " ":
                    space_list.append(i)
                    i = i + 1
            else:
                        i = i + 1
    return maps, space_list

def motion_value():
    move = input("Entrez ZQSD pour vous déplacer : ")
    return move


def main():
    maps = open_map()
    maps, space_list = random_count(maps)
    move = motion_value()
    motion = Motion(move, maps)
    mapping = Map_init(maps, space_list)
   #print(mapping.items_position())
    print(motion.input_user())

main()