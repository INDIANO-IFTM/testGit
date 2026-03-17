# Iterativo
def fatorial_rec(n: int) -> int:
    '''
        algoritmo recursivo para resolver fatorial
        input:
            n:int - Um valor inteiro qualquer>8
        output:
            result - Um valor inteiro >0
    '''
    #caso base
    if(n <= 1):
        return 1
    else:
        return n * fatorial_rec(n-1)

def fatorial(n: int) -> int:
    '''
        algoritmo iterativ para resolver fatorial
        input:
            n:int - Um valor inteiro qualquer>8
        output:
            result - Um valor inteiro >0
    '''
    res = 1
    for i in range(1, n+1):
        res *= i #= a res = res * i
    return res

try:
    print('===== Fatorial =====')
    n = int(input('Digite um numero '))
    print(f'Resultado Iterativo: {fatorial(n)}')
    print(f'Resultado Recursivo: {fatorial_rec(n)}')
except ValueError:
    print('Erro! Voce deve entrar com um numero')

# Recursivo