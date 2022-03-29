def move(state, direction):
    lst_jg = []
    posible_abajo = False
    left_possible = False
    derecha_posible = False
    arriba_posible = False
    mov_dps = []
    jgdr = 0

    for s in state:
        lista_temp = []
        lista_temp[:0] = s
        lst_jg.append(lista_temp)

    if lst_jg !=[]:
        pass
    else:
        raise Warning ("Game state cannot be empty.")
    
    para_each_l_len = len(lst_jg[0])
    
    #test the game state input
    for l in lst_jg:
        if len(l) == para_each_l_len:
            pass
        else:
            raise Warning ("Each line in the game state has to be the same length.")
        for let in l:
            if " " in let or "#" in let or "o" in let:
                if "o" in let:
                    jgdr += 1
                    if jgdr == 1:
                        pass
                    else:
                        raise Warning ("Just one player per game")
            else:
                raise Warning (f"invalid character: {let}")
    if jgdr == 1:
        pass
    elif jgdr == 0:
        raise Warning("There are no players")
    else:
        raise Warning ("You must have one player per game")


    pos_jgdr = get_jgdr_pos(lst_jg)
    h_len = len(lst_jg[0])
    v_len = len(lst_jg)

    if pos_jgdr[0] > 0 and pos_jgdr[0] < v_len - 1 and pos_jgdr[1] < h_len - 1 and pos_jgdr[1] > 0:

        if " " in lst_jg[pos_jgdr[0] - 1][pos_jgdr[1]]:
            ("move up: ok")
            arriba_posible = True
        if " " in lst_jg[pos_jgdr[0] + 1][pos_jgdr[1]]:
            ("move down: ok")
            posible_abajo = True
        if " " in lst_jg[pos_jgdr[0]][pos_jgdr[1] + 1]:
            ("move right: ok")
            derecha_posible = True
        if " " in lst_jg[pos_jgdr[0]][pos_jgdr[1] - 1]:
            ("move left: ok")
            left_possible = True

        move_dir = direction
        lst_jg[pos_jgdr[0]][pos_jgdr[1]] = " "

        if "up" in move_dir and arriba_posible:
            lst_jg[pos_jgdr[0] - 1][pos_jgdr[1]] = "o"
        elif "down" in move_dir and posible_abajo:
            lst_jg[pos_jgdr[0] + 1][pos_jgdr[1]] = "o"
        elif "left" in move_dir and left_possible:
            lst_jg[pos_jgdr[0]][pos_jgdr[1] - 1] = "o"
        elif "right" in move_dir and derecha_posible:
            lst_jg[pos_jgdr[0]][pos_jgdr[1] + 1] = "o"
        else:
            raise Warning ("Move is not a valid")
    else:

        if pos_jgdr[1] == 0 and pos_jgdr[0] == 0:
            posible_abajo = True
            derecha_posible = True
            if "down" in direction and posible_abajo:
                lst_jg[pos_jgdr[0] + 1][pos_jgdr[1]] = "o"
            elif "right" in direction and derecha_posible:
                lst_jg[pos_jgdr[0]][pos_jgdr[1] + 1] = "o"
            else:
                raise Warning ("Move is not a valid")
        elif pos_jgdr[1] == len(lst_jg[0]) - 1 and pos_jgdr[0] == 0:
            posible_abajo = True
            left_possible = True
            if "down" in direction and posible_abajo:
                lst_jg[pos_jgdr[0] + 1][pos_jgdr[1]] = "o"
            elif "left" in direction and left_possible:
                lst_jg[pos_jgdr[0]][pos_jgdr[1] - 1] = "o"
            else:
                raise Warning ("Move is not a valid")
        elif pos_jgdr[0] == len(lst_jg) - 1 and pos_jgdr[1] == 0:
            arriba_posible = True
            derecha_posible = True
            if "up" in direction and arriba_posible:
                lst_jg[pos_jgdr[0] - 1][pos_jgdr[1]] = "o"
            elif "right" in direction and derecha_posible:
                lst_jg[pos_jgdr[0]][pos_jgdr[1] + 1] = "o"
            else:
                raise Warning ("Move is not a valid")
        elif pos_jgdr[0] == len(lst_jg) - 1 and pos_jgdr[1] == len(lst_jg[0]) - 1:
            arriba_posible = True
            left_possible = True
            if "up" in direction and arriba_posible:
                lst_jg[pos_jgdr[0] - 1][pos_jgdr[1]] = "o"
            elif "left" in direction and left_possible:
                lst_jg[pos_jgdr[0]][pos_jgdr[1] - 1] = "o"
            else:
                raise Warning ("Move is not a valid")
        elif pos_jgdr[0] == len(lst_jg) - 1:
            if "down" in direction:
                raise Warning ("Down: not a valid move")
        elif pos_jgdr[0] == 0:
            if "up" in direction:
                raise Warning ("Up: not a valid move")
        elif pos_jgdr[1] == len(lst_jg[0]) - 1:
            if "right" in direction:
                raise Warning ("Right: not a valid move")
        elif pos_jgdr[1] == 0:
            if "left" in direction:
                raise Warning ("Left: not a valid move")

    pos_new_jgdr = get_jgdr_pos(lst_jg)
    
    if pos_new_jgdr[0] > 0 and pos_new_jgdr[0] < v_len -1 and pos_new_jgdr[1] < h_len -1 and pos_new_jgdr[1] > 0:
    
        if " " in lst_jg[pos_new_jgdr[0] - 1][pos_new_jgdr[1]]:
            mov_dps.append("up")
            ("New move up possible")
        if " " in lst_jg[pos_new_jgdr[0] + 1][pos_new_jgdr[1]]:
            mov_dps.append("down")
            ("New move down possible")
        if " " in lst_jg[pos_new_jgdr[0]][pos_new_jgdr[1] + 1]:
            mov_dps.append("right")
            ("New move right possible")
        if " " in lst_jg[pos_new_jgdr[0]][pos_new_jgdr[1] - 1]:
            mov_dps.append("left")
            ("New move left possible")

    sort_list_dps = sorted(mov_dps)
    mov_dps_tup = tuple(sort_list_dps)

    lst_fnl = []
    lista_ = []
    for s in lst_jg:
        joined_s = "".join(s)
        lst_fnl.append(joined_s)
    for l in lst_fnl:
        joined_l = "".join(l)
        lista_.append(joined_l)

    fnl_tup = tuple(lista_)
    tup_fnl = (fnl_tup, mov_dps_tup)

    return tup_fnl

def get_jgdr_pos(lst_state):
    v_lay = 0
    jgdr_i = 0
    for i in lst_state:
        if "o" in i:
            v_lay = lst_state.index(i)
        for index, value in enumerate(i):
            #print(index, value)
            if value == "o":
                jgdr_i = index
    jgdr_pos = [v_lay, jgdr_i]

    return jgdr_pos

# value to the Console.
s1 = (
    "######  ",
    "### o  #",
    "#     ##",
    "    ####"
)
s2 = move(s1, "down")
#print(s2)

print("= New State =")
print("\n".join(s2[0]))
print("\nPossible Moves: {}".format(s2[1]))