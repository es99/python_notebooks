from tkinter import Y


def soma(x, y):
    """Função de adição"""
    return x + y

def multiplicacao(x, y):
    """Função de multiplicação"""
    return x * y

def subtracao(x, y):
    """Função de subtração"""
    return x - y

def divisao(x, y):
    """Função de divisão"""
    if y == 0:
        raise ValueError("Não é possível dividir por zero")
    return x / y

