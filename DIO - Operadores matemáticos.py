operador = input("Qual é o tipo de conta que deseja fazer (+, -, * ou /): ")
x = int(input("Digite um número: "))
y = int(input("Digite outro número: ")) 

# operação matemática   
if operador == '+':
    resposta = x + y
    print("Resposta = ", resposta)

elif operador == '-':
    resposta = x - y
    print("Resposta = ", resposta)

elif operador == '*':
    resposta = x * y
    print("Resposta = ", resposta)

elif operador == '/':
    if y == 0:
        print("Indefinido/infinito")
    else:
        resposta = x / y
        print("Resposta = ", resposta)

else:
    print("ERROR, tente novamente")

# Perguntar ao usuário uma palavra para multiplicar pelo resultado
if 'resposta' in locals():  # Verifica se a variável resposta está definida
    palavra = input("Agora escreva uma palavra que queira multiplicar pelo resultado: ")
    print((palavra + " ") * resposta)
else:
    print("Operação não realizada.")
