"""Modulo con funzioni per l'esercizio 0."""


def fun_1(n: int) -> None:
    """Stampa i numeri pari da 0 a n."""
    for i in range(n + 1):
        if i % 2 == 0:
            print(i, end=" ")


def fun_2(n: int) -> int:
    """Restituisce il doppio di un numero dispari e la metà di un numero pari."""
    if n % 2 != 0:
        return n * 2
    else:
        return n // 2


def fun_3(A: list[int]) -> int:
    """Restituisce l'elemento più piccolo di A."""
    m = A[0]
    for i in range(len(A)):
        if A[i] < m:
            m = A[i]
    return m


def fun_4(A: list[int]) -> int:
    """Restituisce la somma degli elementi di A divisibili per tre o per cinque."""
    s = 0
    for i in range(len(A)):
        if A[i] % 3 == 0 or A[i] % 5 == 0:
            s += A[i]
    return s


def fun_5(A: list[int]) -> float:
    """Restituisce la varianza degli elementi di A."""
    m = 0
    for i in range(len(A)):
        m += A[i]
    m /= len(A)

    v = 0
    for i in range(len(A)):
        v += (A[i] - m) ** 2
    v /= len(A)
    return v


def fattoriale(n: int) -> int:
    """Restituisce il fattoriale di n."""
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def fun_6(n: int) -> int:
    """Restituisce l'n-esimo termine della serie dei reciprocali dei fattoriali."""
    s = 0
    for i in range(n + 1):
        s += 1 / fattoriale(i)
    return s
