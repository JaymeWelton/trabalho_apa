# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:21:31 2019

"""

import re







def main():
    #vai receber um arquivo de entrada que tem as informações da instância
    #é necessário editar o nome do arquivo na função abaixo caso deseje-se testar outra instância
    
    try:
        f = open("P-n19-k2.txt", "r")
    except IOError:    
        print("erro! arquivo nao pode ser aberto, programa será encerrado")
        return
    
    f1 = f.readlines()#f1 vai receber cada linha do arquivo .txt
    
    stringAuxiliar = f1[1]
    Dimensao = int(stringAuxiliar[stringAuxiliar.find(" ") + 1:])
    
    stringAuxiliar = f1[2]
    Veiculos = int(stringAuxiliar[stringAuxiliar.find(" ") + 1:])
    
    stringAuxiliar = f1[3]
    Capacidade = int(stringAuxiliar[stringAuxiliar.find(" ") + 1:])
    
    Demanda = []   
    
    inicio_das_Arestas = 0
    
    for i in range(5, len(f1)):
        stringAuxiliar = f1[i]      
        if stringAuxiliar != '\n':
            stringAuxiliar2 = (re.findall('\d+', stringAuxiliar))# vai criar uma lista apenas com os valores (removendo os espaços)
            Demanda.append(int(stringAuxiliar2[1])) #vai receber apenas o segundo valor na parte de demanda.
        else:
            inicio_das_Arestas = i + 2
            break
                
    Arestas = [[0 for x in range(Dimensao)]for y in range(Dimensao)]  #matriz [Dimensao][Dimensao]
    
    for i in range(Dimensao):
        stringAuxiliar = f1[inicio_das_Arestas]
        stringAuxiliar2 = (re.findall('\d+', stringAuxiliar))
        for j in range(Dimensao):            
            Arestas[i][j] = int(stringAuxiliar2[j])
        
        inicio_das_Arestas = inicio_das_Arestas + 1
        
    
    
    f.close() 




if __name__ == '__main__':
    main()