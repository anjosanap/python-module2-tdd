min = int(input("Insira o primeiro número: "))
max = int(input("Insira o segundo número: "))

def number(min, max):
    for number in range(min, max, 2):
        print(number)

print(number(min, max))
