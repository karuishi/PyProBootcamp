"""
Novamente, solução funcional, contudo, não elegante/eficiente.
    - Uso desnecessário de linhas repetidas
    - Uso ineficiente de loops : e.g. operation = input("+\n-\n*\n/\nEnter a operation: ")
"""

# from art import logo
# from calculator import *
#
# def calculator():
#     print(logo)
#     n1 = float(input("Enter a number: "))
#     operation = input("+\n-\n*\n/\nEnter a operation: ")
#     n2 = float(input("Enter another number: "))
#
#     if operation in operations:
#         result = operations[operation](n1, n2) # cada chave corresponde à sua função (+, -, *, /)
#         print(f"Result: {n1} {operation} {n2} = {result}")
#
#         continue_calculation = True
#         while continue_calculation:
#             should_continue = input(f"Continue calculation with {result}? (y/n): ")
#             if should_continue == "y":
#                 n1 =  result
#                 operation = input("+\n-\n*\n/\nEnter a operation: ")
#                 n2 = float(input("Enter another number: "))
#                 result = operations[operation](n1, n2)
#                 print(f"Result: {n1} {operation} {n2} = {result}")
#             if should_continue == "n":
#                 print("\n" * 20)
#                 calculator() # Chama a função recursivamente para reiniciar o programa com os valores resetados
#
# calculator()

from art import logo
from calculator import *

def calculator():
    print(logo)
    continue_calculation = True
    n1 = float(input("Enter a number: ")) # n1 fora do loop para que não se repita desnecessariamente

    while continue_calculation:
        for op in operations:
            print(op)
        operation = input("Enter a operation: ")
        n2 = float(input("Enter another number: "))
        result = operations[operation](n1, n2)
        print(f"Result: {n1} {operation} {n2} = {result}")

        should_continue = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")

        if should_continue == "y":
            n1 = result
        else:
            continue_calculation = False
            print("\n" * 20)
            calculator()

calculator()