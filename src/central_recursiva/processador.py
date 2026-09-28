import re

from .algoritmos import mdc, soma_digitos
from .excecoes import EntradaInvalida, OperacaoInvalida


def _inteiro(texto):
    if re.fullmatch(r"[+-]?[0-9]+", texto) is None:
        raise EntradaInvalida("É necessário informar um inteiro decimal.")
    try:
        return int(texto)
    except ValueError as erro:
        raise EntradaInvalida("É necessário informar um inteiro.") from erro


def processar_linha(linha):
    partes = linha.split()
    if not partes:
        raise EntradaInvalida("A linha está vazia.")

    operacao = partes[0]
    if operacao not in ("M", "S"):
        raise OperacaoInvalida(f"Operação desconhecida: {operacao}.")

    if operacao == "M":
        if len(partes) != 3:
            raise EntradaInvalida("M exige dois argumentos.")
        a, b = _inteiro(partes[1]), _inteiro(partes[2])
        if a <= 0 or b <= 0:
            raise EntradaInvalida("Os argumentos de M devem ser positivos.")
        return f"MDC = {mdc(a, b)}"

    if len(partes) != 2:
        raise EntradaInvalida("S exige um argumento.")
    n = _inteiro(partes[1])
    if n < 0:
        raise EntradaInvalida("O argumento de S não pode ser negativo.")
    return f"SOMA = {soma_digitos(n)}"
