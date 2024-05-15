import choice
# from move import Move
# M = Move()


class Jufen():
    def __init__(self) -> None:
        pass
    def do_you_whant_enter(self):
        Y_N = ['No', 'Yes']
        answer = choice.WybierzZListy(Y_N, 'Do you whant to enter Jufen? ')
        print (answer)
        return answer
    def info(self):
        print("Jufen - Kingdom")
    def Jufen_kingdom_generator(mapJ):
        mapJ = []
        
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
        
        gen_map(mapJ,39,56)
        gen_square(mapJ,16,37,21,55,'r')
        gen_square(mapJ,2,45,35,49,'r')
        gen_square(mapJ,2,2,6,44,'r')
        gen_square(mapJ,7,2,30,6,'r')
        gen_square(mapJ,31,2,35,44,'r')
        gen_square(mapJ,12,37,25,39,'r')
        gen_square(mapJ,12,12,14,36,'r')
        gen_square(mapJ,15,12,22,14,'r')
        gen_square(mapJ,23,12,25,36,'r')
        
        gen_square(mapJ,12,42,15,44,'s')
        gen_square(mapJ,7,42,10,44,'s')
        gen_square(mapJ,7,29,9,40,'s')
        gen_square(mapJ,7,20,9,27,'s')
        gen_square(mapJ,0,29,1,40,'s')
        gen_square(mapJ,0,20,1,27,'s')
        gen_square(mapJ,0,12,1,17,'s')
        gen_square(mapJ,7,7,10,10,'s')
        gen_square(mapJ,13,7,24,10,'s')
        gen_square(mapJ,13,0,24,1,'s')
        gen_square(mapJ,27,7,30,10,'s')
        gen_square(mapJ,26,16,30,23,'s')
        gen_square(mapJ,26,26,28,38,'s')
        gen_square(mapJ,36,11,38,48,'s')
        gen_square(mapJ,22,42,25,44,'s')
        gen_square(mapJ,27,42,30,44,'s')
        gen_square(mapJ,15,15,22,17,'s')
        gen_square(mapJ,15,19,22,31,'s')
        gen_square(mapJ,15,33,22,36,'s')
        gen_square(mapJ,33,0,37,1,'s')
        gen_square(mapJ,36,2,37,4,'s')
        gen_square(mapJ,0,0,4,1,'s')
        gen_square(mapJ,0,2,1,4,'s')
        
        gen_special2(mapJ,15,44,'W1')
        gen_special2(mapJ,15,43,'W1')
        gen_special2(mapJ,14,44,'W1')
        gen_special2(mapJ,7,44,'M1')
        gen_special2(mapJ,8,44,'M1')
        gen_special2(mapJ,7,43,'M1')
        gen_special2(mapJ,22,44,'F1')
        gen_special2(mapJ,23,44,'F1')
        gen_special2(mapJ,22,43,'F1')
        gen_special2(mapJ,30,44,'T1')
        gen_special2(mapJ,29,44,'T1')
        gen_special2(mapJ,30,43,'T1')
        
        gen_special2(mapJ,1,34,'W2')
        gen_special2(mapJ,1,35,'W2')
        
        gen_special2(mapJ,1,23,'W3')
        gen_special2(mapJ,1,24,'W3')
        gen_special2(mapJ,7,35,'M3')
        gen_special2(mapJ,7,34,'M3')
        gen_special2(mapJ,26,19,'F3')
        gen_special2(mapJ,26,20,'F3')
        gen_special2(mapJ,30,19,'F3')
        gen_special2(mapJ,30,20,'F3')
        gen_special2(mapJ,36,27,'T3')
        gen_special2(mapJ,36,28,'T3')
        gen_special2(mapJ,36,29,'T3')
        gen_special2(mapJ,36,30,'T3')
        gen_special2(mapJ,36,31,'T3')
        gen_special2(mapJ,36,32,'T3')
        
        gen_special2(mapJ,1,14,'W4')
        gen_special2(mapJ,1,15,'W4')
        gen_special2(mapJ,7,23,'M4')
        gen_special2(mapJ,7,24,'M4')
        
        gen_special2(mapJ,1,1,'W5')
        gen_special2(mapJ,2,1,'W5')
        gen_special2(mapJ,1,2,'W5')
        gen_special2(mapJ,36,1,'M5')
        gen_special2(mapJ,35,1,'M5')
        gen_special2(mapJ,36,2,'M5')
        gen_special2(mapJ,30,7,'F5')
        gen_special2(mapJ,29,7,'F5')
        gen_special2(mapJ,30,8,'F5')
        
        gen_special2(mapJ,18,2,'W6')
        gen_special2(mapJ,19,2,'W6')
        gen_special2(mapJ,26,31,'T6')
        gen_special2(mapJ,26,32,'T6')
        gen_special2(mapJ,26,33,'T6')
        
        gen_special2(mapJ,18,15,'W7')
        gen_special2(mapJ,19,15,'W7')
        gen_special2(mapJ,15,16,'W7')
        gen_special2(mapJ,22,16,'W7')
        gen_special2(mapJ,18,7,'M7')
        gen_special2(mapJ,19,7,'M7')
        gen_special2(mapJ,18,11,'M7')
        gen_special2(mapJ,19,11,'M7')
        
        gen_special2(mapJ,22,24,'c3')
        gen_special2(mapJ,22,25,'c3')
        gen_special2(mapJ,22,26,'c3')
        gen_special2(mapJ,15,24,'c3')
        gen_special2(mapJ,15,25,'c3')
        gen_special2(mapJ,15,26,'c3')
        gen_special2(mapJ,16,19,'tc')
        gen_special2(mapJ,17,19,'ta')
        gen_special2(mapJ,18,19,'ts')
        gen_special2(mapJ,19,19,'ti')
        gen_special2(mapJ,20,19,'tn')
        gen_special2(mapJ,21,19,'to')
        
        gen_special2(mapJ,18,36,'g3')
        gen_special2(mapJ,19,36,'g3')
        gen_special2(mapJ,15,35,'g3')
        gen_special2(mapJ,22,35,'g3')
        gen_special2(mapJ,16,33,'tg')
        gen_special2(mapJ,17,33,'tu')
        gen_special2(mapJ,18,33,'ti')
        gen_special2(mapJ,19,33,'tl')
        gen_special2(mapJ,20,33,'td')
        gen_special2(mapJ,21,33,'ts')
        
        gen_special2(mapJ,17,34,'th')
        gen_special2(mapJ,18,34,'ta')
        gen_special2(mapJ,19,34,'tl')
        gen_special2(mapJ,20,34,'tl')
        
        gen_special2(mapJ,18,55,'tL')
        gen_special2(mapJ,19,55,'tL')
        return mapJ
    
    
