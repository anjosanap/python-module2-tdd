nota_1 = int(input("Insira sua nota aqui: "))
nota_2 = int(input("Insira sua nota aqui: "))

def cacula_media(nota_1, nota_2):
    media = (nota_1 + nota_2)/2
    if media >= 6:
        print("Sua média foi ", media, "parabéns você foi aprovado!")

print(cacula_media(nota_1, nota_2))
