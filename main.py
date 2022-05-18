import pytest

#teste de unidade

def imprimir_oi(nome):
    print(f'Oi, {nome}')

def somar(numero_a, numero_b):
    return numero_a + numero_b

def subtrair(numero_a, numero_b):
    return numero_a - numero_b

def multiplicar(numero_a, numero_b):
    return numero_a * numero_b

def dividir(numero_a, numero_b):
    return numero_a / numero_b

    #TryExcept é usado para contornar alguma situação em programação. (Não recomendado)
    #try:
        #return numero_a / numero_b
    #except ZeroDivisionError:
        #return 'Não dividiras por Zero'


if __name__ == '__main__':
    imprimir_oi('Grobyc, Twisted metal high slash tiktok stylish sacred thriller tier SS')

    resultado = somar(2, -6)
    print(f' A soma é: {resultado}')


