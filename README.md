# Central Recursiva

## Integrantes

- Gérson Resplandes de Sá Sousa
- Erdeson Monteiro Candeias

## Disciplina

Algoritmos e Programação Avançada — 2026.2

Este repositório reúne uma atividade do curso de Análise e Desenvolvimento de Sistemas (ADS).

## Sobre o projeto

Desenvolvemos a Central Recursiva em Python para resolver o problema **CentralRecursivaRobusta**. O programa lê a quantidade de operações na primeira linha e depois processa uma operação por linha:

- `M A B`: calcula o máximo divisor comum de `A` e `B`.
- `S N`: calcula a soma dos dígitos de `N`.

Cada operação gera uma linha de saída. Quando a operação ou os valores são inválidos, o programa mostra a mensagem de erro definida no enunciado.

O problema está disponível no beecrowd sob o número **7923**.

## Como executar

É necessário ter Python 3 instalado. Na pasta do projeto, podemos usar o arquivo de exemplo:

No Prompt de Comando, execulte `python src/main.py < entrada_exemplo.txt`. Em Linux ou macOS, talvez seja necessário trocar `python` por `python3`. Para testar outra entrada, basta criar um arquivo com a quantidade `Q` na primeira linha e as operações nas linhas seguintes.

## Estrutura do repositório

```text
central-recursiva/
├── README.md
├── entrada_exemplo.txt
├── src/
│   ├── main.py
│   ├── submissao_beecrowd.py
│   └── central_recursiva/
│       ├── __init__.py
│       ├── algoritmos.py
│       ├── excecoes.py
│       └── processador.py
└── tests/
    └── test_cli.py
```

- `src/central_recursiva/__init__.py`: disponibiliza as funções e exceções do pacote para importação.
- `src/central_recursiva/algoritmos.py`: contém as funções recursivas `mdc` e `soma_digitos`.
- `src/central_recursiva/excecoes.py`: define as exceções e as mensagens de erro usadas na saída.
- `src/central_recursiva/processador.py`: verifica a entrada e chama a função correspondente à operação.
- `src/main.py`: lê as linhas da entrada, trata os erros e imprime as respostas.
- `src/submissao_beecrowd.py`: reúne o código em um único arquivo para a submissão no beecrowd.
- `tests/test_cli.py`: confere as saídas das duas versões com entradas válidas e inválidas.

## Algoritmos recursivos

No **MDC**, usamos o algoritmo de Euclides. A função chama `mdc(b, a % b)` até `b` ser zero. Quando isso acontece, `a` é o resultado. Por exemplo, `mdc(48, 18)` passa por `mdc(18, 12)`, `mdc(12, 6)` e `mdc(6, 0)`, retornando `6`.

Na **soma dos dígitos**, `n % 10` pega o último dígito e `n // 10` remove esse dígito. Somamos o último dígito ao resultado da chamada recursiva. Quando sobra apenas um dígito (`n < 10`), a função retorna o próprio número. Assim, `soma_digitos(2026)` retorna `10`.

## Validação e tratamento de erros

Criamos duas exceções que herdam de `Exception`:

- `OperacaoInvalida`: para qualquer operação diferente de `M` e `S`.
- `EntradaInvalida`: para linha vazia, quantidade errada de argumentos, valores que não são inteiros ou números fora dos limites.

Em `M`, aceitamos dois inteiros entre `1` e `10^9`. Em `S`, aceitamos um inteiro entre `0` e `10^18`. No `src/main.py`, usamos `try` para processar cada linha, `except` para transformar as exceções nas mensagens exigidas e `finally` para guardar uma resposta para a operação.

## Testes

Testamos os exemplos do enunciado, valores nos limites e entradas inválidas. Para executar os testes:

```powershell
python -m unittest discover -s tests -v
```