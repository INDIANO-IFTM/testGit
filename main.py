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
    n = int(input('Digite um numero'))
    print(fatorial(n))
except ValueError:
    print('Erro! Voce deve entrar com um numero')