from math import cos

#DEFINICJE PRZYKŁADOWE FUNKCJI
#wielomian obliczany metodą hornera
def wielomian(x, tablica_wspolczynnikow, dlugosc_tablicy):
    #Czyli zamiast np. y = 4*x*x*x + 3*x + 5 podaje się funkcje wielomian z argumentami: x, [4,0,3,5], 4
    y = tablica_wspolczynnikow[0]
    for i in range(1,dlugosc_tablicy,1):
        y = tablica_wspolczynnikow[i] + x * y
    return y

#skoro to taka prosta funkcja to może ją wywalić? i po prostu import math dać? jak tak to te złożone może też? albo zmienić na inne
def trygonometryczna(x):
    y = cos(x)
    return y

def wykladnicza(x):
    #niby pow() zakazane, ale nikt nie powiedział, że x nie może być całkowite, więc chyba można korzystać?
    #y = 3.14 do potęgi x
    y = (3.14)**x
    return y

def zlozWielomianTryg(x):
    #y = cos(7x^3 - 6x)
    y = trygonometryczna(wielomian(x, [7,0,0,-6,0], 5))
    return y

def zlozTrygWykl(x):
    #y = 3.14 do potęgi cosinus x
    y = wykladnicza(trygonometryczna(x))
    return y

def zlozWielomianWykl(x):
    #y = 3.14 do potęgi (3x^5 + 9x^2 - 20)
    y = wykladnicza(wielomian(x, [3,0,0,9,0,-20],6))
    return y

def zlozWszystko(x):
    #y = cos(3.14 do potęgi (6x^2 - 7))
    y = trygonometryczna(wykladnicza(wielomian(x, [6,0,-7],3)))
    return y

def bisekcja(f,a,b):

    return 0