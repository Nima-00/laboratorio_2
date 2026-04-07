"""Modulo con funzioni per l'esercizio 1."""

import matplotlib.pyplot as plt


def fun_1(c: list[float, float], x: float) -> float:
    """Valuta la retta $y = mx + q$ in un punto $x$."""
    m = c[0]
    q = c[1]
    return m * x + q


def fun_2(I: list, k: int) -> list:
    """Restituisce una lista con i primi $k$ elementi di $I$."""
    punti = []
    passo = (I[1] - I[0]) / k
    for i in range(k + 1):
        punti.append(I[0] + i * passo)
    return punti


def fun_3(c: list, x_list: list) -> list:
    """Valuta la retta $y = mx + q$ in una lista di punti."""
    y_list = []
    for x in x_list:
        y = fun_1(c, x)
        y_list.append(y)
    return y_list


def fun_4(c: list, I: list, k: int, fig_size: tuple = (4, 2)) -> None:
    """Plotta la retta y = mx + q per i valori di x in x_list, dove c = [m, q]."""
    x_list = fun_2(I, k)
    y_list = fun_3(c, x_list)
    plt.figure(figsize=fig_size)
    plt.plot(x_list, y_list, marker="o", color="red")  # flag linestyle="None"
    plt.title(f"Grafico della retta y = {c[0]}x + {c[1]}, con {k} punti")
    plt.axhline(0, color="black", ls="--")
    plt.axvline(0, color="black", ls="--")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()
