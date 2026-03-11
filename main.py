#Dawid Wachecki 254890
#Kacper Skoczylas 254864
#Zadanie 1: metoda bisekcji, reguła falsi, wariant A
import algorytmy as alg
#na początku programu niech narysuje tę funkcje na przedziale i dopiero potem te algorytmy
def petla(warunek, wyborFunkcji, a, b):
    if (warunek == 1):
        #spełnienie konkretnej dokładności
        dokladnosc = float(input("Podaj dokladnosc: "))
        a,b,x0,x1 = alg.bisekcja(wybranaFunkcja(wyborFunkcji), a, b)
        while (abs(x1-x0) > dokladnosc):
            a, b, x0, x1 = alg.bisekcja(wybranaFunkcja(wyborFunkcji), a, b)
    elif (warunek == 2):
        #konkretna liczba iteracji
        liczbaIter = int(input("Podaj liczbę iteracji: "))
        for i in range(liczbaIter):
            a,b = alg.bisekcja(wybranaFunkcja(wyborFunkcji), a, b)
    else:
        print("\nPodano błędną wartość")

def wybranaFunkcja(wyborFunkcji):
    if wyborFunkcji == 1:
        f = alg.wielomian
    elif wyborFunkcji == 2:
        f = alg.trygonometryczna
    elif wyborFunkcji == 3:
        f = alg.wykladnicza
    elif wyborFunkcji == 4:
        f = alg.zlozWielomianTryg
    elif wyborFunkcji == 5:
        f = alg.zlozTrygWykl
    elif wyborFunkcji == 6:
        f = alg.zlozWielomianWykl
    elif wyborFunkcji == 7:
        f = alg.zlozWszystko
    return f

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

    print("\n================================================")
    print("Miejsca zerowe będą poszukiwane w przedziale [a-b]")
    a = float(input("PODAJ WARTOŚĆ 'a': "))
    b = float(input("PODAJ WARTOŚĆ 'b': "))

    print("\n================================================")
    print("WYBIERZ KRYTERIUM ZATRZYMANIA ALGORYTMU")
    print("1. spełnienie warunku nałożonego na dokładność")
    print("2. osiągnięcie zadanej liczby iteracji")
    wyboruWarunku = int(input("WYBRANY WARUNEK: "))

    petla(wyboruWarunku, wyborFunkcji, a, b)

menu()
