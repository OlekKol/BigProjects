import keyboard
import os
import math
import time
class Move():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def map_whole(self):
        def gen_mapa(mapa, dim_x, dim_y):    
            for y in range(dim_y):
                line = []
                for x in range(dim_x):
                    line.append('0')
                mapa.append (line)
                
        def gen_sqare(mapa, x1, y1, x2, y2, kind):
            # w --> woods
            # m --> mountains
            n = 0
            if kind == "w":
                n += 1
            elif kind == "m":
                n += 2
            
            for y in range(y1-1, y2):
                for x in range(x1-1, x2):
                    mapa[y][x] = str(n)

        def print_mapa(mapa):
            for w in range(len(mapa)):
                line = ''
                for k in range(len(mapa[w])):
                    line += mapa[w][k]
                print(line)

        
        def move(mapa):
            def print_pos_acc(mapa, x, y, rd):                
                blocks = {
                    "You":chr(int('0xC6C3' , 16)),
                    'Border':chr(int('0x2B1B', 16)),
                    'Grass':chr(int('0x1F7E9', 16)),
                    'Woods':chr(int('0x1F332', 16)),
                    'Mountains': '🪨 '
                }
                dim_w = len(mapa)
                dim_k = len(mapa[0])
                os.system('clear')
                for w in range(y - rd, y + rd + 1):
                    line = ''
                    for k in range(x - rd, x + rd + 1):
                        if w == y and k == x:
                            line += blocks['You'] # You
                        elif w < 0 or w >= dim_w or k < 0 or k >= dim_k:
                            line += blocks['Border'] # Border  
                        elif mapa[w][k] == "1":
                            line += blocks['Woods'] # Woods
                        elif mapa[w][k] == "2":
                            line += blocks['Mountains'] # Mountains
                        else:
                            line += blocks['Grass'] # Grass
                    print(line)
                    
                print(f"x - {x}")
                print(f"y - {y}")
                
            def awds(x, y):
                time.sleep(0.01)
                key = ''
                
                key = keyboard.read_key()
                if keyboard.is_pressed('w'):
                    if y - 1 >= 0:
                        return ("-1")
                elif keyboard.is_pressed('s'): 
                    if y + 1 <= 55:
                        return "1"
                elif keyboard.is_pressed('a'): 
                    if x - 1 >= 0:
                        return "-10"
                elif keyboard.is_pressed('d'): 
                    if x + 1 <= 37:
                        return "10"
                elif keyboard.is_pressed('x'): 
                    return 'x'
                # else:
                #     key = 'x'
                
            print('')
            
            rd = 4
            x = 0
            y = 0
            c = ''
            print_pos_acc(mapa, x, y, rd)
            while c != 'x':
                c = awds(x, y)
                if c == "-1":
                    y -= 1
                elif c == '1':
                    y += 1
                elif c == '-10':
                    x -= 1
                elif c == '10':
                    x += 1
                elif c == 'x':
                    break
                print_pos_acc(mapa, x, y, rd)
            
         
        gen_mapa(mapa, 38, 56)
        gen_sqare(mapa, 2, 2, 5, 6, 'w')
        gen_sqare(mapa, 14, 5, 34, 8, 'm')
        print_mapa(mapa)
        move(mapa)
        
        

mapa = []
             


import os
os.system('clear')
M = Move(22,16)
M.map_whole()