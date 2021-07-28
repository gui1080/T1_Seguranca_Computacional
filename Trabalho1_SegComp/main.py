# 
# Trabalho 1 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#
# Para rodar: "python3 main.py"
#

# Imports
# ------------------------------------------------

from gerador_chave import keystream_gerador

# ------------------------------------------------

# pegar do usuário o que é para ser executado!
op = int(input("Que operação realizar?\nResponda com número equivalente.\n\n1- Cifrar\n2- Decifrar\n3- Atacar\n\n"))

# Cifrar
if(op == 1):

    # passa a mensagem
    msg = input("Entre com a sua mensagem\n")

    # passa a chave
    key = input("Entre com a sua chave\n")

    # define tamanho da mensagem
    size = len(msg)

    # gera keystream
    keystream = keystream_gerador(key, size)
    # keystream é a parte da chave que será usada caso tamanho da chave for maior do que o tamanho da msg
    # caso tamanho da msg seja maior, keystream é a chave repetida até chegar no tamanho correto!

    # algoritmo aq

    print(msg)
    print(msg[0])
    print(size)
    print(keystream)

# Decifrar
if(op == 2):

    # passa a mensagem
    msg = input("Entre com a sua mensagem\n")

    # passa a chave
    key = input("Entre com a sua chave\n")

    # define tamanho da mensagem
    size = len(msg)

    # gera keystream
    keystream = keystream_gerador(key, size)
    # keystream é a parte da chave que será usada caso tamanho da chave for maior do que o tamanho da msg
    # caso tamanho da msg seja maior, keystream é a chave repetida até chegar no tamanho correto!

    # algoritmo aq

    print(msg)
    print(msg[0])
    print(size)
    print(keystream)

if(op == 3):

    print("Espera ae")

if(op != 1 and op != 2 and op != 3):

    print("Tente com operação válida por favor!")
