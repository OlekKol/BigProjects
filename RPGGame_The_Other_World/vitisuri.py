import choice
from random import randint
class Vitisuri():
    def __init__(self) -> None:
        pass
    def info(self):
        print("Vitisuri - Dungeon")
        print("Stages - I ---> X ")
    def do_you_whant_enter(self):
        Y_N = ['No', 'Yes']
        answer = choice.WybierzZListy(Y_N, 'Do you whant to enter Vitisuri? ')
        print (answer)
        return answer
    def Vitisuri_Dungeon_generator(self, lvl):
        mapV = []
        def gen_map(mapa, dim_x, dim_y):    
            for y in range(dim_y):
                line = []
                for x in range(dim_x):
                    line.append('8')
                mapa.append(line)
                
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
            elif kind == 'wall':  
                n = 7
                
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
            elif kind == 'wall':  
                n = 7
            if len(mapa[0]) == 32:
                s = 1
            c = 0
            ungli = 0
            remainder = 0
            for y_ in range ((y - r),(y + r + 1)):
                c = remainder
                for x_ in range ((x - c),(x + c + 1)):
                    if s == 1:
                        if x_ == 32:
                            mapa[y_][x_ - 1] = str(n)
                        else:
                            if y_ == y and x_ > (x - r) and x_ < (x + r):
                                mapa[y_][x_] = str(0)
                            elif x_== x and y_ > (y - r) and y_ < (y + r):
                                mapa[y_][x_] = str(0)
                            else:
                                mapa[y_][x_] = str(n)
                        c += 1
                    else:
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
            elif kind == 'wall':  
                n = 7
                
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
                            mapa[y_][x_] = str('E')
                        elif y_ == y + 2 and x_ == x + 4:
                            mapa[y_][x_] = str('E')
                        elif y_ >= y + 3 and x_ >= x + 2 and x_ <= x + 5:
                            mapa[y_][x_] = str('E')
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
        
        color = randint(0,9)
        color = 1
        # System : goes max left, every route
        gen_map(mapV,32,56)
        gen_square(mapV, 10, 32, 21, 32, 'wall')
        gen_square(mapV, 10, 46, 10, 53, 'wall')
        gen_square(mapV, 21, 46, 21, 53, 'wall')        
        gen_square(mapV, 10, 0, 10, 10, 'wall')
        gen_square(mapV, 21, 0, 21, 10, 'wall')        

        if color == 0: # Red
            gen_square(mapV, 10, 21, 10, 32, 'wall')
            gen_square(mapV, 21, 32, 21, 43, 'wall')
            gen_square(mapV, 10, 32, 21, 32, 'wall')
            
            in_color = randint(0,4)
            if in_color == 0:
                gen_square(mapV, 10, 21, 21, 21, 'wall')
            elif in_color == 1:
                gen_square(mapV, 21, 21, 21, 32, 'wall')
            elif in_color == 2:
                gen_square(mapV, 21, 21, 31, 21, 'wall')
            elif in_color == 3:
                gen_square(mapV, 21, 21, 21, 10, 'wall')
        
        if color == 1: # Orange
            gen_square(mapV, 21, 32, 21, 43, 'wall')
            gen_square(mapV, 10, 32, 21, 32, 'wall')
            gen_square(mapV, 0, 21, 10, 21, 'wall')
            in_color = randint(0,3)
            if in_color == 0:
                gen_square(mapV, 21, 21, 31, 21, 'wall')
            elif in_color == 1:
                gen_square(mapV, 21, 21, 21, 10, 'wall')
            elif in_color == 2:
                gen_square(mapV, 21, 21, 21, 32, 'wall')
        
        if color == 2: # Rose
            gen_square(mapV, 21, 32, 21, 43, 'wall')
            gen_square(mapV, 10, 32, 21, 32, 'wall')
            gen_square(mapV, 0, 21, 21, 21, 'wall')
            gen_square(mapV, 10, 21, 21, 21, 'wall')
            
        if color == 3: # Yellow
            gen_square(mapV, 21, 32, 21, 43, 'wall')
            gen_square(mapV, 10, 32, 10, 43, 'wall')
            gen_square(mapV, 21, 21, 21, 32, 'wall')
            gen_square(mapV, 10, 21, 21, 21, 'wall')
            
        if color == 4: # Light Green
            gen_square(mapV, 21, 32, 21, 43, 'wall')
            gen_square(mapV, 10, 32, 10, 43, 'wall')
            gen_square(mapV, 21, 21, 21, 32, 'wall')
            gen_square(mapV, 10, 21, 10, 32, 'wall')
        
        if color == 5: # Green
            gen_square(mapV, 21, 32, 21, 43, 'wall')
            gen_square(mapV, 10, 32, 10, 43, 'wall')
            gen_square(mapV, 10, 21, 21, 32, 'wall')
            gen_square(mapV, 10, 21, 21, 21, 'wall')
        
        if color == 6: # Blue
            gen_square(mapV, 10, 32, 21, 32, 'wall')
            gen_square(mapV, 21, 32, 21, 43, 'wall')
            gen_square(mapV, 21, 21, 31, 21, 'wall')
            gen_square(mapV, 10, 21, 21, 21, 'wall')
            
        if color == 7: # Violet
            gen_square(mapV, 10, 32, 21, 32, 'wall')
            gen_square(mapV, 21, 32, 21, 43, 'wall')
            gen_square(mapV, 21, 21, 31, 21, 'wall')
            in_color = randint(0,3)
            if in_color == 0:
                gen_square(mapV, 10, 10, 10, 21, 'wall')
            elif in_color == 1:
                gen_square(mapV, 0, 21, 21, 10, 'wall')
            elif in_color == 2:
                gen_square(mapV, 10, 21, 10, 32, 'wall')
        
        if color == 8: # Brown
            gen_square(mapV, 10, 32, 21, 32, 'wall')
            gen_square(mapV, 21, 32, 21, 43, 'wall')
            gen_square(mapV, 21, 21, 21, 32, 'wall')
            in_color = randint(0,4)
            if in_color == 0:
                gen_square(mapV, 10, 10, 10, 21, 'wall')
            elif in_color == 1:
                gen_square(mapV, 0, 21, 21, 10, 'wall')
            elif in_color == 2:
                gen_square(mapV, 10, 21, 10, 32, 'wall')
            elif in_color == 3:
                gen_square(mapV, 10, 21, 21, 21, 'wall')
        
        gen_diamond(mapV, 0, 10, 1, 'wall')
        gen_diamond(mapV, 0, 21, 1, 'wall')
        gen_diamond(mapV, 0, 32, 1, 'wall')
        gen_diamond(mapV, 0, 43, 1, 'wall')
        gen_diamond(mapV, 10, 10, 2, 'wall')
        gen_diamond(mapV, 21, 10, 2, 'wall')
        gen_diamond(mapV, 31, 10, 1, 'wall')
        gen_diamond(mapV, 10, 21, 2, 'wall')
        gen_diamond(mapV, 10, 32, 2, 'wall')
        gen_diamond(mapV, 10, 43, 2, 'wall')
        gen_diamond(mapV, 21, 21, 2, 'wall')
        gen_diamond(mapV, 31, 21, 1, 'wall')
        gen_diamond(mapV, 21, 32, 2, 'wall')
        gen_diamond(mapV, 21, 43, 2, 'wall')
        gen_diamond(mapV, 31, 32, 1, 'wall')
        gen_diamond(mapV, 31, 43, 1, 'wall')
        gen_special2(mapV, 0, 0,'7')
        gen_special2(mapV, 1, 0,'7')
        gen_special2(mapV, 0, 1,'7')
        gen_special2(mapV, 9, 0,'7')
        gen_special2(mapV, 10, 0,'7')
        gen_special2(mapV, 11, 0,'7')
        gen_special2(mapV, 10, 1,'7')
        gen_special2(mapV, 20, 0,'7')
        gen_special2(mapV, 21, 0,'7')
        gen_special2(mapV, 22, 0,'7')
        gen_special2(mapV, 21, 1,'7')
        gen_special2(mapV, 30, 0,'7')
        gen_special2(mapV, 31, 0,'7')
        gen_special2(mapV, 31, 1,'7')
        gen_special2(mapV, 0, 54,'7')
        gen_special2(mapV, 0, 55,'7')
        gen_special2(mapV, 1, 55,'7')
        gen_special2(mapV, 9, 55,'7')
        gen_special2(mapV, 10, 55,'7')
        gen_special2(mapV, 11, 55,'7')
        gen_special2(mapV, 10, 54,'7')
        gen_special2(mapV, 20, 55,'7')
        gen_special2(mapV, 21, 55,'7')
        gen_special2(mapV, 22, 55,'7')
        gen_special2(mapV, 21, 54,'7')
        gen_special2(mapV, 30, 55,'7')
        gen_special2(mapV, 31, 55,'7')
        gen_special2(mapV, 31, 54,'7')
        lvl += 1
        lvlr = 'I   '
        if lvl == 1:
            lvlr ='I   '
        if lvl == 2:
            lvlr ='II  '
        if lvl == 3:
            lvlr ='III '
        if lvl == 4:
            lvlr ='IV  '
        if lvl == 5:
            lvlr ='V   '
        if lvl == 6:
            lvlr ='VI  '
        if lvl == 7:
            lvlr ='VII '
        if lvl == 8:
            lvlr = 'VIII'
        if lvl == 9:
            lvlr = 'IX  '
        if lvl == 10:
            lvlr = 'X   '
            lvl = 0
    
        gen_special2(mapV, 15, 1,lvlr[0] + lvlr[1])
        
        gen_special2(mapV, 16, 1,lvlr[2] + lvlr[3])
        
        
        gen_special2(mapV, 4, 4,'9' + str(lvl))
        gen_special2(mapV, 15, 4,'9' + str(lvl))
        gen_special2(mapV, 16, 4,'9' + str(lvl))
        
        gen_special2(mapV, 6, 4,'9' + str(lvl))
        gen_special2(mapV, 17, 4,'9' + str(lvl))
        gen_special2(mapV, 18, 4,'9' + str(lvl))
        
        gen_special2(mapV, 4, 15,'9' + str(lvl))
        gen_special2(mapV, 15, 15,'9' + str(lvl))
        gen_special2(mapV, 16, 15,'9' + str(lvl))
        
        gen_special2(mapV, 6, 15,'9' + str(lvl))
        gen_special2(mapV, 17, 15,'9' + str(lvl))
        gen_special2(mapV, 18, 15,'9' + str(lvl))
        
        gen_special2(mapV, 4, 26,'9' + str(lvl))
        gen_special2(mapV, 15, 26,'9' + str(lvl))
        gen_special2(mapV, 16, 26,'9' + str(lvl))
        
        gen_special2(mapV, 6, 26,'9' + str(lvl))
        gen_special2(mapV, 17, 26,'9' + str(lvl))
        gen_special2(mapV, 18, 26,'9' + str(lvl))
        
        gen_special2(mapV, 4, 35,'9' + str(lvl))
        gen_special2(mapV, 15, 35,'9' + str(lvl))
        gen_special2(mapV, 16, 35,'9' + str(lvl))
        
        gen_special2(mapV, 6, 35,'9' + str(lvl))
        gen_special2(mapV, 17, 35,'9' + str(lvl))
        gen_special2(mapV, 18, 35,'9' + str(lvl))
        
        gen_special2(mapV,15, 55, 'tL')
        gen_special2(mapV,16, 55, 'tL')
        
        return mapV