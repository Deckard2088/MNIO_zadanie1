#Dawid Wachecki 254890
#Kacper Skoczylas 254864
#Zadanie 1: metoda bisekcji, reguła falsi, wariant A

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
    wyborFunkcji = input("WYBRANA FUNKCJA: ")

    print("\n================================================")
    print("Miejsca zerowe będą poszukiwane w przedziale [a-b]")
    a = input("PODAJ WARTOŚĆ 'a': ")
    b = input("PODAJ WARTOŚĆ 'b': ")

    print("\n================================================")
    print("WYBIERZ KRYTERIUM ZATRZYMANIA ALGORYTMU")
    print("1. spełnienie warunku nałożonego na dokładność")
    print("2. osiągnięcie zadanej liczby iteracji")
    wyboruWarunku = input("WYBRANY WARUNEK: ")

#jak to by zrobić najbardziej optymalnie?
#osobna funkcja z instukcją warunkową co do kryterium zatrzymania algorytmu?
#tylko przy założeniu że ten algorytm bisekcji robimy jako osobną funkcje to jak uwzględnić ten wybór?
#po prostu instrukcja warunkowa w głównej pętli?
#chyba że właśnie nie bo dla jednej wersji byłałby pętla while a dla drugiej pętla for to może
#instrukcja warunkowa z tymi pętlami i dopiero wewnątrz zdefiniowana bisekcja?

menu()
