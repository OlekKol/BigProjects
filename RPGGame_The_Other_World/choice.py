
import time

from colorama import Fore, Back, Style
OchronaKodu = True


def WybierzZListy(lista, pytanie, szer = 50):
        print('')
        print('')
        print(pytanie)
        print('')
        print('')

        wybor = 0
    
    # if OchronaKodu: 
    #     keyboard.press_and_release('ctrl+`')
        # while keyboard.is_pressed('enter'): 
        #     print ("Puść [Enter]\033[A")
        if lista[0] == [0, "nic", 0, 0, 0]:
            for i in range(len(lista)):
                if lista [0][1] == "nic":
                    while True:
                        print("\033[A" * (len(lista) + 1)) ## Przesuwa kursor do góry
                        P_Gems = 10
                        d = 0
                        if lista[i][0] <= 8:
                            while d < lista[i][2]:
                                        
                                if lista[i][2] > 30 and d >  d % 5 == 0:
                                    P_Gems += 1
                                elif lista[i][2] < 20 and d == 0 :
                                    P_Gems -= 5
                                d += 1
                        elif lista[i][0] >= 9:
                            while d < lista[i][2]:
                                        
                                if lista[i][2] > 10 and d >  d % 5 == 0:
                                    P_Gems += 1
                                elif lista[i][2] < 6 and d == 0 :
                                    P_Gems -= 5
                                d += 1        
                        for i in range(len(lista)):
                            if wybor == i:
                                print(f"{Fore.BLACK + Back.WHITE }{(lista[i][0], lista[i][1], lista[i][2])} - Cena {lista[i][2] * P_Gems} Gems {Fore.WHITE + Back.BLACK}")
                            else:
                                print ((f"{lista[i][0], lista[i][1], lista[i][2]} - Cena {lista[i][2] * P_Gems} Gems").ljust(szer))
                        key = input('>w< or >s< or >etr<')
                        
                        if key == 'w':  
                            if wybor > 0:
                                wybor -= 1
                        elif key == 's': 
                            if wybor < len(lista)-1:
                                wybor += 1
                        elif key == 'etr': 
                            break
                    return wybor
        
        else:
            while True: 
                print("\033[A" * (len(lista) + 1)) ## Przesuwa kursor do góry
                lista_stringow = []
                for i in lista:
                    if i != str:
                        i = str(i)
                        lista_stringow.append(i)
                if len(lista_stringow) > 0:
                    lista = lista_stringow
                for i in range(len(lista)):
                    if wybor == i:
                        print(Fore.BLACK + Back.WHITE + lista[i].ljust(szer) + Fore.WHITE + Back.BLACK)
                    else:
                        print(lista[i].ljust(szer))



                key = input('>w< or >s< or >etr<')
                        
                if key == 'w':  
                    if wybor > 0:
                        wybor -= 1
                elif key == 's': 
                    if wybor < len(lista)-1:
                        wybor += 1
                elif key == 'etr': 
                    break

            
            return wybor