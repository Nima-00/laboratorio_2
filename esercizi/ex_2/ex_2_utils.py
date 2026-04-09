"""Modulo con funzioni per l'esercizio 2."""

import math


def fun_1(n: int):
    """Stampa i multipli di tre compresi tra 0 e n, estremi inclusi."""
    for i in range(n + 1):
        if i % 3 == 0:
            print(i, end=" ")


def fun_2(l: list) -> list:
    """Prende una lista e ritorna una nuova lista con glie elementi in ordine invertito."""
    new_l = []
    n = len(l)
    for i in range(n):
        new_l.append(l[n - 1 - i])
    return new_l


def fun_3(A: list, num: int) -> int:
    """Resituisce il numero di occorrenze di num in A."""
    k = 0
    for i in range(len(A)):
        if A[i] == num:
            k += 1
    return k


def fun_4(A: list) -> int:
    """Ritorna il massimo di una lista di interi."""
    m = A[0]
    for i in range(len(A)):
        if m < A[i]:
            m = A[i]
    return m


def fun_5(A: list) -> list:
    """Restituisce l'array normalizzato seconfo la funzione softmax."""
    s = 0
    for i in range(len(A)):
        s += math.e ** A[i]
    B = []
    for i in range(len(A)):
        B.append(math.e ** A[i] / s)
    return B


def fun_6(n: int) -> float:
    """Calcola la somma dei reciproci dei quadrati dei primi n interi"""
    s = 0
    for i in range(1, n + 1):
        s += 1 / i**2
    return s


def fun_7(n: int) -> float:
    return (6 * fun_6(n)) ** 0.5
