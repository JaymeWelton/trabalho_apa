def mergeSort(lista):

    if len(lista) > 1:

        meio = len(lista)//2       

        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1



def main():
    #vai receber um arquivo de entrada onde esse arquivo conterá:
    # primeira linha se refere ao tamanho da mochila (capacidade)
    #as linhas restantes tem 2 colunas por linha: peso e valor
    try:
        f = open("arquivo.txt", "r")
    except IOError:    
        print("erro! arquivo nao pode ser aberto, programa será encerrado")
        return
    
    f1 = f.readlines()#f1 vai receber cada linha do arquivo .txt
    
    peso = []
    peso_ordenado = []#vai armazenar os pesos ordenados baseado no valor_por_peso depois do merge
    valor = []       
    valor_por_peso = []  # peso/valor
    valor_peso_sem_ordenar = [] #vai copiar o valor_por_peso para comparar depois
        
    for i in range(len(f1)):        
        #nesse for vai ser separado os valores de peso e valor e depois calculado o valor por peso
        if i == 0:
            peso_mochila = int(f1[0])#capacidade da mochila
        else:            
            auxiliar = f1[i] #auxiliar é uma string de cada linha do arquivo que f1 leu
            peso.append(auxiliar[:auxiliar.find(" ") + 1])       
            valor.append(auxiliar[auxiliar.find(" ") + 1:])
            valor_por_peso.append(int(valor[i-1])/int(peso[i-1])) 
            valor_peso_sem_ordenar.append(valor_por_peso[i-1])
            
            
    
    mergeSort(valor_por_peso)#ordena os valores por peso 
     
    #precisa ordenar os pesos em relação a ordenação anterior, para poder calcular o peso restante na mochila.
    for i in range(len(f1) -1):   
         for j in range(len(f1) -1):
             if valor_por_peso[i] == valor_peso_sem_ordenar[j]: 
                 peso_ordenado.append(int(peso[j]))
                 break
    
    
    posicao_Atual = len(f1)-2
    valor_obtido = 0
    
    while (1):
        if peso_mochila > 0:      #se tiver espaço na mochila    
            for i in range(peso_ordenado[posicao_Atual]): #enquanto tiver desse material valioso                  
                valor_obtido = valor_obtido + valor_por_peso[posicao_Atual] #atualiza o valor que tem na mochila (cada iteração ganha o valor equivalente a uma unidade do material)
                peso_mochila = peso_mochila - 1 #uma unidade da mochila é ocupada
                if peso_mochila == 0:#se a mochila encher, encerra
                    break
            
            posicao_Atual = posicao_Atual - 1 
            if posicao_Atual == -1:# se já tiver pego todo material valioso, encerra
                break
            
        else:
            break
        
    print(peso_mochila)
    print(valor_obtido)    
       
    f.close() 




if __name__ == '__main__':
    main()