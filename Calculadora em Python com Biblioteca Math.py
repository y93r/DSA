import math

print("\n******************* Calculadora em Python com Biblioteca Math *******************")
print('''1-Somar (+)
2-Subtrair (-)
3-Multiplicar (*)
4-Dividir (/)
5-Potência (^)
6-Raiz Quadrada (√)
''')

def escolher_operacao():
    try:
        operacao = int(input('Digite qual das 6 operações deseja fazer: '))

        if operacao in [1, 2, 3, 4]:
            num1 = float(input('Digite um número: '))
            num2 = float(input('Digite outro número: '))

            if operacao == 1:
                resultado = num1 + num2
                print(f'{num1} + {num2} = {resultado}')
            elif operacao == 2:
                resultado = num1 - num2
                print(f'{num1} - {num2} = {resultado}')
            elif operacao == 3:
                resultado = num1 * num2
                print(f'{num1} * {num2} = {resultado}')
            elif operacao == 4:
                if num2 == 0:
                    print('Não é possível dividir por zero.')
                else:
                    resultado = num1 / num2
                    print(f'{num1} / {num2} = {resultado}')
        elif operacao == 5:
            num1 = float(input('Digite a base: '))
            num2 = float(input('Digite o expoente: '))
            resultado = math.pow(num1, num2)
            print(f'{num1} ^ {num2} = {resultado}')
        elif operacao == 6:
            num = float(input('Digite o número: '))
            resultado = math.sqrt(num)
            print(f'A raiz quadrada de {num} é {resultado}')
        else:
            print('Digite uma operação válida (1 a 6)!')
    except ValueError:
        print('Digite um número válido!')

escolher_operacao()
