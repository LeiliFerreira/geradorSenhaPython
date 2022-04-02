from random import random, choice
from time import sleep
import string

print("\033[30;46m------------------GERADOR DE SENHAS------------------\033[m")

print("Menu opções: ")
print("\033[30m[1]\033[m - Letras maiúsculas")
print("\033[30m[2]\033[m - Letras minúsculas")
print("\033[30m[3]\033[m - Letras maísculas com números")
print("\033[30m[4]\033[m - Letras minúsculas com números")
print("\033[30m[5]\033[m - Letras maiúsculas e minúsculas com números")
print("\033[30m[6]\033[m - Letras maiúsculas e minúsculas com números e caracteres especiais")
print("-----------------------------------------------------------------------")

while True:
    try:
        padrao = int(input("Qual o padrão da senha?"))
        print("------------------------")
        break
    except:
        print("\033[1;31mOpção inválida!\033[m")
        continue

if padrao == 1:
   valores = string.ascii_uppercase

elif padrao == 2:
    valores = string.ascii_lowercase

elif padrao == 3:
    valores = string.ascii_uppercase
    valores += string.digits

elif padrao == 4:
    valores = string.ascii_lowercase
    valores += string.digits

elif padrao == 5:
    valores = string.ascii_letters
    valores += string.digits

elif padrao == 6:
    valores = string.ascii_letters
    valores += string.digits
    valores += string.punctuation
else:
    print("\033[1;31mOpção inválida!\033[m")

while True:
    try:
        tamanho_senha = int(input("Digite a quantidade de caracteres que deseja: "))
        break
    except:
        print("\033[1;31mInsira apenas números.\033[m")
        continue

resultado = ""

for a in range(tamanho_senha):
    resultado += choice(valores)

sleep(0.6)
print("\033[1;33mGerando senha...\033[m")
sleep(2)

print("\033[30mResultado:\033[m {}".format(resultado))














