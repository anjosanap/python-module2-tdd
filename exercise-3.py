import math

raio = int(input("Escreva o valor do raio: "))

def calculate_area(raio):
    area  = (math.pi * (raio * raio))
    return area

def circle(raio):
    circulo = (2 * math.pi * raio)
    return circulo

comprimento_circulo = circle(raio)
area_circulo = calculate_area(raio)


print("O valor da area é ", comprimento_circulo)
print("O comprimento do círculo é ", area_circulo)
