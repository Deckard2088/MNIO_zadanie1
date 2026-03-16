from numpy import cos


#DEFINICJE PRZYKŁADOWE FUNKCJI
#wielomian obliczany metodą hornera
def horner(x, tablica_wspolczynnikow, dlugosc_tablicy):
    #Czyli zamiast np. y = 4*x*x*x + 3*x + 5 podaje się funkcje wielomian z argumentami: x, [4,0,3,5], 4
    y = tablica_wspolczynnikow[0]
    for i in range(1,dlugosc_tablicy,1):
        y = tablica_wspolczynnikow[i] + x * y
    return y

#przykładowy wielomian
def wielomian(x):
    #y = 4x^3 -6x^2 + 9x
    #y = horner(x, [4,-6,9,0], 4)
    y = horner(x, [1,-1,-2,1],4)
    return y

#skoro to taka prosta funkcja to może ją wywalić? i po prostu import math dać? jak tak to te złożone może też? albo zmienić na inne
def trygonometryczna(x):
    y = cos(x+6) + 0.5
    return y

def wykladnicza(x):
    #niby pow() zakazane, ale nikt nie powiedział, że x nie może być całkowite, więc chyba można korzystać?
    #y = 3.14 do potęgi x - 5
    y = (3.14)**x - 5
    return y

def zlozWielomianTryg(x):
    #y = cos(7x^3 - 6x + 6)
    y = trygonometryczna(horner(x, [7,0,-6,0], 4))
    return y

def zlozTrygWykl(x):
    #y = 3.14 do potęgi cos(x+6) - 1.5
    y = (3.14)**trygonometryczna(x) - 1.5
    return y

def zlozWielomianWykl(x):
    #y = 3.14 do potęgi (3x^5 + 9x^2 - 20)
    y = wykladnicza(horner(x, [3,0,0,9,0,-20],6))
    return y

def zlozWszystko(x):
    #y = cos(3.14 do potęgi (6x^2 - 7))
    y = trygonometryczna(wykladnicza(horner(x, [6,0,-7],3)))
    return y

def bisekcja(f,a,b):
    #x0 to przybliżenie miejsca zerowego, które wyznaczone jest z początkowych wartości a i b
    x0 = (a+b)/2
    #porównanie floata do zera inaczej?
    if (f(x0) == 0):
        return a, b, x0, x0
    elif (f(x0)*f(b) < 0):
        a = x0
    elif (f(x0)*f(a) < 0):
        b = x0

    #x1 to przybliżenie po przejściu przez algorytm, jeśli pierwiastek został znaleziony to x0 = x1
    x1 = (a+b)/2
    return a,b,x0,x1

def regulaFalsi(f,a,b):
    x0 = a - f(a)*(b-a)/(f(b)-f(a))
    #porównanie floata do zera inaczej?
    if (f(x0) == 0):
        return a,b,x0,x0
    elif (f(x0)*f(b) < 0):
        a = x0
    elif (f(x0)*f(a) < 0):
        b = x0
    x1 = a - f(a) * (b - a) / (f(b) - f(a))
    return a,b,x0,x1