from numpy import cos

EPS_ZERO = 1e-12

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
    #y = 2x^3 - 5x^2 + 2x
    y = horner(x, [2,-5,2,0],4)
    return y

#skoro to taka prosta funkcja to może ją wywalić? i po prostu import math dać? jak tak to te złożone może też? albo zmienić na inne
def trygonometryczna(x):
    y = cos(x+6) + 0.5
    return y

def wykladnicza(x):
    #y = 3.14 do potęgi x - 5
    y = (3.14)**x - 5
    return y

def zlozWielomianTryg(x):
    #y = cos((0.5x^3 + 2x^2) + 6) + 0.5
    y = trygonometryczna(horner(x, [0.5,2,0,0], 4))
    return y

def zlozTrygWykl(x):
    #y = 3.14^(cos(x+6) + 0.5) - 2
    y = wykladnicza(trygonometryczna(x)) + 3
    return y

def zlozWielomianWykl(x):
    #y = 3.14^(x^3 + 3x^2 + x) - 5
    y = wykladnicza(horner(x, [1,3,1,0],4))
    return y

def zlozWszystko(x):
    #y = 3.14^(cos((0.5x^3 + 0.6x^2) + 6) + 0.5) - 2
    y = wykladnicza(trygonometryczna(horner(x, [0.1, 0.6, 0, 0], 4))) + 3
    return y

def bisekcja(f,a,b):
    """Wykonuje jeden krok metody bisekcji i zwraca nowe (a, b, x)."""
    x = (a + b) / 2
    fx = f(x)
    if abs(fx) <= EPS_ZERO:
        return a, b, x

    fa = f(a)
    if fa * fx < 0:
        b = x
    else:
        a = x

    return a, b, x

def regulaFalsi(f,a,b):
    """Wykonuje jeden krok regula falsi i zwraca nowe (a, b, x)."""
    fa = f(a)
    fb = f(b)
    mianownik = fb - fa
    if abs(mianownik) <= EPS_ZERO:
        x = (a + b) / 2
        return a, b, x

    # Klasyczny wzor regula falsi: przeciecie siecznej z osia OX.
    x = a - fa * (b - a) / mianownik
    fx = f(x)
    if abs(fx) <= EPS_ZERO:
        return a, b, x

    if fa * fx < 0:
        b = x
    else:
        a = x

    return a, b, x