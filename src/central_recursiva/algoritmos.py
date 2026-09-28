def mdc(a, b):
    """Calcula o MDC pelo algoritmo de Euclides."""
    if b == 0:
        return a
    return mdc(b, a % b)


def soma_digitos(n):
    """Soma o último dígito com os dígitos restantes."""
    if n < 10:
        return n
    return n % 10 + soma_digitos(n // 10)
