lista = [145, , 32, 23]

soma = 0

try:
    for valor in lista:
        soma += valor
    media = soma / len(lista)
    print(f'Media: {media:.2f}')
except ZeroDivisionError:
    print("Não é possível calcular a média de uma lista vazia.")
except Exception as e:
    print(f'ERRO: {e}')