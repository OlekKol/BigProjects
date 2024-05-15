from kira import Kira
from jufen import Jufen
from sunui import Sunui
from hasitis import Hasitis
from lacai import Lacai
from vitisuri import Vitisuri



import os
K = Kira()

S = Sunui()

J = Jufen()

H = Hasitis()

L = Lacai()

V = Vitisuri()

def Moving_between_files(file):
    os.system('cls')
    if file == 'jufen':
        answer = J.do_you_whant_enter()
        print(answer)
        return answer
    elif file == 'kira':
        answer = K.do_you_whant_enter()
        print(answer)
        return answer
    elif file == 'sunui':
        answer = S.do_you_whant_enter()
        print(answer)
        return answer
    elif file == 'hasitisi':
        answer = H.do_you_whant_enter()
        print(answer)
        return answer
    elif file == 'lacai':
        answer = L.do_you_whant_enter()
        print(answer)
        return answer
    elif file == 'vitisuri':
        answer = V.do_you_whant_enter()
        print(answer)
        return answer
def Generators(file,lvl):
    if file == 'jufen':
        g = J.Jufen_kingdom_generator()
        return g
    elif file == 'kira':
        g = K.Kira_kingdom_generator()
        return g
    elif file == 'sunui':
        g = S.Sunui_kingdom_generator()
        return g
    elif file == 'hasitisi':
        g = H.Hasitisi_Dungeon_generator(lvl)
        return g
    elif file == 'lacai':
        g = L.Lacai_Dungeon_generator(lvl)
        return g
    elif file == 'vitisuri':
        g = V.Vitisuri_Dungeon_generator(lvl)
        return g
    
    