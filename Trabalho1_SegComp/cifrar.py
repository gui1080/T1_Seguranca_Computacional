
import time

def cifrador(msg, key, tamanho):

    msg_num = [ord(letra) - 97 for letra in msg]

    # testes
    print("msg[0]")
    print(msg_num[0])

    # a = 0, b = 1, c = 2...

    key_num = [ord(letra) - 97 for letra in key]

    msg_cifrada_num = []
    
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

    fim = "".join([chr(c) for c in msg_cifrada_num])
    # tem que adicionar um 97, assumindo apenas letras minúsculas na tabela ascii
    
    # testes
    print("msgcifrada[0]")
    print(msg_cifrada_num[0])
    print("msg final")
    print(fim)

    # a + b = c
    # pois 1 + 2 = 3 (estes numeros sendo a ordem no alfabeto)
    # teste feito : https://www.cs.du.edu/~snarayan/crypt/vigenere.html?t1=aa+aa&t2=bb+bb&A0=abcd&D1=4
    # "aaaaaa aa" cifrado com key "abcd" tem que dar "abcdab cd"

    salvar = input("Deseja salvar o resultado em um arquivo de texto?[Y/N]?\n\n")

    if(salvar == 'y' or salvar == 'Y'):

        nome_arquivo = "resultado_cifrado" + str(time.time())
    
        arquivo = open(nome_arquivo, 'w+')

        arquivo.writelines("Resultado cifrado: " + fim)

        arquivo.close()

        print("Arquivo salvo!")

    return fim
