class Cliente:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente: Cliente, saldo: float) -> None:
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        return self.saldo

    def sacar(self, valor: float) -> float:  
        if valor <= self.saldo:
            self.saldo -= valor
            return self.saldo
        else:
            raise ValueError("Saldo insuficiente.")  

    def consultar_saldo(self) -> float:
        return self.saldo

class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, saldo: float, limite: float ) -> None:
        super().__init__(cliente, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:  
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return self.saldo
        else:
            raise ValueError("Saldo e limite insuficientes.") 

class ContaPoupanca(Conta):
    def __init__(self, cliente: Cliente, saldo: float, juros: float) -> None:  
        super().__init__(cliente, saldo)
        self.juros = juros

    def aplicar_juros(self) -> float:
        while True:
            try:
                self.juros = float(input("Digite o valor do juros em porcentagem (0.01 à 100): "))
                if 0.01 <= self.juros <= 100:
                    break
                else:
                    print("Valor de juros inválido. Digite um valor entre 0.01 e 100.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
        self.juros /= 100
        self.saldo += self.saldo * self.juros
        return self.saldo
