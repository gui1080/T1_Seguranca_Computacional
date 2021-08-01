# 
# Trabalho 1 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------

import time     # usado para gerar o nome do arquivo de saída, valor único por execução

# ------------------------------------------------

def cifrador(msg, key, tamanho):

    # para cada letra na string, transforma em numero (posição relativa no alfabeto)
    msg_num = [ord(letra) - 97 for letra in msg]

    # testes
    # print("msg[0]:",msg_num[0])

    # a = 0, b = 1, c = 2...

    # para cada letra na string, transforma em numero (posição relativa no alfabeto)
    key_num = [ord(letra) - 97 for letra in key]

    # lista vazia que receberá mensagem cifrada
    msg_cifrada_num = []
    
    # indexando a key com "j" e não "i" pois pulamos posições "i" que são espaços na mensagem
    # mas não se pula esse espaço na key
    j = 0

    for i in range (tamanho):

        # detecta-se espaços!
        # -65 é o que sai quando se contabiliza os espaços
        if(msg_num[i] == (-65)):

            # 32 é o espaço em ASCII 
            msg_cifrada_num.append(32)

        # se não é espaço, realiza-se a soma, módulo por 26
        # adiciona-se 97 na base para converter pro valor em ASCII
        else:

            msg_cifrada_num.append(((msg_num[i] + key_num[j]) % 26)+97)
            # atualiza-se a posição da keystream
            j=j+1
        # tem que adicionar um 97, assumindo apenas letras minúsculas na tabela ascii

    # a string no final é tudo junto pelo método "join", sem espaços, transformado em caractere
    fim = "".join([chr(c) for c in msg_cifrada_num])
    
    
    return fim


    # a + b = c
    # pois 1 + 2 = 3 (estes numeros sendo a ordem no alfabeto)
    # teste feito : https://www.cs.du.edu/~snarayan/crypt/vigenere.html?t1=aa+aa&t2=bb+bb&A0=abcd&D1=4
    # "aaaaaa aa" cifrado com key "abcd" tem que dar "abcdab cd"

    # ------------------------------------------------
