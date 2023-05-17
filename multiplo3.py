numero_str = input("Digite um número amigo: ")

try:
    numero = int(numero_str)
except ValueError:
    print("Desculpe amigo,",numero_str, "não é um número, não sei oque fazer!!")
else:
    if numero % 3==0:
         print("O número" ,numero, "é múltiplo de 3.")
    else:
         print("O número", numero, "não é múltiplo de 3.")