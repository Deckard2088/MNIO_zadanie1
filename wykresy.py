#Dawid Wachecki 2548901
#Kacper Skoczylas 254864
#Zadanie 1: metoda bisekcji, reguła falsi, wariant A
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def wykres_funkcji_z_miejscami_zerowymi(f, a, b, zero_bis, zero_rf, nazwa_funkcji, zakres=None):
    """Rysuje wykres funkcji z zaznaczonymi miejscami zerowymi obu metod.
    Automatycznie dopasowanie zakresy osi do wartości funkcji.

    Parametry:
        f              - funkcja f(x)
        a, b           - krańce przedziału
        zero_bis       - miejsce zerowe znalezione bisekcją
        zero_rf        - miejsce zerowe znalezione falsi
        nazwa_funkcji  - nazwa/opis funkcji - tytul i legenda
    """
    if zakres is None:
        margines = (b - a) * 0.1
        x = np.linspace(a - margines, b + margines, 500)
    else:
        x = np.linspace(zakres[0], zakres[1], 500)
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
    if zakres is not None:
        if zakres[0] <= 0 <= zakres[1]:
            plt.axvline(x=0, color='k', linewidth=0.5)
            plt.xticks(np.arange(np.floor(x.min()), np.ceil(x.max()) + 1, 1))
    else:
        if a <= 0 <= b:
            plt.axvline(x=0, color='k', linewidth=0.5)

        plt.axvline(x=a, color='orange', linestyle='--', linewidth=1.5, label=f'Przedział [a={a}, b={b}]')
        plt.axvline(x=b, color='orange', linestyle='--', linewidth=1.5)

        plt.plot(zero_bis, f(zero_bis), 'ro', markersize=10, zorder=5,
             label=f'Bisekcja: x = {zero_bis:.6f}')
        plt.plot(zero_rf, f(zero_rf), 'g^', markersize=10, zorder=5,
             label=f'Regula falsi: x = {zero_rf:.6f}')

    if zakres is not None:
        plt.ylim(zakres[0], zakres[1])
    else:
        plt.ylim(y_min - y_pad, y_max + y_pad)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Wykres funkcji z miejscami zerowymi\nf(x) = {nazwa_funkcji}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    nazwa_pliku = f'wykres_{nazwa_funkcji}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
    plt.savefig(nazwa_pliku, dpi=150, bbox_inches='tight')
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
     nazwa_pliku = f'wykres_porownanie_iteracji_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
     plt.savefig(nazwa_pliku, dpi=150, bbox_inches='tight')
     plt.show()
