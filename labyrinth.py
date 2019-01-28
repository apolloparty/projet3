import random

class Input_user:

    def __init__(self):
        self.move = ""

    def entry_user(self):
        self.move = input("Entrez ZQSD pour vous déplacer : ")
        return self.move

entry = Input_user()

class Mcgyver:

    def __init__(self, maps):
        self.maps = maps
    
    def mc_position(self):
        position = self.maps.index("M")
        #print(position)
        return position
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


def open_map():
    with open("maplabyrinthe.txt") as file:
        maps = file
        maps = maps.read()
        #print(maps)
        maps = list(maps)
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
    return space_list

def main():
    maps = open_map()
    space_list = random_count(maps)
    X, Y, Z = Items(maps, space_list).item_position()
    print("".join(maps))
    while 1:
        move = entry.entry_user()
        position = Mcgyver(maps).mc_position()
        tina = Tina(X, Y, Z, maps).tina_ready()
        Motion(maps, position, move, tina).direction()
        position = Mcgyver(maps).mc_position()
        X, Y, Z = Collect(position, X, Y, Z).collect_items()
        #tina = Tina(X, Y, Z, maps).tina_ready()
        #print(position)
        #print(maps.index("M"))


main()
#Mcgyver()
#print(mac.input_user())