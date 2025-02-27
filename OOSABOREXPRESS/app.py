from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
bebida_vinho = Bebida('vinho', 15.00, 'taca')
bebida_suco.aplicar_desconto
prato_paozinho = Prato('Paozinho', 2.00, 'Pao') 
prato_paozinho.aplicar_desconto()


restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
    