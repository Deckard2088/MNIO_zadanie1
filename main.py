#Dawid Wachecki 254890
#Kacper Skoczylas 254864
#Zadanie 1: metoda bisekcji, reguła falsi, wariant A
import algorytmy as alg
import wykresy as wyk

def podsumowanieInfoDokladnosc(a,b, iterB, iterF, xB, xF, dokladnosc):
    print("\nPODSUMOWANIE")
    print('=' * 57)
    print("ZAKRES: [",a,",",b,"]")
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

def podsumowanieInfoIteracje(a,b,dokB, dokF, xB, xF, iteracje):
    print("\nPODSUMOWANIE")
    print('=' * 57)
    print("ZAKRES: [", a, ",", b, "]")
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
def petla(warunek, a, b, f, nazwa, dokladnosc, liczbaIter, rysuj_wykres=True):
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
        if rysuj_wykres:
            podsumowanieInfoDokladnosc(a,b,iter_bis, iter_falsi, x_bis, x_falsi, dokladnosc)
    elif warunek == 2:
        if rysuj_wykres:
            podsumowanieInfoIteracje(a,b,dok_bis, dok_falsi, x_bis, x_falsi, liczbaIter)

    przyblizeniaBis.append(x_bis)
    przyblizeniaFalsi.append(x_falsi)
    if rysuj_wykres:
        wyk.wykres_funkcji_z_miejscami_zerowymi(f, a, b, x_bis, x_falsi, nazwa)

#wybór funkcji jako słownik, gdzie kluczem jest numer funkcji, a wartością jest sama funkcja. 
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

def nazwaFunkcji(wybor):
    nazwa = {
        1: "2x^3 - 5x^2 + 2x",
        2: "cos(x+6) + 0.5",
        3: "3.14^(x) - 5",
        4: "cos((0.5x^3 + 2x^2) + 6) + 0.5",
        5: "3.14^(cos(x+6) + 0.5) - 2",
        6: "3.14^(x^3 + 3x^2 + x) - 5",
        7: "3.14^(cos((0.1x^3 + 0.6x^2) + 6) + 0.5) - 2"
    }
    return nazwa.get(wybor)

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
    print("1. Wielomian: y = 2x^3 - 5x^2 + 2x")
    print("2. Trygonometryczna: y = cos(x+6) + 0.5")
    print("3. Wykładnicza: y = 3.14^(x) - 5")
    print("4. Złożenie wielomianu i trygonometrycznej: y = cos((0.5x^3 + 2x^2) + 6) + 0.5")
    print("5. Złozenie trygonometrycznej i wykładniczej: y = 3.14^(cos(x+6) + 0.5) - 2")
    print("6. Złozenie wielomianu i wykładniczej: y = 3.14^(x^3 + 3x^2 + x) - 5")
    print("7. Złozenie wszystkich trzech: y = 3.14^(cos((0.1x^3 + 0.6x^2) + 6) + 0.5) - 2\n")
    wyborFunkcji = int(input("WYBRANA FUNKCJA: "))
    if (wyborFunkcji < 1 or wyborFunkcji > 7):
        print("Błąd: wpisano niepoprawny numer.")
        return

    f = wybranaFunkcja(wyborFunkcji)
    wyk.wykres_funkcji_z_miejscami_zerowymi(f, None, None, None, None, nazwaFunkcji(wyborFunkcji), zakres=(-6,6))

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

    petla(wyboruWarunku, a, b, f, nazwaFunkcji(wyborFunkcji), dokladnosc, liczbaIter)
    iterBis.clear()
    iterFalsi.clear()
    liczbEps.clear()

    #w pętli uruchamiamy funkcję petla(), z warunkiem na dokładność, gdzie każda dokładność jest 10 większa
    #następnie wyświetlamy liczbę iteracji obu metod dla każdej z tych dokładności
    for i in range (1,10):
        petla(1, a, b, f, "", 10**-i, liczbaIter, False)
        # ładne jednolite formatowanie dla dokładności
        liczbEps.append(f"$10^{{-{i}}}$")
    wyk.wykres_porownanie_iteracji(liczbEps, iterBis, iterFalsi)

menu()