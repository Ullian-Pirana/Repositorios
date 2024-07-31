import os

def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def menu():
    print("---MENU--- \n")
    esc_menu = int(input("O que gostaria de fazer? \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair \n --> "))
    
    return esc_menu

def pshipshi():
    os.system("pause")
    os.system("cls")