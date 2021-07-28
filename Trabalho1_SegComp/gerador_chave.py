# 
# Trabalho 1 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

def keystream_gerador(key, tamanho):

    # divide o tamanho que queremos com o tamanho atual, arredonda pra +1
    repeticoes = tamanho // len(key) + 1

    # repete a chave "x" vezes
    key_repetida = key * repeticoes

    # corta no tamanho desejado
    key_repetida_corretamente = key_repetida[:tamanho]

    # retorna o que sobrou
    return key_repetida_corretamente