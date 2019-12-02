import re

number = input("Digite o número do celular: ")

## Para validar se possui 9 digitos
def digit_is_valid(digito):
    digito = re.findall("9", number)

    if (digito):
        return True
    else:
        return False

## Para validar se o numero comeca com 9
def number_is_valid(number):
    number = re.search("^9", number)
    
    if (number):
        return True
    else:
        return False
    
if digit_is_valid(number)  and number_is_valid(number):
  print('Número válido! :)')
else:
  print('Número inválido! :(')  