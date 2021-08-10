# 
# Trabalho 1 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

#
# Para rodar: "python3 main.py"
#

# Programa modularizado em:
#    - Gerador de key (gerador_chave.py)
#    - Cifrar (cifrar.py)
#    - Decifrar (decifrar.py)
#    - Atacar! (atacar.py)
#    - Analisador de Frequência (freq.py)
#    - Salvar resultado (salvar.py)

# Imports
# ------------------------------------------------

from gerador_chave import keystream_gerador
from cifrar import cifrador
from decifrar import decifrador
from atacar import ataque
from salvar import salva

# ------------------------------------------------

# pegar do usuário o que é para ser executado!
op = int(input("Que operação realizar?\nResponda com número equivalente.\n\n1- Cifrar\n2- Decifrar\n3- Atacar\n\n"))

# ------------------------------------------------

# Cifrar
if(op == 1):

    # passa a mensagem
    msg = input("Entre com a sua mensagem\n")
    msg = msg.lower()   # trabalhando com letras minusculas, sem caracteres especiais
    msg = msg.replace(',', "").replace('.', "").replace('-', "").replace('"', "").replace(':', "").replace(';', "")

    # passa a chave
    key = input("Entre com a sua chave\n")
    key = key.lower()   # trabalhando com letras minusculas, sem caracteres especiais

    # essa variavel recebe o resultado da operação
    msg_cifrada = cifrador(msg, key)
    print("menssagem cifrada:",msg_cifrada)
    salva(msg_cifrada)

# ------------------------------------------------

# Decifrar
if(op == 2):

    # passa a cifra
    cifra = input("Entre com a sua cifra\n")
    cifra = cifra.lower()   # trabalhando com letras minusculas, sem caracteres especiais
    cifra = cifra.replace(',', "").replace('.', "").replace('-', "").replace('"', "").replace(':', "").replace(';', "")

    # passa a chave
    key = input("Entre com a sua chave\n")
    key = key.lower()   # trabalhando com letras minusculas, sem caracteres especiais

    # essa variavel recebe o resultado da operação
    msg_decifrada = decifrador(cifra, key)
    print("msg final:",msg_decifrada)
    salva(msg_decifrada)

# ------------------------------------------------

# Atacar!
if(op == 3):

    # passa a cifra
    cifra = input("Entre com a sua cifra\n")
    cifra = cifra.lower()   # trabalhando com letras minusculas, sem caracteres especiais
    cifra = cifra.replace(',', "").replace('.', "").replace('-', "").replace('"', "").replace(':', "").replace(';', "")

    resultado = ataque(cifra)


# ------------------------------------------------

if(op != 1 and op != 2 and op != 3):

    print("Tente com operação válida por favor!\nO programa será encerrado agora!")

# ------------------------------------------------

# Referência para testes: https://www.cs.du.edu/~snarayan/crypt/vigenere.html?t1=aa+aa&t2=bb+bb&A0=abcd&D1=4
# "attack at dawn" com key "gondim" retorna "ghgdkw gh qdez"
    
