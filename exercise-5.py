nome_funcionario = input("Digite o nome do funcionário: ")
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora: "))

def calculo_salario(nome_funcionario, horas_trabalhadas, valor_hora):
    salario = horas_trabalhadas * valor_hora
    print("O funcionário", nome_funcionario, "trabalhou", horas_trabalhadas, "horas", "e receberá", salario, "reais")
    return salario

print (calculo_salario(nome_funcionario, horas_trabalhadas, valor_hora))
