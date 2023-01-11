import random

nomes = ["Maria", "José", "Antônio", "João", "Francisco", "Ana", "Luiz", "Paulo","Carlos", "Manoel", "Pedro", "Francisca", "Marcos", "Raimundo","Sebastião", "Antônia", "Marcelo", "Jorge", "Márcia", "Geraldo", "Adriana", "Sandra", "Luis", "Fernando", "Fabio", "Roberto", "Márcio", "Edson", "André", "Sérgio"]

sobrenomes = ["da Silva", "dos Santos", "Oliveira", "de Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", "Almeida", "Lopes", "Soares", "Fernandes", "Vieira", "Barbosa", "Rocha", "Dias", "Nascimento", "Andrade", "Moreira", "Nunes", "Marques", "Machado", "Mendes", "Freitas"]


class Pessoa:

    def __init__(self, nome="Nome", cpf="CPF"):
        self.nome = nome
        self.cpf = cpf

    def gerarNomeSobrenome(self):
        nome = nomes[random.randint(0, 25)]
        sobrenome = sobrenomes[random.randint(0, 25)]

        return nome + " " + sobrenome

    def gerarCPF(self):
        multiplicador = 10
        soma = 0
        cpf = ""

        for i in range(9):
            numero = random.randint(0, 9)
            cpf += str(numero)
            soma += numero * multiplicador
            multiplicador -= 1

            primeiroDigitoVerificador = soma % 11
            primeiroDigitoVerificador = 11 - primeiroDigitoVerificador

        if primeiroDigitoVerificador >= 10:
            primeiroDigitoVerificador = 0

        cpf += str(primeiroDigitoVerificador)

        multiplicador = 11
        soma = 0

        for i in range(10):
            numero = int(cpf[i])
            soma += numero * multiplicador
            multiplicador -= 1

        segundoDigitoVerificador = soma % 11
        segundoDigitoVerificador = 11 - segundoDigitoVerificador

        if segundoDigitoVerificador >= 10:
            segundoDigitoVerificador = 0

        cpf += str(segundoDigitoVerificador)

        digitosIguais = 0

        for i in range(len(cpf)):
            if cpf[0] == cpf[i]:
                digitosIguais += 1

        if digitosIguais == 11:
            return self.gerarCPF()

        else:
            cpfMascarado = cpf[0:3]
            cpfMascarado += "."
            cpfMascarado += cpf[3:6]
            cpfMascarado += "."
            cpfMascarado += cpf[6:9]
            cpfMascarado += "-"
            cpfMascarado += cpf[9:len(cpf)]

            for i in range(len(pessoas)):
                if pessoas[i].cpf == cpfMascarado:
                    return self.gerarCPF()
            return cpfMascarado

    def criarPessoa(self, quantidade):
        for i in range(quantidade):
            pessoas.append(Pessoa(self.gerarNomeSobrenome(), self.gerarCPF()))

    def exibirPessoasCriadas(self):
        print("Pessoas Criadas:\n")

        for i in range(len(pessoas)):
            print("Nome: " + pessoas[i].nome + "\nCPF: " + pessoas[i].cpf + "\n")


pessoa = Pessoa()

pessoas = []

quantidadePessoasParaCriar = 10

pessoa.criarPessoa(quantidadePessoasParaCriar)
pessoa.exibirPessoasCriadas()