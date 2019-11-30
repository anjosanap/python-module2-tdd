class Carro:
    def __init__(self, proprietario, modelo, cor, placa, preco, marca):
        self.proprietario = proprietario
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.preco = preco
        self.marca = marca

    def __str__(self):
        return f"Olá {self.proprietario}, seu carro é o {self.marca}-{self.modelo}, cor {self.cor} e placa {self.placa}"
        
meu_carro = Carro(
    proprietario = "Ana",
    modelo = "Kicks",
    cor = "preto",
    placa = "HEL-6666",
    preco = 40000,
    marca = "Nissan"
)

print(meu_carro)
