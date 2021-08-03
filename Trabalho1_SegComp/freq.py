# 
# Trabalho 1 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------


# ------------------------------------------------

def pega_frequencia(cifra, tamanho_chave, intervalo):
    
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
    
    freq_cifra = []
    
    freq_alfabeto = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074] 
    
    for i in range(26):
        freq_cifra.append(0)
    
    print(freq_cifra)
    
    # posição [0] é a quantidade de vezes que o "a" repetiu
    # posição [1] é a quantidade de vezes que o "b" repetiu
    # ...
    # posição [25] é a quantidade de vezes que o "z" repetiu
    
    j = 0
    quantidade_de_resets = 0
    
    for i in range(len(cifra)):
        
        if(cifra[i] != " "):
        
            if(j == tamanho_chave):
                # reset
                j = 0
                quantidade_de_resets = quantidade_de_resets + 1
                
            if(j == intervalo):
                # salva a ocorrencia da letra
                letra = (ord(cifra[i]) - 97)
                #print("letra!")
                #print(letra)
                freq_cifra[letra] = freq_cifra[letra] + 1
                letra = 0
                
            j = j + 1
    
    print("Frequência encontrada: ")
    for i in range(26):
        porcentagem = round((freq_cifra[i]/quantidade_de_resets)*100, 2)
        print("Frequencia da Letra '" + alfabeto[i] + "' na cifra: " + str(porcentagem) + "%, Frequência original: " + str(freq_alfabeto[i]) + "%")
        
    
    return 0