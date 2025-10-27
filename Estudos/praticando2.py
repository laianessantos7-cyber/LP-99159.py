import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Conta_Bancaria:
    titular: str
    saldo: float

    def mostrar_dados(self):
        print("\n=== Dados da Conta ===")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

# ===============================================

print("Solicitando dados da conta bancária...\n")

# Criação da conta
titular = input("Digite o nome do titular da conta: ")
saldo_inicial = float(input("Digite o saldo inicial da conta: "))

conta1 = Conta_Bancaria(titular=titular, saldo=saldo_inicial)

# Lista para armazenar contas (caso queira expandir depois)
lista_contas = [conta1]

# ===============================================
# Menu interativo
while True:
    print("\n========= MENU =========")
    print("1 - Mostrar dados da conta")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("0 - Sair")
    print("========================")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            conta1.mostrar_dados()
        case "2":
            valor = float(input("Digite o valor para depósito: "))
            conta1.depositar(valor)
        case "3":
            valor = float(input("Digite o valor para saque: "))
            conta1.sacar(valor)
        case "0":
            print("\nSaindo... Obrigado por usar o sistema bancário!")
            break
        case _:
            print("Opção inválida. Tente novamente.")
