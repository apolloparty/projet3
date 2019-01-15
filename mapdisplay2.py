import random

def mapping():
    with open("maplabyrinthe.txt") as m:
        maps = m.read()
        #print(maps)
        #maps = list(maps)
        return maps

def items():
    #with open("maplabyrinthe.txt") as m:
        maps = mapping()
        i = 0
        f = 0
        space_count = 0
        space_list = ""
        space_list = list(space_list)
        #maps = maps.read()
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
        item_position = (X, Y, Z)
        item_position = list(item_position)
        maps = "".join(maps)
        maps = list(maps)
        return maps, item_position

def motion():
    j = 0
    maps, item_position = items()
    maps = "".join(maps)
    print(maps)
    maps = list(maps)
    print(item_position)

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
            elif move == "Z" or move == "z":
                maps[position - 18] == maps[item_position[[1], [2], [3]]]
                maps[position - 18] = "M"
                j = j + 1
                print(j)
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
            elif move == "S" or move == "s":
                maps[position - 18] == maps[item_position[[1], [2], [3]]]
                maps[position + 18] = "M"
                j = j + 1
                print(j)
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
            elif move == "D" or move == "d":
                maps[position - 18] == maps[item_position[[1], [2], [3]]]
                maps[position + 1] = "M"
                j = j + 1
                print(j)
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
            elif move == "Q" or move == "q":
                maps[position - 18] == maps[item_position[[1], [2], [3]]]
                maps[position - 1] = "M"
                j = j + 1
                print(j)
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