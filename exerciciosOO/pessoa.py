class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao
    
    def __str__(self):
        return f'NOME: {self._nome} IDADE: {self._idade} PROFISSAO: {self._profissao}'
    
    @property
    def aniversario(self):
        self._idade += 1
    
    def saudacao(self):
        if self._profissao:
            return f'Parabens! por ser {self._profissao}'
        else: 
            return f'Desempregado!'
    
pessoa1 = Pessoa('gustavo', 20, 'Engenheiro')
print(pessoa1)
pessoa1.aniversario
print(pessoa1)
print(pessoa1.saudacao())

    
pessoa2 = Pessoa('carlinho', 20, '')
print(pessoa2)
print(pessoa2.saudacao())