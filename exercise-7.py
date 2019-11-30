## Cadastro de usuario no sistema
class Funcionario:
    def __init__(self, nome, email, rg, idade, salario):
        self.nome = nome
        self.email = email
        self.rg = rg
        self.idade = idade
        self.salario = 2000

    def __str__(self):
        return f"Olá {self.nome}, você foi cadastrado com sucesso em nosso sistema! :)"

## Aumentar salario
    def aumentar_salario(self, valor):
        return self.salario + valor

## Dados funcionario
cadastro_funcionario = Funcionario (
    nome = "Ana",
    email = "aanjos@google.com",
    rg = "66.666.666-6",
    idade = 18,
    salario = 2000
)

## Valor de acréscimo de salário
valor = float(input("Digite o valor: "))

## Print de cadastro do usuário com salário atual
print(cadastro_funcionario)
print("O seu salário é de", cadastro_funcionario.salario, "reais")

## Print aumento salarial
print("O seu salário com o aumento fica", cadastro_funcionario.aumentar_salario(valor), "reais")
