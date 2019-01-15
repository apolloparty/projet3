import random

def mapping():
    with open("maplabyrinthe.txt") as m:
        maps = m
        i = 0
        f = 0
        space_count = 0
        space_list = ""
        space_list = list(space_list)
        maps = maps.read()
        maps = list(maps)
        #randomisation 
        while i != 305:
                if maps[i] == " ":
                        space_list.append(i)
                        i = i + 1
                else:
                        i = i + 1
        space_rand = random.randint(0, len(space_list) - 1)
        value_x = space_list[space_rand]
        maps[value_x] = "X"
        space_rand = random.randint(0, len(space_list) - 1)
        value_y = space_list[space_rand]
        maps[value_y] = "Y"
        space_rand = random.randint(0, len(space_list) - 1)
        value_z = space_list[space_rand]
        maps[value_z] = "Z"
        item_position = (value_x, value_y, value_z)
        print(item_position)
        maps = "".join(maps)
        print(maps)

        #maps = "".join(maps) #permet de replacer correctement la str 
        #position = maps.index("M")
        
        #maps[position - 18] = "M" #déplacement vers le haut
        #maps[position+1] = "M" #déplacement vers la droite
        #maps[position-1] = "M" #déplacement vers la gauche
        #maps[position + 18] = "M" #déplacement vers le bas 
        #maps[position] = " "
        #maps = "".join(maps)
        #print(maps)
        # map = map.replace('M', " ")
        # map = map.replace(map[29], "M")
        #print(maps)
        #while maps[i] != '\n':
        #        i = i + 1
        #        pass
        #print(i)
        #print(map)


mapping()