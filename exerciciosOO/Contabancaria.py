class ContaBancaria:
    def __init__ (self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo

    
    def __str__(self):
        return f'Titular: {self._titular} - Saldo: {self._saldo} - Ativo: {self._ativo}'
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo    

conta1 = ContaBancaria('Joao', 1000.0)
conta2 = ContaBancaria('Maria', 500.0)

print(conta1)
print(conta2)
print('\n--------\n')
conta1.ativar_conta()
print(conta1)
print(conta1.titular)

conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")