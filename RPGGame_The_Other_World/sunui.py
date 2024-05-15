import choice
class Sunui():
    def __init__(self) -> None:
        pass
    def do_you_whant_enter(self):
        Y_N = ['No', 'Yes']
        answer = choice.WybierzZListy(Y_N, 'Do you whant to enter Sunui? ')
        print (answer)
        return answer
    def info(self):
        print("Sunui - Kingdom")
    def Sunui_kingdom_generator(mapS):
        mapS = []
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
                    
                    
        gen_map(mapS, 39, 56)
        #
        #
        gen_square(mapS,0,5,15,9,'r')
        gen_square(mapS,21,46,38,48,'r')
        gen_square(mapS,21,34,38,36,'r')
        #
        #
        gen_square(mapS,21,13,28,15,'r')
        gen_square(mapS,8,10,10,35,'r')
        gen_square(mapS,0,27,15,29,'r')
        gen_square(mapS,3,33,10,35,'r')
        gen_square(mapS,3,36,5,55,'r')
        
        gen_square(mapS,26,49,32,50,'s')
        gen_square(mapS,26,44,32,45,'s')
        gen_square(mapS,14,44,15,50,'s')
        gen_square(mapS,21,43,23,45,'s')
        gen_square(mapS,21,49,23,51,'s')
        gen_square(mapS,14,37,15,43,'s')
        gen_square(mapS,25,37,33,39,'s')
        gen_square(mapS,21,30,28,33,'s')
        gen_square(mapS,32,30,35,33,'s')
        gen_square(mapS,26,21,28,27,'s')
        gen_square(mapS,32,21,34,27,'s')
        gen_square(mapS,25,2,35,12,'s')
        
        ##
        gen_square(mapS,29,6,31,33,'r')
        ##
        
        gen_square(mapS,18,2,23,7,'s')
        
        ##
        gen_square(mapS,16,5,20,55,'r')
        ##
        
        gen_square(mapS,6,36,9,42,'s')
        gen_square(mapS,1,31,2,42,'s')
        gen_square(mapS,3,31,7,32,'s')
        gen_square(mapS,13,21,15,25,'s')
        gen_square(mapS,11,11,13,19,'s')
        gen_square(mapS,14,14,15,16,'s')
        gen_square(mapS,5,12,7,20,'s')
        gen_square(mapS,1,2,5,4,'s')
        gen_square(mapS,9,2,13,4,'s')
        
        gen_special2(mapS,29,49,'W1')
        gen_special2(mapS,29,45,'M1')
        gen_special2(mapS,15,47,'F1')
        gen_special2(mapS,21,45,'T1')
        gen_special2(mapS,21,45,'T1')
        
        gen_special2(mapS,15,40,'W2')
        
        gen_special2(mapS,32,24,'W3')
        gen_special2(mapS,28,24,'M3')
        gen_special2(mapS,28,37,'F3')
        gen_special2(mapS,29,37,'F3')
        gen_special2(mapS,30,37,'F3')
        gen_special2(mapS,32,32,'T3')
        
        gen_special2(mapS,7,32,'W4')
        gen_special2(mapS,2,32,'W4')
        gen_special2(mapS,3,32,'W4')
        gen_special2(mapS,2,31,'W4')
        gen_special2(mapS,2,41,'W4')
        gen_special2(mapS,7,36,'M4')
        gen_special2(mapS,7,37,'M4')
        gen_special2(mapS,6,36,'M4')
        gen_special2(mapS,6,37,'M4')
        
        gen_special2(mapS,7,19,'W5')
        gen_special2(mapS,7,13,'M5')
        gen_special2(mapS,11,11,'F5')
        gen_special2(mapS,11,18,'F5')
        gen_special2(mapS,15,15,'F5')
        
        gen_special2(mapS,15,23,'W6')
        gen_special2(mapS,21,4,'T6')
        gen_special2(mapS,20,4,'T6')
        gen_special2(mapS,20,5,'T6')
        
        gen_special2(mapS,3,4,'W7')
        gen_special2(mapS,11,4,'M7')
        
        gen_special2(mapS,30,5,'c3')
        gen_special2(mapS,32,11,'c3')
        gen_special2(mapS,28,11,'c3')
        gen_special2(mapS,25,33,'g3')
        gen_special2(mapS,24,33,'g3')
        
        gen_special2(mapS,25,2,'tc')
        gen_special2(mapS,27,2,'ta')
        gen_special2(mapS,29,2,'ts')
        gen_special2(mapS,31,2,'ti')
        gen_special2(mapS,33,2,'tn')
        gen_special2(mapS,35,2,'to')
        
        gen_special2(mapS,22,30,'tg')
        gen_special2(mapS,23,30,'tu')
        gen_special2(mapS,24,30,'ti')
        gen_special2(mapS,25,30,'tl')
        gen_special2(mapS,26,30,'td')
        gen_special2(mapS,27,30,'ts')
        
        gen_special2(mapS,23,31,'th')
        gen_special2(mapS,24,31,'ta')
        gen_special2(mapS,25,31,'tl')
        gen_special2(mapS,26,31,'tl')  
        
        gen_special2(mapS,18,55,'tL')
        return mapS