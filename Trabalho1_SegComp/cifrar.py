
def cifrador(msg, key, tamanho):

    # falta tratar espaços como casos especiais

    msg_num = [ord(letra) - 97 for letra in msg]

    # testes
    print("msg[0]")
    print(msg_num[0])

    # a = 0, b = 1, c = 2...

    key_num = [ord(letra) - 97 for letra in key]

    msg_cifrada_num = []
    
    for i in range (tamanho):

        msg_cifrada_num.append(((msg_num[i] + key_num[i]) % 26)+97)

    s = "".join([chr(c) for c in msg_cifrada_num])

    # tem que adicionar um 97, assumindo apenas letras minúsculas na tabela ascii
    
    # testes
    print("msgcifrada[0]")
    print(msg_cifrada_num[0])
    print("msg final")
    print(s)

    # a + b = c
    # pois 1 + 2 = 3 (estes numeros sendo a ordem no alfabeto)

    return 1
