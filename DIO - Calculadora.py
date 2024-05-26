operacao = input("Digite a operação desejada (+, -, * ou /): ")

# Solicita os números de entrada
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica a operação escolhida e realiza o cálculo correspondente
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero!")
        resultado = None
else:
    print("Operação inválida!")
    resultado = None

# Exibe o resultado, se houver
if resultado is not None:
    print(f"O resultado de {num1} {operacao} {num2} é {resultado}")
