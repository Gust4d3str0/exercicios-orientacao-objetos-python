class Carro:
    lista_carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.lista_carros.append(self)
        
    def __str__(self):
        return f'Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}'
    
    def listar_todos_carros():
        for carro in Carro.lista_carros:
            print (carro)
    

carro1 = Carro('mustang', 'azul', 2020)
carro2 = Carro('Camaro', 'Amarelo', 2025)

Carro.listar_todos_carros()

