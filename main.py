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
    print(f"| {'':>16} | {'METODA BISEKCJA':>16} | {'REGUŁA FALSI':>16}")
    print('=' * 57)
    print(f"| {'LICZBA ITERACJI':>16} | {iterB:>16} | {iterF:>16}")
    print('=' * 57)
    print(f"| {'PIERWIASTEK':>16} | {xB:>16} | {xF:>16}")
    print('=' * 57)

def podsumowanieInfoIteracje(dokB, dokF, xB, xF, iteracje):
    print("\nPODSUMOWANIE")
    print('=' * 57)
    print("WARUNEK: określona liczba iteracji")
    print('=' * 57)
    print("LICZBA ITERACJI: ", iteracje)
    print('=' * 57)
    print(f"| {'':>16} | {'METODA BISEKCJA':>16} | {'REGUŁA FALSI':>16}")
    print('=' * 57)
    print(f"| {'DOKŁADNOŚĆ':>16} | {dokB:>16} | {dokF:>16}")
    print('=' * 57)
    print(f"| {'PIERWIASTEK':>16} | {xB:>16} | {xF:>16}")
    print('=' * 57)

iterBis = []
iterFalsi = []

przyblizeniaBis = []
przyblizeniaFalsi = []

liczbEps = []


def uruchom_metode(metoda, f, a, b, warunek, dokladnosc, liczba_iter):
    lewy, prawy = a, b
    poprzednie_x = float('inf')
    aktualne_x = -float('inf')
    wykonane_iteracje = 0

    if warunek == 1:
        while abs(aktualne_x - poprzednie_x) > dokladnosc:
            poprzednie_x = aktualne_x
            lewy, prawy, aktualne_x = metoda(f, lewy, prawy)
            wykonane_iteracje += 1
    elif warunek == 2:
        for _ in range(liczba_iter):
            poprzednie_x = aktualne_x
            lewy, prawy, aktualne_x = metoda(f, lewy, prawy)
            wykonane_iteracje += 1
    else:
        return None

    osiagnieta_dokladnosc = abs(aktualne_x - poprzednie_x)
    return wykonane_iteracje, aktualne_x, osiagnieta_dokladnosc

#na początku programu niech narysuje tę funkcje na przedziale i dopiero potem te algorytmy
def petla(warunek, a, b, f, dokladnosc, liczbaIter, rysuj_wykres=True):
    wynik_bis = uruchom_metode(alg.bisekcja, f, a, b, warunek, dokladnosc, liczbaIter)
    wynik_falsi = uruchom_metode(alg.regulaFalsi, f, a, b, warunek, dokladnosc, liczbaIter)

    if wynik_bis is None or wynik_falsi is None:
        print("\nPodano błędną wartość")
        return

    iter_bis, x_bis, dok_bis = wynik_bis
    iter_falsi, x_falsi, dok_falsi = wynik_falsi

    if warunek == 1:
        iterBis.append(iter_bis)
        iterFalsi.append(iter_falsi)
        podsumowanieInfoDokladnosc(iter_bis, iter_falsi, x_bis, x_falsi, dokladnosc)
    elif warunek == 2:
        podsumowanieInfoIteracje(dok_bis, dok_falsi, x_bis, x_falsi, liczbaIter)

    przyblizeniaBis.append(x_bis)
    przyblizeniaFalsi.append(x_falsi)
    if rysuj_wykres:
        wyk.wykres_funkcji_z_miejscami_zerowymi(f, a, b, x_bis, x_falsi, "Funkcja")

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
    iterBis.clear()
    iterFalsi.clear()
    liczbEps.clear()
    przyblizeniaBis.clear()
    przyblizeniaFalsi.clear()

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
    if (wyborFunkcji < 1 or wyborFunkcji > 7):
        print("Błąd: wpisano niepoprawny numer.")
        return

    f = wybranaFunkcja(wyborFunkcji)

    print("\n================================================")
    print("Miejsca zerowe będą poszukiwane w przedziale [a-b]")
    a = float(input("PODAJ WARTOŚĆ 'a': "))
    b = float(input("PODAJ WARTOŚĆ 'b': "))

    #zabezpieczenie przedziału
    if (f(a)*f(b) >= 0):
        print("Podano nieprawidłowy przedział, nie da się wykorzystać metody bisekcji ani reguły Falsi")
        return

    print("\n================================================")
    print("WYBIERZ KRYTERIUM ZATRZYMANIA ALGORYTMU")
    print("1. spełnienie warunku nałożonego na dokładność")
    print("2. osiągnięcie zadanej liczby iteracji")
    wyboruWarunku = int(input("WYBRANY WARUNEK: "))
    dokladnosc = 0
    liczbaIter = 0

    if (wyboruWarunku == 1):
        dokladnosc = float(input("Podaj dokladnosc: "))
        if dokladnosc <= 0:
            print("Błąd: dokładność musi być dodatnia.")
            return
    elif (wyboruWarunku == 2):
        liczbaIter = int(input("Podaj liczbę iteracji: "))
        if liczbaIter <= 0:
            print("Błąd: liczba iteracji musi być dodatnia.")
            return

    petla(wyboruWarunku, a, b, f, dokladnosc, liczbaIter)
    iterBis.clear()
    iterFalsi.clear()
    liczbEps.clear()

    #w pętli uruchamiamy funkcję petla(), z warunkiem na dokładność, gdzie każda dokładność jest 10 większa
    #następnie wyświetlamy liczbę iteracji obu metod dla każdej z tych dokładności
    for i in range (1,10):
        petla(1, a, b, f, 10**-i, liczbaIter, rysuj_wykres=False)
        liczbEps.append(10**-i)
    wyk.wykres_porownanie_iteracji(liczbEps, iterBis, iterFalsi)
'''
    for i in range (1,10):
        petla(2, a, b, f, dokladnosc, i)
    wyk.wykres_zbieznosci(przyblizeniaBis, przyblizeniaFalsi)
'''
menu()