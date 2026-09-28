import re
import sys


class OperacaoInvalida(Exception):
    mensagem_saida = "ERRO: OperacaoInvalida"


class EntradaInvalida(Exception):
    mensagem_saida = "ERRO: EntradaInvalida"


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def soma_digitos(n):
    if n < 10:
        return n
    return n % 10 + soma_digitos(n // 10)


def inteiro(texto):
    if re.fullmatch(r"[+-]?[0-9]+", texto) is None:
        raise EntradaInvalida
    try:
        return int(texto)
    except ValueError as erro:
        raise EntradaInvalida from erro


def processar_linha(linha):
    partes = linha.split()
    if not partes:
        raise EntradaInvalida

    operacao = partes[0]
    if operacao not in ("M", "S"):
        raise OperacaoInvalida

    if operacao == "M":
        if len(partes) != 3:
            raise EntradaInvalida
        a, b = inteiro(partes[1]), inteiro(partes[2])
        if a <= 0 or b <= 0:
            raise EntradaInvalida
        return f"MDC = {mdc(a, b)}"

    if len(partes) != 2:
        raise EntradaInvalida
    n = inteiro(partes[1])
    if n < 0:
        raise EntradaInvalida
    return f"SOMA = {soma_digitos(n)}"


def main():
    quantidade = int(sys.stdin.readline())
    resultados = []

    for _ in range(quantidade):
        linha = sys.stdin.readline()
        resultado = "ERRO: EntradaInvalida"
        try:
            resultado = processar_linha(linha)
        except (EntradaInvalida, OperacaoInvalida) as erro:
            resultado = erro.mensagem_saida
        finally:
            resultados.append(resultado)

    sys.stdout.write("\n".join(resultados) + "\n")


if __name__ == "__main__":
    main()
