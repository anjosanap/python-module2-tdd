import re

number = input("Digite o número do celular: ")

## Para validar se possui 9 digitos
def digito(digito):
    digito = re.findall("9", number)

    if (digito):
        print("Número válido! :)")
    else:
        print("Número inválido! :(")

## Para validar se o numero comeca com 9
def number(number):
    x = re.search("^9", number)
    
    if (x):
        print("Número válido! :)")
    else:
        print("Número inválido! :(")
    
resultado = number(number) + digito(digito)

print(resultado)