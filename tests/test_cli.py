from pathlib import Path
import subprocess
import sys
import unittest


RAIZ = Path(__file__).resolve().parents[1]


class CentralRecursivaCLITest(unittest.TestCase):
    def conferir_ambas_versoes(self, entrada, esperado):
        for arquivo in ("main.py", "submissao_beecrowd.py"):
            with self.subTest(arquivo=arquivo):
                processo = subprocess.run(
                    [sys.executable, "-B", str(RAIZ / "src" / arquivo)],
                    input=entrada,
                    text=True,
                    capture_output=True,
                    cwd=RAIZ,
                    check=True,
                )
                self.assertEqual(processo.stdout, esperado)
                self.assertEqual(processo.stderr, "")

    def test_exemplo_do_enunciado(self):
        self.conferir_ambas_versoes(
            "7\nS 12345\nM 72 30\nM 17 19\nS 0\nM 0 25\nS -50\nX 10 20\n",
            "SOMA = 15\nMDC = 6\nMDC = 1\nSOMA = 0\n"
            "ERRO: EntradaInvalida\nERRO: EntradaInvalida\n"
            "ERRO: OperacaoInvalida\n",
        )

    def test_limites_e_entradas_invalidas(self):
        self.conferir_ambas_versoes(
            "10\nM 1000000000 1\nS 1000000000000000000\n"
            "M 1\nS 1 2\nM 1_0 3\nS -1\nM 1 0\n?\n\n"
            "S 999999999999999999\n",
            "MDC = 1\nSOMA = 1\n"
            + "ERRO: EntradaInvalida\n" * 5
            + "ERRO: OperacaoInvalida\n"
            + "ERRO: EntradaInvalida\n"
            + "SOMA = 162\n",
        )

    def test_valores_acima_dos_limites_continuam_validos(self):
        self.conferir_ambas_versoes(
            "2\nM 1000000001 1000000000\nS 1000000000000000001\n",
            "MDC = 1\nSOMA = 2\n",
        )


if __name__ == "__main__":
    unittest.main()
