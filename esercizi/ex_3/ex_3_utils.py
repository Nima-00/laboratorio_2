"""Modulo con funzioni per l'esercizio 3."""


def fun_1(a: str):
    """Prende in input una stringa e la stampa in vari modi"""
    print(a.upper())
    print(a.lower())
    for c in a:
        print(c, end=" ")


def conta_parole(a: str) -> int:
    """Ritorna il numero di parole che compongono una stringa"""
    return len(a.split())


def fun_3(a: str) -> float:
    """Ritorna la lunghezza media delle parole di una frase."""
    parole = a.split()
    m = 0
    for p in parole:
        m += len(p)
    return m / len(parole)


def dec_to_bin(n: int) -> int:
    """Converte numero da decimale a binario"""
    b = 0
    i = 0
    while n > 0:
        b += (n % 2) * 10**i
        n = n // 2
        i += 1
    return b


def bin_to_dec(n: int) -> int:
    """Converte numero da binario a decimale"""
    d = 0
    i = 0
    while n > 0:
        d += (n % 10) * 2**i
        n = n // 10
        i += 1
    return d


def conv_to_ascii(a: str):
    """Stampa i caratteri di una stringa in formato  ascii"""
    for c in a:
        print(c, "->", str(dec_to_bin(ord(c))).zfill(8))


def codifica_ascii(a: str) -> str:
    """Codifica una stringa in codice ASCII"""
    s = ""
    for c in a:
        s += str(dec_to_bin(ord(c))).zfill(8)
    return s


def decodifica_ascii(a: str) -> str:
    """Decodifica testo in ASCII"""
    if len(a) % 8 != 0:
        raise ValueError("Lunghezza non valida")
    s = ""
    for i in range(len(a) // 8):
        s += chr(bin_to_dec(int(a[i * 8 : (i + 1) * 8])))
    return s
