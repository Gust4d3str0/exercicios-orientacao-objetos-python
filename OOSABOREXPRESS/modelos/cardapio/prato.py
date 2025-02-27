from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #Herança
        self._descricao = descricao
    
    def __str__(self):
        return f'Nome: {self.nome} - R${self.preco:.2f}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)