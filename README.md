## Implementações de Fatorial em Python

O objetivo deste repositório é mostrar duas diferentes versões de algoritmos para resolução de fatorial.

## Fatorial Iterativo

Fatorial iterativo consiste da implementação de versão iterativa do algoritmo fatorial.
Nesta abordagem utiliza-se *loops* condicionais e armazenamento explícito em variável.

* Exemplo:
```python
def fatorial(n: int) -> int:
    res = 1
    for i in range(1, n+1):
        res *= i #= a res = res * i
    return res
  ```
## Fatorial Recursivo

Fatorial Recursivo consiste na implementação de versão recursiva do algoritmo fatorial.
Nesta abordagem utiliza-se recurso de chama da propria função para quebrar em problemas menores até o caso base (parada).

* Exemplo
```python
def fatorial_rec(n: int) -> int:
    if(n <= 1):
        return 1
    else:
        return n * fatorial_rec(n-1)
``
