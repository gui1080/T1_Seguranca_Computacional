# 
# Trabalho 1 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------
from decifrar import decifrador 
from gerador_chave import keystream_gerador
from freq import pega_frequencia_ing
from freq import pega_frequencia_ptbr
# ------------------------------------------------

def ataque(cifra):
    
    # seleciona lingua
    op = int(input("Deseja usar frequências das letras em Inglês(1) ou Português(2)?\n"))
    
    # pegar frequências de grupos de 3 letras
    # ------------------------------------------------

    itens = []
    # itens = [letras analizadas1, vezes que repetiu1, distancia1, letras analizadas2, vezes que repetiu2, distancia2...]
    
    tamanho = len(cifra)
    letras = "" # grupo de letras inicia vazio
    j = 0   # contador de grupos de 3 letras inicia em zero
    repeticao = 0   # variavel que guarda repeticao inicia em zero
    dist = 0 # distancia entre repetições
    
    for i in range(tamanho):
        
        # se estamos dentro do grupo de 3 letras, e a cifra não é espaço vazio, atualiza as letras de analise
        if(cifra[i] != " " and j < 3):
            letras = letras + cifra[i]
            j = j + 1
        
        dist_sem_espaco = 0
            
        # caso já seja conhecido o grupo de 3 letras a ser analizado
        if(j == 3):
            # varre a string da cifra inteira vendo quantas vezes o grupo de letras se repetiu
            for a in range(tamanho):
                
                if(cifra[a] != " "):
                    dist_sem_espaco = dist_sem_espaco + 1 
                
                if( a < (tamanho - 3)):
                    
                    # salvamos a quantidade de vezes que repetiu
                    if(cifra[a] == letras[0]):
                        if((cifra[a+1] == " ")):
                            
                            # achamos uma repetição e ignoramos o espaço no meio: "a bc"
                            if((cifra[a+2] == letras[1]) and (cifra[a+3] == letras[2])):
                                
                                # queremos salvar a distância entre repetições!
                                # se é a primeira repetição, guarda onde ela ocorreu
                                # se é a segunda, pega a diferença de posição atual e primeira ocorrência
                                if(repeticao == 0):
                                    primeira_ocorrencia = dist_sem_espaco
                                if(repeticao > 0):
                                    dist = dist_sem_espaco - primeira_ocorrencia    
                                repeticao = repeticao + 1
                                
                        else:
                            
                            # achamos uma repeticao das 3 letras sem o espaço "abc"
                            if((cifra[a+1] == letras[1]) and (cifra[a+2] == letras[2])):
                                
                                # guardamos resultado de distância
                                if(repeticao == 0):
                                    primeira_ocorrencia = dist_sem_espaco
                                if(repeticao > 0):
                                    dist = dist_sem_espaco - primeira_ocorrencia     
                                repeticao = repeticao + 1
                                
                            if((cifra[a+2] == " ")):  
                                # achamos a repetição das 3 letras, com um espaço no final: "ab c"
                                if((cifra[a+1] == letras[1]) and (cifra[a+3] == letras[2])):
                                    
                                    # guardamos resultado de distância
                                    if(repeticao == 0):
                                        primeira_ocorrencia = dist_sem_espaco
                                    if(repeticao > 0):
                                        dist = dist_sem_espaco - primeira_ocorrencia     
                                    repeticao = repeticao + 1  

            # se o grupo de letras repetiu em algum ponto, salvamos
            if(repeticao != 0):
                itens.append(letras)
                itens.append(repeticao)
                itens.append(dist)
                    
            j = 0 # zera contador
            letras = "" # esvazia string
            repeticao = 0 # zera repeticao
            dist = 0 # zera distancia
    
    # mostramos o resultado da análise de letras em grupos
    # ------------------------------------------------
    
    tamanho_rep = len(itens)
    quantidade_reps = int(tamanho_rep/3)
        
    print("Analizou-se " + str(quantidade_reps) + "grupos de letras!\n")
    
    j = 0
    for i in range(quantidade_reps):
        print("Grupo de letras: " + str(itens[j]))   
        j = j + 1
        print("Vezes que repetiu: " + str(itens[j]))
        j = j + 1 
        print("Distância entre repetição: " + str(itens[j]) + "\n")
        j = j + 1 

    tamanho_key_chute = int(input("\n\nSugestão para o tamanho da key diante desta análise?\nInforme um número inteiro por favor.\n\n"))

    # analizar frequencia de letras da lingua
    # ------------------------------------------------


    # digamos, a key tem tamanho 6
    # se analisa a posição x dentro desse tamanho 6, pois a posição x a cada 6 letras sofreu o mesmo deslocamento
    # mesmo deslocamento, mesma frequencia da língua escolhida, possibilitando um bom chute

    # Inglês
    if(op == 1):
        
        print("Iniciando análise para texto em Inglês!")
        
        # faz isso para cada letra "y" dentro do tamanho da sugestão de chave, pega um input com sugestão do deslocamento 
        for j in range(tamanho_key_chute):
            print("\n\nANÁLISE PARA POSIÇÃO " + str(j) + " NA CIFRA DE TAMANHO SUGERIDO " + str(tamanho_key_chute))
            frequencia = pega_frequencia_ing(cifra, tamanho_key_chute, j)
        
    # Português    
    if(op == 2):
        
        print("Iniciando análise para texto em Português!")
        # faz isso para cada letra "y" dentro do tamanho da sugestão de chave, pega um input com sugestão do deslocamento 
        for j in range(tamanho_key_chute):
            print("\n\nANÁLISE PARA POSIÇÃO " + str(j) + " NA CIFRA DE TAMANHO SUGERIDO " + str(tamanho_key_chute))
            frequencia = pega_frequencia_ptbr(cifra, tamanho_key_chute, j)
        
    
    # Idioma inválido    
    if((op != 1) and (op != 2)):
        print("Selecione uma opção válida, encerrando programa")

    return 0

# ------------------------------------------------

# Frequências em PT-BR
# a 	14.63%
# b 	1.04%
# c 	3.88%
# d 	4.99%
# e 	12.57%
# f 	1.02%
# g 	1.30%
# h 	1.28%
# i 	6.18%
# j 	0.40%
# k 	0.02%
# l 	2.78%
# m 	4.74%
# n 	5.05%
# o 	10.73%
# p 	2.52%
# q 	1.20%
# r 	6.53%
# s 	7.81%
# t 	4.34%
# u 	4.63%
# v 	1.67%
# w 	0.01%
# x 	0.21%
# y 	0.01%
# z 	0.47% 

# Letras mais frequentes: a, e, o 

# Frequências em Inglês
# a 	8.167%
# b 	1.492%
# c 	2.782%
# d 	4.253%
# e 	12.702%
# f 	2.228%
# g 	2.015%
# h 	6.094%
# i 	6.966%
# j 	0.153%
# k 	0.772%
# l 	4.025%
# m 	2.406%
# n 	6.749%
# o 	7.507%
# p 	1.929%
# q 	0.095%
# r 	5.987%
# s 	6.327%
# t 	9.056%
# u 	2.758%
# v 	0.978%
# w 	2.360%
# x 	0.150%
# y 	1.974%
# z 	0.074% 

# Letras mais frequentes: e, t, a, o 