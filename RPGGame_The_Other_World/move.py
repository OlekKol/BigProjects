import keyboard
import os
import math
import time
import moving_between_files
import choice
# from jufen import Jufen
# J = Jufen
F = moving_between_files

class Move():
    def __init__(self) -> None:
        pass
    def map_whole(self):
        
        
        def gen_map(mapa, dim_x, dim_y):    
            for y in range(dim_y):
                line = []
                for x in range(dim_x):
                    line.append('0')
                mapa.append (line)
                
        def gen_square(mapa, x1, y1, x2, y2, kind):
            # w --> woods
            # m --> mountains
            n = 0
            
            if kind == "f":
                n += 1
            elif kind == "m":
                n += 2
            elif kind == 'w':
                n += 3
            elif kind == 'b':
                n += 4
            elif kind == 'r':
                n += 5
            elif kind == 's':
                n += 6
                
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    mapa[y][x] = str(n)
                    
        def gen_diamond(mapa, x, y, r, kind):
            n = 0
            if kind == "f":
                n += 1
            elif kind == "m":
                n += 2
            elif kind == 'w':
                n += 3    
            
            c = 0
            ungli = 0
            remainder = 0
            for y_ in range ((y - r),(y + r + 1)):
                c = remainder
                for x_ in range ((x - c),(x + c + 1)):
                
                    mapa[y_][x_] = str(n)
                
                    c += 1
                if remainder < r and ungli <= 0:
                    remainder += 1
                    
                else:
                    ungli += 1
                    remainder -= 1
                    
        def print_map(mapa):
            for w in range(len(mapa)):
                line = ''
                for k in range(len(mapa[w])):
                    line += mapa[w][k]
                print(line)
        
        def gen_special(mapa, x, y, kind):
            n = 0
            if kind == '0':
                n == '0'
            if kind == "f":
                n += 1
            elif kind == "m":
                n += 2
            elif kind == 'w':
                n += 3
            elif kind == 'b':
                n += 4
            elif kind == 'r':
                n += 5
            elif kind == 's':
                n += 6
                
            mapa[y][x] = str(n)
        
        def gen_special2(mapa, x, y, kind:str):
            mapa[y][x] = str(kind)
            
        def gen_castle(mapa, x, y, name):
            for y_ in range(y - 1, y + 2):
                for x_ in range(x - 1, x + 2): 
                    mapa[y_][x_] = str('C')
                    if y_ == y - 1 and x_ == x:
                        mapa[y_][x_] = str('0')
                    elif y_ == y + 1 and x_ == x:
                        mapa[y_][x_] = str(name)

        def gen_dungeon(mapa, x, y, name):
            # x y __________________
            # |NAME                 |
            # |                     |
            # |                     |
            # |                     |
            # |                     |
            # -----------------------
        
            for y_ in range(y, y + 6):
                for x_ in range(x, x + 8):
                        mapa[y_][x_] = str('C')
                        if y_ == y + 2 and x_ == x + 3:
                            mapa[y_][x_] = str('E' + name[0])
                        elif y_ == y + 2 and x_ == x + 4:
                            mapa[y_][x_] = str('E' + name[0])
                        elif y_ >= y + 3 and x_ >= x + 2 and x_ <= x + 5:
                            mapa[y_][x_] = str('E' + name[0])
                        elif y_ == y and x_ == x:
                            mapa[y_][x_] = str(name[0])
        

        def gen_moutains(mapa, x1 ,y1 ,x2, kind, up_or_down):
            n = 0
            if kind == "f":
                n += 1
            elif kind == "m":
                n += 2
            elif kind == 'w':
                n += 3
                
            if up_or_down == 'u':
                i = 0
                ix = 0
                while i >= (-x2 + x1):
                    if i != 0 and (i + 1)%3 == 0 or i==1:
                        for y in range(y1 + i -6 - 1 ,y1 + i ):
                            for x in range(x1 + ix, x1 + ix + 1):
                                mapa[y][x] = str(n)
                    else:
                        for y in range(y1 + i - 4 - 1,y1 + i):
                            for x in range(x1 + ix, x1 + ix + 1):
                                mapa[y][x] = str(n)
                    i -= 1
                    ix += 1
                
            else:

                i = 0
                
                while i <= (x2 - x1):
                    if i != 0 and ((i*-1) +1 )%3 == 0 or i==1:
                        for y in range(y1 + i - 2, y1 + i + 6 - 1):
                            for x in range(x1 + i, x1 + i + 1):
                                mapa[y][x] = str(n)
                    
                    else:
                        for y in range(y1 + i, y1 + i + 4 + 1):
                            for x in range(x1 + i, x1 + i + 1):
                                mapa[y][x] = str(n)
                    i += 1
        
        def gen_triangle_r(mapa, x1, y1, x2, y2, kind, stair_or_roof):
            # ------x2 y2
            # |    /|
            # |   / |
            # |  /  |
            # | /   |
            #x1 y1 ---
            n = 0
            if kind == "f":
                n += 1
            elif kind == "m":
                n += 2
            elif kind == 'w':
                n += 3
            i = 0
            l = x2 - x1
            if stair_or_roof == 's':
                for y in range (y2, y1 + 1 ):
                    i = 0
                    for x in range (x1, x2 + 1):
                        if i >= l:
                            mapa[y][x] = str(n)
                        i += 1
                    l -= 1
            else:
                l = 0
                for y in range (y2, y1 + 1 ):
                    i = x2 - x1
                    for x in range (x1, x2 + 1):
                        if i >= l:
                            mapa[y][x] = str(n)
                        i -= 1
                    l += 1
        def gen_triangle_l(mapa, x1, y1, x2, y2, kind, stair_or_roof):
            n = 0
            if kind == "f":
                n += 1
            elif kind == "m":
                n += 2
            elif kind == 'w':
                n += 3
            
            i = 0
            l = 0
            
            if stair_or_roof == 's':
                l = 0
                for y in range (y1, y2 + 1 ):
                    i = 0
                    for x in range (x1, x2 + 1):
                        if i <= l:
                            mapa[y][x] = str(n)
                        i += 1
                    l += 1
                
            else:
                for y in range (y1, y2 + 1 ):
                    i = 0
                    for x in range (x1, x2 + 1):
                        if i >= l:
                            mapa[y][x] = str(n)
                        i += 1
                    l += 1
            
        def specials(map, x, y):
            r = [0]
            being_checked = ['J', 'K', 'S']
            for i in range (0,len(being_checked)):
                if map[y][x] == being_checked[i]:
                    r = being_checked[i]
                    return r
            being_checked = ['EV', 'EL', 'EH']
            for i in range (0,len(being_checked)):
                if map[y][x] == being_checked[i]:
                    r = being_checked[i]
                    return r
            return r
            
        def kingdom_uncoder(u):
            print(u)
            if u == 'J' or u == 'j':
                return mapJ
            if u == 'K' or u == 'k':
                return mapK
            if u == 'S' or u == 's':
                return mapS
        def dungeon_uncoder(u):
            if u == 'H' or u == 'h':
                return mapH
            if u == 'L' or u == 'l':
                return mapL
            if u == 'V' or u == 'v':
                return mapV
        def move_speed_next_move_checker(mapac, x, y, if_in_dungeon, rd):
            
            
            if mapac == mapa:
                if mapac[y][x] == '1':
                    return 2
                elif mapac[y][x]  == '3':
                    return 3
                elif mapac[y][x]  == '2':
                    return 4
                else:
                    return 1
            elif mapac == mapK or mapac == mapJ or mapac == mapS:
                if mapac[y][x]  == '5':
                    return 1
                elif mapac[y][x]  == 'tL':
                    return 9
                elif mapac[y][x][0]  == 'W' or mapac[y][x][0]  == 'M' or mapac[y][x][0]  == 'F' or mapac[y][x][0]  == 'T':
                    return 2
                else:
                    return 0
            elif if_in_dungeon == 1:
                
                if mapac[y][x]  == '8':
                    return 1
                elif mapac[y][x]  == 'tL':
                    return 9
                elif mapac[y][x][0] == 'I' or mapac[y][x][0] == 'V' or mapac[y][x][0] == 'X':
                    pims = mob_detector(mapac,x,y,rd - 1, '9')
                    if len(pims[0]) == 0:
                        return 8
                    else: return 0
                else: return 0
                
        def which_shop_enter_checker(mapac, x, y):
            i = 1
            if mapac[y][x][0]  == 'W':
                while i < 8:
                    if str(mapac[y][x][1]) == str(i):
                        return str (mapac[y][x][0]) + str(mapac[y][x][1])
                    i += 1
            elif mapac[y][x][0]  == 'M':
                while i < 8:
                    if str(mapac[y][x][1]) == str(i):
                        return str (mapac[y][x][0]) + str(mapac[y][x][1])
                    i += 1
            elif mapac[y][x][0]  == 'F':
                while i < 8:
                    if str(mapac[y][x][1]) == str(i):
                        return str (mapac[y][x][0]) + str(mapac[y][x][1])
                    i += 1
            elif mapac[y][x][0]  == 'T':
                while i < 8:
                    if str(mapac[y][x][1]) == str(i):
                        return str(mapac[y][x][0]) + str(mapac[y][x][1])
                    i += 1
                    
                    
                    
        def are_you_sure_about_the_purchase():
        
            Y_N = ['No', 'Yes']
            answer = choice.WybierzZListy(Y_N, 'Do you whant to buy this item? ')
            print (answer)
            return answer
                    
        def shop(which,p_eq, pm):
            def shop_display(display, price, players_money, kind):
                
                z = 0
                exit_1_buy_2 = 0
                it_is = 0
                while exit_1_buy_2 == 0:
                    os.system('clear')
                    once = 0
                    for i in range (0,len(display)):
                        if price == '1' or it_is == 1:
                            price = display[i][2]
                            it_is = 1
                            
                        if once == 0 and kind == 'F':
                            price_to_show = display[z][2]
                            print('')
                            print(f'money - {players_money} (of yours)')
                            print('')
                            print(f'money - {players_money - price_to_show} (of yours --> after the purchase !)')
                        elif once == 0:
                            print('')
                            print(f'money - {players_money} (of yours)')
                            print('')
                            print(f'money - {players_money - price} (of yours --> after the purchase !)')
                        print('')
                        if z == i:
                            print(f'-> {display[i], price}')
                        else:
                            print(f'   {display[i], price}')
                        if i == (len(display)):
                            print('')
                        once = 1
                    print('')
                    print('Enter - to buy')
                    print('')
                    print('x - to Leave')
                    print('')
                    print_(p_eq, 's', 's', 'E' , 0, '')
                    keyboard.read_key()
                    if keyboard.is_pressed('Up'):
                        if z > 0 :
                            z -= 1
                    elif keyboard.is_pressed('Down'):
                        if z < len(display) - 1:
                            z += 1
                    elif keyboard.is_pressed('x'):
                        exit_1_buy_2 += 1
                    elif keyboard.is_pressed('Enter'):
                        exit_1_buy_2 += 2
                        
                after_the_buying = ['nothing','nothing', players_money]
                
                
                
                if exit_1_buy_2 == 2:

                    if players_money >= price:
                        aysatp = are_you_sure_about_the_purchase()
                        if aysatp == 1:
                            players_money -= price
                            after_the_buying = [kind,[display[z][0], display[z][1]],players_money]
                            easier = [after_the_buying]
                            return easier
                return after_the_buying
            
            def Weapon_shop(which,players_money):
                lvl = int(which[1])
            
                lvlr = 'I'
                if lvl == 1:
                    lvlr ='I'
                if lvl == 2:
                    lvlr ='II'
                if lvl == 3:
                    lvlr ='III'
                if lvl == 4:
                    lvlr ='IV'
                if lvl == 5:
                    lvlr ='V'
                if lvl == 6:
                    lvlr ='VI'
                if lvl == 7:
                    lvlr ='VII'

                    
            #(I --> VII)Level  Name     Damage    RdSPD       Price
                # Sword = [lvlr,'Sword',{lvl*25}, {1/lvl}, {(lvl ** 2) * 10}]
                # Spear = [lvlr,'Spear',{lvl*100},{4/lvl}, {(lvl ** 2) * 10}]
                # Bow =   [lvlr,'Bow',  {lvl*50}, {2/lvl}, {(lvl ** 2) * 10}]
                # price = Sword[len(Sword) - 1]
                
                ################
                Sword = [lvlr,'Sword']
                Spear = [lvlr,'Spear']
                Bow =   [lvlr,'Bow']
                
                price = (lvl ** 2) * 10
                
                display = [Sword,Spear,Bow]
                kind = 'W'
                return shop_display(display, price, players_money, kind)
                
                
                    
                    
                
            
                
                    
            def Magic_shop(which, players_money):
                kind = 'M'
                
                lvl = int(which[1])
                
                # lvlr = 'I'
                # if lvl == 1:
                #     lvlr ='I'
                # #(I --> VII)Level  Name     Damage    Mana_needed       Price
                #     Water = [lvlr,'Teardrop',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Fire = [lvlr,'Snap_flame',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Earth = [lvlr,'Sand_throw',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Air = [lvlr,'Air_blow',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                # if lvl == 2:
                #     lvlr ='II'
                # if lvl == 3:
                #     lvlr ='III'
                #     Water = [lvlr,'Splash',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Fire = [lvlr,'Fire_trow',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Earth = [lvlr,'Quicksand',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Air = [lvlr,'Wind_blow',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                # if lvl == 4:
                #     lvlr ='IV'
                #     Water = [lvlr,'WaterBall',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Fire = [lvlr,'FireBall',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Earth = [lvlr,'EarthBall',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Air = [lvlr,'AirBall',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                # if lvl == 5:
                #     lvlr ='V'
                #     Water = [lvlr,'Wave',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Fire = [lvlr,'Dragon_breath',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Earth = [lvlr,'Earth_prison',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Air = [lvlr,'Air_shoes',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                # if lvl == 6:
                #     lvlr ='VI'
                # if lvl == 7:
                #     lvlr ='VII'
                #     Water = [lvlr,'Tsunami',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Fire = [lvlr,'Fire_Beam',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Earth = [lvlr,'Earthquake',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                #     Air = [lvlr,'Tornado',{lvl*25}, {lvl} * 100, {(lvl ** 2) * 10}]
                lvlr = 'I'
                if lvl == 1:
                    lvlr ='I'
                if lvl == 2:
                    lvlr ='II'
                if lvl == 3:
                    lvlr ='III'
                if lvl == 4:
                    lvlr ='IV'
                if lvl == 5:
                    lvlr ='V'
                if lvl == 6:
                    lvlr ='VI'
                if lvl == 7:
                    lvlr ='VII'
                
                
                Wand = [lvlr, 'Wand']
                Potion_bottle = [lvlr, 'Potion_bottle']
                Spell_book = [lvlr, 'Spell']
                
                price = lvl**3 * 10
                display = [Wand, Potion_bottle, Spell_book]
                
                return shop_display(display, price, players_money, kind)
                
                
                
            
            
            def Food_shop(which, players_money):
                kind = 'F'
                
                lvl = int(which[1])
                if lvl == 1:
                    d = 1
                elif lvl == 3:
                    d = 3
                elif lvl == 5:
                    d = 5
                    
                Bread = ['I', 'Bread', lvl]
                Water = ['I', 'Water', 1/2*lvl]
                
                Chicken = ['III', 'Chicken',2*lvl]
                Sugar_water = ['III', 'Sugar_water',lvl]
                
                Beef = ['V', 'Beef', 3*lvl]
                Whisky = ['V', 'Whisky', 4*lvl]
                
                
                if d == 1:
                    display = [Bread, Water]
                elif d == 3:
                    display = [Bread, Water, Chicken, Sugar_water]
                elif d == 5:
                    display = [Bread, Water, Chicken, Sugar_water, Beef, Whisky]
                
                price = '1'
                
                
                return shop_display(display, price, players_money, kind)
            
            def Travel_shop(which, players_money):
                
                lvl = int(which[1])
            
                if lvl == 1:
                    d = 1
                elif lvl == 3:
                    d = 3
                elif lvl == 6:
                    d = 6
                    
                Bike = ['I', 'Bike']
                
                Horse = ['III', 'Horse']
                
                Carriage = ['VI', 'Carriage']
                
                
                
                if d == 1:
                    display = [Bike]
                elif d == 3:
                    display = [Horse]
                elif d == 6:
                    display = [Carriage]
                
                price = lvl**3 * 10

                kind = 'T'
                
                return shop_display(display, price, players_money, kind)
            
            if which[0] == 'W':
                after_the_buying = Weapon_shop(which, pm)
            elif which[0] == 'M':
                after_the_buying = Magic_shop(which, pm)
            elif which[0] == 'F':
                after_the_buying = Food_shop(which, pm)
            elif which[0] == 'T':
                after_the_buying = Travel_shop(which, pm)
                
            return after_the_buying  
        
        def awds(mapn ,x, y, where):
            if where == 'Eq':
                borderx = 8
                bordery = 3
            elif where == 'Dg':
                borderx = 31
                bordery = 55
            else:
                borderx = 38
                bordery = 55
            time.sleep(0.01)
            # print('Can Move')
            key = ''
            
            key = keyboard.read_key()
            if keyboard.is_pressed('w') or keyboard.is_pressed('Up'):
                if y - 1 >= 0 and mapn[y - 1][x] != 'C':
                    return ("-1")
            elif keyboard.is_pressed('s') or keyboard.is_pressed('Down'): 
                
                if y + 1 <= bordery and mapn[y + 1][x] != 'C':
                    return "1"
            elif keyboard.is_pressed('a') or keyboard.is_pressed('Left'):
                
                if x - 1 >= 0 and mapn[y][x - 1] != 'C':
                    return "-10"
            elif keyboard.is_pressed('d') or keyboard.is_pressed('Right'): 
                
                if x + 1 <= borderx and mapn[y][x + 1] != 'C':
                    return "10"
            elif keyboard.is_pressed('Enter'):
                return 'Enter'
            elif keyboard.is_pressed('e'):
                return 'e'
            elif keyboard.is_pressed('f'):
                return 'f'
            elif keyboard.is_pressed('Escape'):
                m = menu()
        
        def mob_detector(Dungeon,xp,yp,rd,mob):
            mobs_sight = []
            player_in_mobs_sight = []
            mis = 0
            ms = 0
            for vy in range(yp - rd, yp + rd + 1):
                mobs_sight.append([])
                for vx in range(xp - rd, xp + rd + 1):
                    
                    if vy < len(Dungeon) and vy > -1:
                        if vx < len(Dungeon[0]) and vx > -1:
                            mobs_sight[ms] += Dungeon[vy][vx]
                            if str(Dungeon[vy][vx][0]) == mob:
                                player_in_mobs_sight.append([])
                                player_in_mobs_sight[mis] += vy, vx
                                mis += 1
                            # print(Dungeon[vy][vx])
                ms += 1 
            easy = [player_in_mobs_sight, mobs_sight]    
            return easy
        
        def mobs(Dungeon, my, mx , yp, xp):
            wy, wx = my, mx
            where_will_it_go_if_the_way_is_valid = ''
            while wy != yp or wx != xp:
            
                if wy > yp:
                    wy -= 1
                elif wy < yp:
                    wy += 1
                elif wx > xp:
                    wx -= 1
                elif wx < xp:
                    wx += 1
                if Dungeon[wy][wx] == '8':
                    if where_will_it_go_if_the_way_is_valid == '':
                        where_will_it_go_if_the_way_is_valid = (wy, wx)
                        
                    
                elif Dungeon[wy][wx] == '7':
                    return (my, mx)
                
                elif Dungeon[wy][wx][0] == '9':
                    return (my, mx)
                
                elif Dungeon[wy][wx] == 'P':
                    if where_will_it_go_if_the_way_is_valid == '':
                        return (my, mx, 'fight')
                
            return where_will_it_go_if_the_way_is_valid        
            
            

        def fight(mapn, x, y):
            e = mob_detector(mapn,x,y,3,'9')
            if len(e[0]) > 0:
                if eq[3][0][0][0] == "[ ]":
                    return ''
                else: w_lvl = eq[3][0][0][1] 
                    
                Dmg = 1
                if w_lvl == 'I':
                    Dmg = 1
                if w_lvl == "II":
                    Dmg = 2
                if w_lvl == 'III':
                    Dmg = 3
                if w_lvl == 'IV':
                    Dmg = 4
                if w_lvl == 'V':
                    Dmg = 5
                if w_lvl == 'VI':
                    Dmg = 6
                if w_lvl == 'VII':
                    Dmg = 7
                
                Dmg = Dmg*25
                
                
                list_of_opponents = []
                for i in range(0, len(e[0])):
                    # print(int(mapn[e[0][i][0]][e[0][i][1]][1]) * 20)
                    Monsters_hp = (int(mapn[e[0][i][0]][e[0][i][1]][1]) * 20)
                    list_of_opponents.append([])
                    if len(mapn[e[0][i][0]][e[0][i][1]]) == 2:
                        if Dmg >= Monsters_hp:
                            list_of_opponents[i] += e[0][i], mapn[e[0][i][0]][e[0][i][1]], 'dead'    
                        else:
                            list_of_opponents[i] += e[0][i], mapn[e[0][i][0]][e[0][i][1]], Monsters_hp - Dmg
                    else:
                        if Dmg >= Monsters_hp:
                            list_of_opponents[i] += e[0][i],  mapn[e[0][i][0]][e[0][i][1]], 'dead'    
                        else:
                            list_of_opponents[i] += e[0][i],  mapn[e[0][i][0]][e[0][i][1]], Monsters_hp - Dmg
                        
                return list_of_opponents
                    
                    
        def print_(mapn, x, y, rd, spec, HP):
            if rd != 'E':
                blocks = {
                    "You":chr(int('0xC6C3' , 16)),
                    'Kira':'Ki',
                    'Jufen':'Ju',
                    'Sunui':'Su',
                    'Lacai':'La',
                    'Hasitisi':'Ha',
                    'Vitisuri':'Vi',
                    'Castle':chr(int('0x2B1B', 16)), 
                    'Border':chr(int('0x2B1B', 16)),
                    'Grass':chr(int('0x1F7E9', 16)),
                    'Woods':chr(int('0x1F332', 16)),
                    'White_Border':'⬜',
                    'Shop':'🟫',
                    'Road':chr(int('0x2B1B', 16)),
                    'Mountains': '🪨 ',
                    'Water':'🌊',
                    'Bridge':"🟫",
                    'Dungeon_Entrance':'⬜',
                    'Dungeon_road':'🏻'
                    
                }
                dim_w = len(mapn)
                dim_k = len(mapn[0])
                
                # print("\033[A" * ((2 * rd) + 10))
                os.system('clear')
                
            
                for w in range(y - rd, y + rd + 1):
                    line = ''
                    for k in range(x - rd, x + rd + 1):
                        if w == y and k == x:
                            # if mapn == mapH or mapn == mapL or mapn == mapV:
                            #     line += 'Y '
                            # else:
                            if spec == 'fight':
                                line += '👾'
                            else: line += blocks['You'] # You
                            
                        elif w < -1 or w >= dim_w + 1 or k < -1 or k >= dim_k + 1:
                            line += blocks['Border'] # Border
                        elif w == -1 or w == dim_w or k == -1 or k == dim_k:
                            line += blocks['White_Border'] # White_Border
                        # elif mapa[w][k] == "H":
                        #     line += blocks['Home'] # Home
                        elif mapn[w][k] == "K":
                            line += blocks['Kira'] # Kira
                        elif mapn[w][k] == "J":
                            line += blocks['Jufen'] # Jufen
                        elif mapn[w][k] == "S":
                            line += blocks['Sunui'] # Sunui
                        elif mapn[w][k] == "C":
                            line += blocks['Castle'] # Castle
                        elif mapn[w][k][0] == "E":
                            line += blocks['Dungeon_Entrance'] # Dungeon_Entrance
                        elif mapn[w][k] == "L":
                            line += blocks['Lacai'] # Lacai
                        elif mapn[w][k] == "H":
                            line += blocks['Hasitisi'] # Hasitisi
                        elif mapn[w][k] == "V":
                            line += blocks['Vitisuri'] # Vitisuri
                        elif mapn[w][k] == "1":
                            line += blocks['Woods'] # Woods
                        elif mapn[w][k] == "2":
                            line += blocks['Mountains'] # Mountains
                        elif mapn[w][k] == "3":
                            line += blocks['Water'] # Water
                        elif mapn[w][k] == "4":
                            line += blocks['Bridge'] # Bridge
                        elif mapn[w][k] == "5":
                            line += blocks['Road'] # Road
                        elif mapn[w][k] == "6":
                            line += blocks['Shop'] # Shop
                        elif mapn[w][k] == "7":
                            line += blocks['Border'] # Dungeon_structure
                        elif mapn[w][k] == "8":
                            line += blocks['Dungeon_road'] # Dungeon_street
                        elif mapn[w][k][0] == "9":
                            if spec == 'fight':
                                line += blocks['Dungeon_road'] # Dungeon_street
                            else:line += "👾" # Mobs    
                        elif mapn[w][k][0] == "M":
                            line += 'M' + mapn[w][k][1] # Magic_entrance
                        elif mapn[w][k][0] == "W":
                            line += 'W' + mapn[w][k][1] # Weapons_entrance
                        elif mapn[w][k][0] == "T":
                            line += 'T' + mapn[w][k][1] # Transport_entrance
                        elif mapn[w][k][0] == "F":
                            line += 'F' + mapn[w][k][1] # Food_entrance
                        elif mapn[w][k][0] == "g":
                            line += 'g' + mapn[w][k][1] # Guild_Hall_entrance
                        elif mapn[w][k][0] == "c":
                            line += 'c' + mapn[w][k][1] # Casino_entrance
                        elif mapn[w][k][0] == 'I' or mapn[w][k][0] == 'V' or mapn[w][k][0] == 'X':
                            line += mapn[w][k]
                        elif mapn[w][k][0] == 't':
                            if mapn[w][k][1] == 'L':
                                line += blocks['Dungeon_Entrance'] # From_Kingdom_to_world (Leave)
                            else:
                                line += mapn[w][k][1] + ' '
                        
                        
                        else:
                            line += blocks['Grass'] # Grass
                
                
                    print(line,' ')
                
                print('♥️'* HP)
                
                line = ''
                for cl in range(0, 9):
                    for i in range(0, len(eq[3][cl])):
                        line += str(eq[3][cl][i])
                print(line)
                
                print(f"x - {x}")
                print(f"y - {y}")

            
            
            
            else:
                
                
                if spec == 1:
                    Cursor = f'({str(eq[y][x][0])})'
                else:
                    Cursor = " ༓ "
                
                if x == 's' or y == 's':
                    x = 0
                    y = 0
                    Cursor = str(eq[y][x][0])
                
                cl = 0
                sq = 0

                for sq in range (0,4):
                    line = ''
                    for cl in range(0, 9):
                        if x == cl and y == sq:
                            if str(eq[sq][cl][0]) == '[ ]':
                                line += Cursor
                            else:
                                line += f'({str(eq[sq][cl][0])})'
                            
                        else:
                            line += str(eq[sq][cl][0])
                    print(line)

        def move_eq(mapn,xw,yw,rd,p_eq,p_money):
            e = 0
            x = 0
            y = 0
            c = ''
            spec = 0
            while e != 1:
                os.system('clear')
                print_(p_eq, x, y, 'E' , spec, '')
                c = awds(p_eq,x,y, 'Eq')
                if c == "-1":
                    y -= 1
                elif c == '1':
                    y += 1
                elif c == '-10':
                    x -= 1
                elif c == '10':
                    x += 1
                elif c == 'Enter':
                    if spec == 0:
                        spec = 1
                        xr = x
                        yr = y
                    else:
                        if p_eq[y][x][0] == '[ ]':
                            p_eq[y][x][0] = p_eq[yr][xr][0]
                            p_eq[yr][xr][0] = '[ ]'
                            spec = 0
                        
                elif c == 'e':

                    the_returning_info = [mapn,xw,yw,rd,p_eq,p_money]
                    return the_returning_info
            
        def move(mapn,x,y,rd,p_eq,p_money,if_dungeon_which_lvl):
            HP = 10
            os.system('clear')
            p_eq_befor_anything = p_eq
            
            
            c = ''

            once = 0
            if_eq = ''
            change_maps = ''
            print_(mapn, x, y, rd, '', HP)
            while c != 'x' and change_maps == '' and if_eq == '' and p_eq_befor_anything == p_eq and HP > 0:
                
                if mapn == mapH or mapn == mapL or mapn == mapV:
                    mapn[y][x] = '8'    
                    c = awds(mapn, x, y, 'Dg')
                else:
                    c = awds(mapn, x, y, '')
                xr = x
                yr = y
                coordinates_befor = [xr, yr]
                if c == "-1":
                    y -= 1
                    once = 1
                elif c == '1':
                    y += 1
                    once = 1
                elif c == '-10':
                    x -= 1
                    once = 1
                elif c == '10':
                    x += 1
                    once = 1
                elif c == 'e':
                    if once == 1:
                        if_eq = 'Eq'
                        change_maps = mapn
                elif c == 'f':
                    fight_reasoults = fight(mapn, x,y)
                    if fight_reasoults != None:
                        for i in range (0, len(fight_reasoults)):
                            if fight_reasoults[i][2] == 'dead':
                                mapn[fight_reasoults[i][0][0]][fight_reasoults[i][0][1]] = '8'
                                change_maps = mapn
                                ################################################### Place where Player gets loot from mobs
                                ################################################### Place where Player gets loot from mobs
                                ################################################### Place where Player gets loot from mobs
                                ################################################### Place where Player gets loot from mobs
                                ################################################### Place where Player gets loot from mobs
                                loot = [fight_reasoults[i][1][1],'Wood']
                                p_money += mapn[fight_reasoults[i][0][0]][fight_reasoults[i][0][1]][1] ** 2
                                e_once = 0
                                j = 3
                                for l in range (0,4):
                                    
                                    for i in range (0, 9):
                                        if e_once == 0:
                                            if p_eq[j][i][0] == '[ ]':
                                                p_eq[j][i][0] = loot
                                                e_once = 1
                                    j -= 1
                            else:
                                print(mapn[fight_reasoults[i][0][0]][fight_reasoults[i][0][1]][1])
                                print(str(round((if_dungeon_which_lvl / 20) + 0.5)))
                                mapn[fight_reasoults[i][0][0]][fight_reasoults[i][0][1]] = mapn[fight_reasoults[i][0][0]][fight_reasoults[i][0][1]][0] + str(round((if_dungeon_which_lvl / 20) + 0.5))
                                
                            
                            
                coordinates_after = [x, y]
                if mapn == mapH or mapn == mapL or mapn == mapV:
                
                    ms = move_speed_next_move_checker(mapn, coordinates_after[0], coordinates_after[1], 1, rd)
                else:
                    ch = which_shop_enter_checker(mapn, coordinates_after[0], coordinates_after[1])
                    ms = move_speed_next_move_checker(mapn, coordinates_after[0], coordinates_after[1], 0, rd)
                time.sleep(0.01 * int(ms))

                s = specials(mapn, coordinates_after[0], coordinates_after[1])
                if s[0] == 'K' or s[0] == 'J' or s[0] == 'S':
                    if s[0] == 'K':
                        s = 'kira'
                    elif s[0] == 'J':
                        s = 'jufen'
                    elif s[0] == 'S':
                        s = 'sunui'
                        
                    enter = F.Moving_between_files(s)
                    
                    if enter == 1:
                        u = kingdom_uncoder(s[0])
                        change_maps = u
                if s == 'EV' or s == 'EH' or s == 'EL':
                    if s == 'EV':
                        s = 'vitisuri'
                    elif s == 'EH':
                        s = 'hasitisi'
                    elif s == 'EL':
                        s = 'lacai'
                    
                    enter = F.Moving_between_files(s)
                    
                    if enter == 1:
                        u = dungeon_uncoder(s[0])
                        change_maps = u
                    
                if mapn == mapJ or mapn == mapK or mapn == mapS:
                    if ms == 0: # Illegal move
                        x = xr
                        y = yr
                    elif ms == 2: # Leaving the shop
                        after_shop = shop(ch,p_eq,p_money)
                        if after_shop[0] != 'nothing':
                            once = 0
                            for l in range (0,4):
                                j = 3
                                for i in range (0, 9):
                                    if once == 0:
                                        if p_eq[j][i][0] == '[ ]':
                                            p_eq[j][i][0] = after_shop[0][1]
                                            once = 1
                                j -= 1
                        change_maps = mapn
                
                    
                        
                    elif ms == 9:
                        change_maps = mapa
                                
                if mapn == mapH or mapn == mapL or mapn == mapV:
                    if ms != 0 and ms!= 8: mapn[y][x] = 'P'
                    else: mapn[yr][xr] = 'P'
                    if ms == 0:
                        x = xr
                        y = yr
                    pims = mob_detector(mapn,x,y,rd + 2, '9')
                    if len(pims[0]) > 0:
                        # print(len(pims[0]))
                        for i in range (0, len(pims[0])):
                            m = mobs(mapn, pims[0][i][0], pims[0][i][1], y, x)
                            if len(m) == 3:
                                HP -= int(mapn[pims[0][i][0]][pims[0][i][1]][1])
                                print_(mapn, x, y, rd, 'fight', HP)
                                time.sleep(1)
                            mob = mapn[pims[0][i][0]][pims[0][i][1]]
                            mapn[pims[0][i][0]][pims[0][i][1]] = '8'
                            mapn[m[0]][m[1]] = mob
                    
                    if ms == 8: 
                        
                        if if_dungeon_which_lvl == '':
                            if_dungeon_which_lvl = 1
                        else:
                            if_dungeon_which_lvl += 1
                        change_maps = mapn
                    if ms == 9:
                        change_maps = mapa 
                            
                    print_(mapn, x, y, rd, '', HP)
                    
                else:
                    print_(mapn, x, y, rd, '', HP)
                
            
            time.sleep(0)
            if HP <= 0:
                print('You shall be revived tommorow at the exact same hour "D ')
                time.sleep(60*60*24)
            the_returning_info = [change_maps,xr,yr,rd,p_eq,p_money,if_eq,if_dungeon_which_lvl]
            return the_returning_info

            
        def menu():
            os.system('clear')
            print('To go back to the game press : `esc` ')
            
            m = 0
            while m == 0:
                key = keyboard.read_key()
                if keyboard.is_pressed('esc'):
                    m = 1
                    os.system('clear')
                    return 0
            
            
        
        
        
        
        gen_map(mapa, 39, 56)
        
        # gen_map(mapJ, 39, 56)
        
        
        # Map_whole(accual)
        def Whole_map_generator():
            gen_castle(mapa,4,12,'J')
            gen_castle(mapa,7,34,'K')
            gen_castle(mapa,31,34,'S')
            gen_square(mapa,0,19,10,21,'m')
            gen_moutains(mapa,11,21,19,'m','u')
            gen_moutains(mapa,23,8,30,'m','d')
            gen_triangle_l(mapa,31,17,34,20,'m','s')
            gen_triangle_r(mapa,35,14,38,11,'w','s')
            gen_triangle_r(mapa,35,31,38,28,'w','r')
            gen_triangle_r(mapa,32,27,34,25,'w','s')
            gen_triangle_r(mapa,22,31,25,28,'w','s')
            gen_triangle_r(mapa,26,34,28,32,'w','r')
            gen_square(mapa,35,15,38,27,'w')
            gen_square(mapa,26,28,34,31,'w')
            gen_square(mapa,22,32,25,55,'w')
            gen_square(mapa,21,37,26,39,'b')
            gen_square(mapa,0,39,12,41,'f')
            gen_square(mapa,13,28,15,55,'f')
            gen_square(mapa,16,23,22,29,'f')
            gen_triangle_r(mapa,14,27,15,26,'f','s')
            gen_special(mapa,16,30,'f')
            gen_special(mapa,18,26,'0')
            gen_special(mapa,19,26,'0')
            gen_special(mapa,20,26,'0')
            gen_special(mapa,19,25,'0')
            gen_special(mapa,19,27,'0')
            gen_special(mapa,22,29,'0')
            gen_special(mapa,22,24,'0')
            gen_special(mapa,22,23,'0')
            gen_special(mapa,21,23,'0')
            gen_special(mapa,16,24,'0')
            gen_special(mapa,16,23,'0')
            gen_special(mapa,17,23,'0')
            gen_special(mapa,1,18,'m')
            gen_special(mapa,3,18,'m')
            gen_square(mapa,4,17,5,18,'m')
            gen_special(mapa,9,16,'m')
            gen_square(mapa,8,17,9,18,'m')
            gen_special(mapa,10,18,'m')
            
            gen_dungeon(mapa,31,4,'L')
            gen_dungeon(mapa,2,45,'H')
            gen_dungeon(mapa,29,42,'V')
        Whole_map_generator()
        
        mapJ = F.Generators('jufen', '')
        # Kira(Kingdom)

        mapK = F.Generators('kira', '')
        # Sunui(Kingdom)
        
        mapS = F.Generators('sunui', '')
        
        # print_map(mapa)
        mapH = F.Generators('hasitisi', 1)
        
        mapL = F.Generators('lacai', 1)
        
        mapV = F.Generators('vitisuri', 1)
        
        os.system('clear')
        
        
        money = 100
        eq = [[['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]']],
              [['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]']],
              [['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]']],
              [[['I' ,'Sword']],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]'],['[ ]']]]
        
        maprememberer = 0
        x = 19
        y = 26
        
        xb = 0
        yb = 0
        
        
        z = 0
        once = 0
        while z <= 8:
            was_in_eq_and_whants_again = 0
            if once == 0:
                w = move(mapa,x,y,4,eq,money, '')
                xrw = w[1]
                yrw = w[2]
                once += 1
            if w[-2] == 'Eq':
                w = move_eq(w[0],xb,yb,4,eq,money)

            if w[0] == mapa:
                w = move(mapa,xrw,yrw,4,eq,money, '')
                xrw = w[1]
                yrw = w[2]
                xb = w[1]
                yb = w[2]
            
            money = w[5]
            eq = w[4]
            
            if w[-2] == 'Eq':
                was_in_eq_and_whants_again = 1
            
            
            if was_in_eq_and_whants_again == 0:
                
            
                if str(w[0]) == '7':
                    z = 9
                else:   
                    if maprememberer != w[0]:
                        if w[0] == mapH:
                            if w[-1] == '':
                                w[-1] = 1
                            mapH = F.Generators('hasitisi', w[-1])
                            w[0] = mapH
                            w = move(w[0],18,53,5,eq,money,w[-1])
                        if w[0] == mapS :
                            if w[-1] == '':
                                w[-1] = 1
                            mapS = F.Generators('sunui', w[-1])
                            w[0] = mapH
                            w = move(w[0],18,53,5,eq,money,w[-1])
                        if w[0] == mapV:
                            if w[-1] == '':
                                w[-1] = 1
                            mapS = F.Generators('vitisuri', w[-1])
                            w[0] = mapH
                            w = move(w[0],18,53,5,eq,money,w[-1])
                            
                        else: w = move(w[0],18,53,5,eq,money, '')
                        maprememberer = w[0]
                        xb = w[1]
                        yb = w[2]
                    else:
                        
                        w = move(w[0],w[1],w[2],5,eq,money, w[-1])
                        if w[0] == mapH:
                            if w[-1] == '':
                                w[-1] = 1
                            mapH = F.Generators('hasitisi', w[-1])
                            w[0] = mapH
                            w = move(w[0],18,53,5,eq,money,w[-1])
                        if w[0] == mapS :
                            if w[-1] == '':
                                w[-1] = 1
                            mapS = F.Generators('sunui', w[-1])
                            w[0] = mapH
                            w = move(w[0],18,53,5,eq,money,w[-1])
                        if w[0] == mapV:
                            if w[-1] == '':
                                w[-1] = 1
                            mapS = F.Generators('vitisuri', w[-1])
                            w[0] = mapH
                            w = move(w[0],18,53,5,eq,money,w[-1])
                        xb = w[1]
                        yb = w[2]
mapa = []
# mapK = []
# mapJ = []
# mapS = []

M = Move()
M.map_whole()