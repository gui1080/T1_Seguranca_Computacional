# 
# Trabalho 1 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------
from gerador_chave import keystream_gerador
# ------------------------------------------------

def decifrador(cifra, chave):

    # define tamanho da mensagem
    tamanho=len(cifra)
    # gera keystream
    key = keystream_gerador(chave, tamanho)

    # para cada letra na string, transforma em numero (posição relativa no alfabeto)
    cifra_num = [ord(letra) - 97 for letra in cifra]

    # testes
    # print("cifra[0]:",cifra_num[0])

    # a = 0, b = 1, c = 2...

    # para cada letra na string, transforma em numero (posição relativa no alfabeto)
    key_num = [ord(letra) - 97 for letra in key]
    
    # testes
    # print("key_num[0]:",key_num[0])

    # lista vazia que receberá mensagem decifrada
    msg_decifrada_num = []
    
    # indexando a key com "j" e não "i" pois pulamos posições "i" que são espaços na cifra
    # mas não se pula esse espaço na key
    j = 0

    for i in range (tamanho):

        # detecta-se espaços!
        # -65 é o que sai quando se contabiliza os espaços
        if(cifra_num[i] == (-65)):

            # 32 é o espaço em ASCII 
            msg_decifrada_num.append(32)

        # se não é espaço, realiza-se a soma, módulo por 26
        # adiciona-se 97 na base para converter pro valor em ASCII
        else:

            msg_decifrada_num.append(((cifra_num[i] - key_num[j]) % 26)+97)
            # atualiza-se a posição da keystream
            j=j+1
    # tem que adicionar um 97, assumindo apenas letras minúsculas na tabela ascii

    # a string no final é tudo junto pelo método "join", sem espaços, transformado em caractere
    fim = "".join([chr(c) for c in msg_decifrada_num])

    return fim
