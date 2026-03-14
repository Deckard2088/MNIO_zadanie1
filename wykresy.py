import numpy as np
import matplotlib.pyplot as plt


def wykres_funkcji_z_miejscami_zerowymi(f, a, b, zero_bis, zero_rf, nazwa_funkcji):
    """Rysuje wykres funkcji z zaznaczonymi miejscami zerowymi obu metod.
    Automatycznie dopasowanie zakresy osi do wartości funkcji.

    Parametry:
        f              - funkcja f(x)
        a, b           - krańce przedziału
        zero_bis       - miejsce zerowe znalezione bisekcją
        zero_rf        - miejsce zerowe znalezione falsi
        nazwa_funkcji  - nazwa/opis funkcji - tytul i legenda
    """
    margines = (b - a) * 0.1
    x = np.linspace(a - margines, b + margines, 500)
    y = f(x)

    y_finite = y[np.isfinite(y)]
    if len(y_finite) > 0:
        y_min, y_max = np.min(y_finite), np.max(y_finite)
        y_zakres = y_max - y_min if y_max != y_min else 1.0
        y_pad = y_zakres * 0.15
    else:
        y_min, y_max, y_pad = -1, 1, 0.2

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {nazwa_funkcji}')
    plt.axhline(y=0, color='k', linewidth=0.5)
    if a <= 0 <= b:
        plt.axvline(x=0, color='k', linewidth=0.5)

    plt.axvline(x=a, color='orange', linestyle='--', linewidth=1.5, label=f'Przedział [a={a}, b={b}]')
    plt.axvline(x=b, color='orange', linestyle='--', linewidth=1.5)

    plt.plot(zero_bis, f(zero_bis), 'ro', markersize=10, zorder=5,
             label=f'Bisekcja: x = {zero_bis:.6f}')
    plt.plot(zero_rf, f(zero_rf), 'g^', markersize=10, zorder=5,
             label=f'Regula falsi: x = {zero_rf:.6f}')

    plt.ylim(y_min - y_pad, y_max + y_pad)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Wykres funkcji z miejscami zerowymi\nf(x) = {nazwa_funkcji}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

'''
 Dodatkowe wykresy - mogą się przydać może do jakiejs analizy do sprawka czy coś

 def wykres_zbieznosci(przybliżenia_bis, przybliżenia_rf):
     """Porównanie zbieżności obu metod - przybliżenia w kolejnych iteracjach.

     Parametry:
         przybliżenia_bis  - lista przybliżeń z bisekcji
         przybliżenia_rf   - lista przybliżeń z regula falsi
     """
     plt.figure(figsize=(10, 6))

     plt.plot(range(1, len(przybliżenia_bis) + 1), przybliżenia_bis,
              'ro-', label='Bisekcja', markersize=5)
     plt.plot(range(1, len(przybliżenia_rf) + 1), przybliżenia_rf,
              'g^-', label='Regula falsi', markersize=5)

     plt.xlabel('Numer iteracji')
     plt.ylabel('Przybliżenie x')
     plt.title('Zbieżność metod - przybliżenia w kolejnych iteracjach')
     plt.legend()
     plt.grid(True, alpha=0.3)
     plt.tight_layout()
     plt.show()


 def wykres_bledu(przybliżenia_bis, przybliżenia_rf, wartosc_dokladna):
     """Porównanie błędu bezwzględnego obu metod w kolejnych iteracjach - skala logarytmiczna.

     Parametry:
         przybliżenia_bis   - lista przybliżeń z bisekcji
         przybliżenia_rf    - lista przybliżeń z regula falsi
         wartosc_dokladna   - wartość referencyjna x* (dokładne miejsce zerowe)
     """
     bledy_bis = [abs(x - wartosc_dokladna) for x in przybliżenia_bis]
     bledy_rf = [abs(x - wartosc_dokladna) for x in przybliżenia_rf]

     plt.figure(figsize=(10, 6))

     plt.semilogy(range(1, len(bledy_bis) + 1), bledy_bis,
                  'ro-', label='Bisekcja', markersize=5)
     plt.semilogy(range(1, len(bledy_rf) + 1), bledy_rf,
                  'g^-', label='Regula falsi', markersize=5)

     plt.xlabel('Numer iteracji')
     plt.ylabel('Błąd bezwzględny |x_i − x*|')
     plt.title('Porównanie błędu bezwzględnego obu metod (skala logarytmiczna)')
     plt.legend()
     plt.grid(True, alpha=0.3)
     plt.tight_layout()
     plt.show()

 def wykres_porownanie_iteracji(nazwy_eps, iteracje_bis, iteracje_rf):
     """Wykres słupkowy - porównanie liczby iteracji dla różnych dokładności.

     Parametry:
         nazwy_eps      - lista etykiet ε (np. ['1e-2', '1e-4', ...])
         iteracje_bis   - lista liczby iteracji bisekcji dla każdego epsilon
         iteracje_rf    - lista liczby iteracji regula falsi dla każdego epsilon
     """
     plt.figure(figsize=(10, 6))
     x_pos = np.arange(len(nazwy_eps))
     width = 0.35

     plt.bar(x_pos - width/2, iteracje_bis, width, label='Bisekcja', color='red', alpha=0.7)
     plt.bar(x_pos + width/2, iteracje_rf, width, label='Regula falsi', color='green', alpha=0.7)

     plt.xlabel('Dokładność ε')
     plt.ylabel('Liczba iteracji')
     plt.title('Porównanie liczby iteracji dla różnych dokładności')
     plt.xticks(x_pos, nazwy_eps)
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
     plt.tight_layout()
    plt.show()
'''