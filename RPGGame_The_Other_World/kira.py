import choice
class Kira():
    def __init__(self) -> None:
        pass
    def do_you_whant_enter(self):
        Y_N = ['No', 'Yes']
        answer = choice.WybierzZListy(Y_N, 'Do you whant to enter Kira? ')
        print (answer)
        return answer
    def info (self):
        print("Kira - Kingdom")
    def Kira_kingdom_generator(mapK):
        mapK = []
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
        
        gen_map(mapK, 39, 56)
        gen_square(mapK,16,46,21,55,'r')
        gen_square(mapK,4,46,15,50,'r')
        gen_square(mapK,4,3,8,45,'r')
        gen_square(mapK,9,3,38,7,'r')
        gen_square(mapK,16,8,19,38,'r')
        gen_square(mapK,28,8,30,55,'r')
        gen_square(mapK,22,53,27,55,'r')
        
        gen_square(mapK,6,51,10,53,'s')
        gen_square(mapK,13,51,15,53,'s')
        gen_square(mapK,22,50,24,52,'s')
        gen_square(mapK,1,44,3,48,'s')
        gen_square(mapK,9,42,12,45,'s')
        gen_square(mapK,9,31,11,40,'s')
        gen_square(mapK,1,31,3,40,'s')
        gen_square(mapK,1,0,3,27,'s')
        gen_square(mapK,4,0,6,2,'s')
        gen_square(mapK,9,8,15,14,'s')
        gen_square(mapK,9,16,15,27,'s')
        gen_square(mapK,12,0,19,2,'s')
        gen_square(mapK,22,0,29,2,'s')
        gen_square(mapK,20,8,27,11,'s')
        gen_square(mapK,20,13,27,14,'s')
        gen_square(mapK,20,16,27,37,'s')
        gen_square(mapK,25,39,27,49,'s')
        gen_square(mapK,31,13,35,20,'s')
        gen_square(mapK,31,22,35,29,'s')
        gen_square(mapK,31,8,38,11,'s')
        
        gen_special2(mapK,8,51,'W1')
        gen_special2(mapK,3,46,'M1')
        gen_special2(mapK,15,51,'F1')
        gen_special2(mapK,22,52,'T1')
        gen_special2(mapK,23,52,'T1')
        gen_special2(mapK,22,51,'T1')
        
        gen_special2(mapK,9,45,'W2')
        gen_special2(mapK,10,45,'W2')
        gen_special2(mapK,11,45,'W2')
        gen_special2(mapK,9,44,'W2')
        gen_special2(mapK,9,43,'W2')
        
        gen_special2(mapK,3,34,'W3')
        gen_special2(mapK,3,35,'W3')
        gen_special2(mapK,3,36,'W3')
        gen_special2(mapK,3,37,'W3')
        gen_special2(mapK,9,34,'M3')
        gen_special2(mapK,9,35,'M3')
        gen_special2(mapK,9,36,'M3')
        gen_special2(mapK,9,37,'M3')
        gen_special2(mapK,9,18,'F3')
        gen_special2(mapK,9,19,'F3')
        gen_special2(mapK,9,20,'F3')
        gen_special2(mapK,9,21,'F3')
        gen_special2(mapK,9,22,'F3')
        gen_special2(mapK,9,23,'F3')
        gen_special2(mapK,9,24,'F3')
        gen_special2(mapK,9,25,'F3')
        gen_special2(mapK,3,2,'T3')
        gen_special2(mapK,4,2,'T3')
        gen_special2(mapK,3,3,'T3')
        gen_special2(mapK,3,23,'T3')
        gen_special2(mapK,3,24,'T3')
        gen_special2(mapK,3,25,'T3')
        
        gen_special2(mapK,15,2,'W4')
        gen_special2(mapK,16,2,'W4')
        gen_special2(mapK,25,2,'M4')
        gen_special2(mapK,26,2,'M4')
        
        gen_special2(mapK,20,13,'W5')
        gen_special2(mapK,20,14,'W5')
        gen_special2(mapK,27,13,'M5')
        gen_special2(mapK,27,14,'M5')
        gen_special2(mapK,9,8,'F5')
        gen_special2(mapK,10,8,'F5')
        gen_special2(mapK,9,9,'F5')
        
        gen_special2(mapK,27,45,'W6')
        gen_special2(mapK,27,44,'W6')
        gen_special2(mapK,27,43,'W6')
        gen_special2(mapK,31,8,'T6')
        gen_special2(mapK,32,8,'T6')
        gen_special2(mapK,31,9,'T6')
        
        gen_special2(mapK,31,16,'W7')
        gen_special2(mapK,31,17,'W7')
        gen_special2(mapK,31,25,'M7')
        gen_special2(mapK,31,26,'M7')
        
        gen_special2(mapK,27,17,'c3')
        gen_special2(mapK,27,18,'c3')
        gen_special2(mapK,20,17,'c3')
        gen_special2(mapK,20,18,'c3')
        gen_special2(mapK,20,35,'c3')
        gen_special2(mapK,20,36,'c3')
        gen_special2(mapK,27,35,'c3')
        gen_special2(mapK,27,36,'c3')
        gen_special2(mapK,23,8,'g3')
        gen_special2(mapK,24,8,'g3')
        
        gen_special2(mapK,21,16,'tc')
        gen_special2(mapK,22,16,'ta')
        gen_special2(mapK,23,16,'ts')
        gen_special2(mapK,24,16,'ti')
        gen_special2(mapK,25,16,'tn')
        gen_special2(mapK,26,16,'to')
        
        gen_special2(mapK,21,10,'tg')
        gen_special2(mapK,22,10,'tu')
        gen_special2(mapK,23,10,'ti')
        gen_special2(mapK,24,10,'tl')
        gen_special2(mapK,25,10,'td')
        gen_special2(mapK,26,10,'ts')
        gen_special2(mapK,22,11,'th')
        gen_special2(mapK,23,11,'ta')
        gen_special2(mapK,24,11,'tl')
        gen_special2(mapK,25,11,'tl')
        
        gen_special2(mapK,18,55,'tL')
        gen_special2(mapK,19,55,'tL')
        return mapK