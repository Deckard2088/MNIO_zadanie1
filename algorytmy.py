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