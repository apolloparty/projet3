import random

def mapping():
    with open("maplabyrinthe.txt") as m:
        maps = m.read()
        return maps

def items():
        maps = mapping()
        i = 0
        f = 0
        space_count = 0
        space_list = ""
        space_list = list(space_list)
        maps = list(maps)
        #randomisation 
        while i != 305:
                if maps[i] == " ":
                        space_list.append(i)
                        i = i + 1
                else:
                        i = i + 1
        space_rand = random.randint(0, len(space_list) - 1)
        X = space_list[space_rand]
        maps[X] = "X"
        space_rand = random.randint(0, len(space_list) - 1)
        Y = space_list[space_rand]
        maps[Y] = "Y"
        space_rand = random.randint(0, len(space_list) - 1)
        Z = space_list[space_rand]
        maps[Z] = "Z"
        #item_position = [value_x, value_y, value_z]
        maps = "".join(maps)
        maps = list(maps)
        return maps, X, Y, Z

def motion():
    maps, X, Y, Z = items()
    maps = "".join(maps)
    #print(item_position)
    print(maps)
    maps = list(maps)

    while 1:
        move = input('Entrez ZQSD pour vous déplacer : ')
        position = maps.index("M")

        if move == "Z" or move == "z":
            if maps[position - 18] == " ":
                maps[position - 18] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
            elif maps[position - 18] == maps[X] or maps[position - 18] == maps[Y] or maps[position - 18] == maps[Z]:
                maps[position - 18] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
            else:
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
        if move == "S" or move == "s":
            if maps[position + 18] == " ":
                maps[position + 18] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
            elif maps[position + 18] == maps[X] or maps[position + 18] == maps[Y] or maps[position + 18] == maps[Z]:
                maps[position + 18] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
            else:
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
        if move == "D" or move == "d":
            if maps[position + 1] == " ":
                maps[position + 1] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
            elif maps[position + 1] == maps[X] or maps[position + 1] == maps[Y] or maps[position + 1] == maps[Z]:
                maps[position + 1] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
            else:
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
        if move == "Q" or move == "q":
            if maps[position - 1] == " ":
                maps[position - 1] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
            elif maps[position - 1] == maps[X] or maps[position - 1] == maps[Y] or maps[position - 1] == maps[Z]:
                maps[position - 1] = "M"
                maps[position] = " "
                maps = "".join(maps)
                print(maps)
                maps = list(maps)
            else:
                maps = "".join(maps)
                print(maps)
                maps = list(maps)

mapping()
items()
motion()