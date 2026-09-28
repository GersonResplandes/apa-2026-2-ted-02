import sys

from central_recursiva import EntradaInvalida, OperacaoInvalida, processar_linha


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
            # Guardamos a resposta mesmo quando a linha tem algum erro.
            resultados.append(resultado)

    sys.stdout.write("\n".join(resultados) + "\n")


if __name__ == "__main__":
    main()
