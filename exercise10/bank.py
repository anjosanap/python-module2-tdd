class Bank:
    def __init__(self, usuario):
        self.usuario = usuario
        self.opcoes = {"1": "saque", "2": "deposito", "3": "emprestimo", "4": "infos", "Qualquer tecla": "sair"}
        self.menu()

    def menu(self):
        print(f"Seja bem-vindo(a), {self.usuario.nome} ao New Bank! :)")
        for chave,valor in self.opcoes.items():
            print("Digite ("+chave+")","para", valor)
        opcao = input(" ")
        self.inicializacao(opcao)
    
    def inicializacao(self, opcao):
        if opcao == "1":
            self.saque()
        elif opcao == "2":
            self.deposito()
        elif opcao == "3":
            self.emprestimo()
        elif opcao == "4":
            self.informacoes()
        else:
            print("Volte sempre!")
    
    def saque(self):
        valor = int(input("Digite o valor para saque: "))
        if valor > 1000 > self.usuario.saldo:
            print("Saldo insuficiente")
        else:
            self.usuario.saldo = self.usuario.saldo - valor 
            print("Saque realizado com sucesso. Saldo atual: ", self.usuario.saldo)
    
    def deposito(self):
        valor = int(input("Digite o valor para depósito: "))
        if valor > 5000:
            print("Não foi permitido realizar o saque!")
        else:
            self.usuario.saldo = self.usuario.saldo + valor
            print("Depósito realizado com sucesso! Saldo atual: ", self.usuario.saldo)
    
    def emprestimo(self):
        if self.usuario.idade < 21:
            print('Idade fora da faixa etária aceita :(')
        else:
            valor = int(input("Digite o valor para empréstimo: "))
            if self.usuario.saldo < 1000:
                print("Infelizmente seu saldo é insuficiente para realizar o empréstimo.")
            else:
                if 2000 <= valor < (15 * self.usuario.saldo):
                    print("Empréstimo realizado com sucesso! Empréstimo:", valor)
                else:
                    print("Causa: valor não compatível!")

    def informacoes(self):
        print("Nome:", self.usuario.nome, "Idade:", self.usuario.idade, "anos. Seu saldo é de", self.usuario.saldo, "reais.")


        

