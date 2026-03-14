#Dawid Wachecki 254890
#Kacper Skoczylas 254864
#Zadanie 1: metoda bisekcji, reguła falsi, wariant A
import algorytmy as alg
import wykresy as wyk

def podsumowanieInfoDokladnosc(iterB, iterF, xB, xF, dokladnosc):
    print("\nPODSUMOWANIE")
    print('=' * 57)
    print("WARUNEK: określona dokładność")
    print('=' * 57)
    print("DOKŁADNOŚĆ: ", dokladnosc)
    print('=' * 57)
    print(f"| {'':>16} | {'METODA BISEKCJA':>16} | {'REGUŁA FALSI':>16}|")
    print('=' * 57)
    print(f"| {'LICZBA ITERACJI':>16} | {iterB:>16} | {iterF:>16}|")
    print('=' * 57)
    print(f"| {'PIERWIASTEK':>16} | {xB:>16} | {xF:>16}|")
    print('=' * 57)
    input("")

def podsumowanieInfoIteracje(dokB, dokF, xB, xF, iteracje):
    print("\nPODSUMOWANIE")
    print('=' * 57)
    print("WARUNEK: określona liczba iteracji")
    print('=' * 57)
    print("LICZBA ITERACJI: ", iteracje)
    print('=' * 57)
    print(f"| {'':>16} | {'METODA BISEKCJA':>16} | {'REGUŁA FALSI':>16}|")
    print('=' * 57)
    print(f"| {'DOKŁADNOŚĆ':>16} | {dokB:>16} | {dokF:>16}|")
    print('=' * 57)
    print(f"| {'PIERWIASTEK':>16} | {xB:>16} | {xF:>16}|")
    print('=' * 57)

#na początku programu niech narysuje tę funkcje na przedziale i dopiero potem te algorytmy
def petla(warunek, a, b, f):
    if (warunek == 1):
        #spełnienie konkretnej dokładności
        dokladnosc = float(input("Podaj dokladnosc: "))
        #METODA BISEKCJI
        aBis, bBis = a, b
        x0 = float('inf')
        x1 = -float('inf')
        liczbaIterBi = 0
        while (abs(x1-x0) > dokladnosc):
            aBis, bBis, x0, x1 = alg.bisekcja(f, aBis, bBis)
            liczbaIterBi += 1

        #REGULA FELASI
        aFal, bFal = a, b
        xf0 = float('inf')
        xf1 = -float('inf')
        liczbaIterFal = 0
        while (abs(xf1-xf0) > dokladnosc):
            aFal, bFal, xf0, xf1 = alg.regulaFalsi(f, aFal, bFal)
            liczbaIterFal += 1
        podsumowanieInfoDokladnosc(liczbaIterBi,liczbaIterFal, x1, xf1, dokladnosc)

    elif (warunek == 2):
        #konkretna liczba iteracji
        liczbaIter = int(input("Podaj liczbę iteracji: "))
        aBis, bBis = a, b
        aFal, bFal = a, b
        x0, x1, xf0, xf1 = float('inf'), -float('inf'), float('inf'), -float('inf')
        for i in range(liczbaIter):
            aBis, bBis, x0, x1 = alg.bisekcja(f, aBis, bBis)
            aFal, bFal, xf0, xf1 = alg.regulaFalsi(f, aFal, bFal)
        dokladnoscBisekcja = abs(x1-x0)
        dokladnoscFalsi = abs(xf1-xf0)
        podsumowanieInfoIteracje(dokladnoscBisekcja, dokladnoscFalsi, x1, xf1, liczbaIter)
    else:
        print("\nPodano błędną wartość")
    wyk.wykres_funkcji_z_miejscami_zerowymi(f, a, b, x1, xf1, "Funkcja")

#wybór funkcji wcześniej był realizowany przez instukcję warunkową if, zastąpiono na słownik
def wybranaFunkcja(wybor):
    funkcje = {
        1: alg.wielomian,
        2: alg.trygonometryczna,
        3: alg.wykladnicza,
        4: alg.zlozWielomianTryg,
        5: alg.zlozTrygWykl,
        6: alg.zlozWielomianWykl,
        7: alg.zlozWszystko
    }
    return funkcje.get(wybor)

def menu():
    print("================================================")
    print("ZADANIE 1.")
    print("================================================\n")
    print("WYBIERZ FUNKCJĘ NIELINIOWĄ:")
    #nazwy zamienić na konkretne funkcje (chyba)
    print("1. wielomian")
    print("2. trygonometryczna")
    print("3. wykładnicza")
    print("4. złożenie wielomianu i trygonometrycznej")
    print("5. złozenie trygonometrycznej i wykładniczej")
    print("6. złozenie wielomianu i wykładniczej")
    print("7. złozenie wszystkich trzech\n")
    wyborFunkcji = int(input("WYBRANA FUNKCJA: "))
    f = wybranaFunkcja(wyborFunkcji)

    print("\n================================================")
    print("Miejsca zerowe będą poszukiwane w przedziale [a-b]")
    a = float(input("PODAJ WARTOŚĆ 'a': "))
    b = float(input("PODAJ WARTOŚĆ 'b': "))

    #zabezpieczenie przedziału
    if (f(a)*f(b) >= 0):
        print("Podano nieprawidłowy przedział, nie da się wykorzystać metody bisekcji ani reguły Falesi")
        return

    print("\n================================================")
    print("WYBIERZ KRYTERIUM ZATRZYMANIA ALGORYTMU")
    print("1. spełnienie warunku nałożonego na dokładność")
    print("2. osiągnięcie zadanej liczby iteracji")
    wyboruWarunku = int(input("WYBRANY WARUNEK: "))

    petla(wyboruWarunku, a, b, f)

while True:
    menu()
