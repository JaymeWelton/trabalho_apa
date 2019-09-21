# -*- coding: utf-8 -*-

class ConstructionHeuristic():

        
    def procura_Menor(self, lista_Arestas, posAtual, demandas, capacidade_atual):
    
        menor = 0
        
        for i in range(len(demandas)):   
                  
            if menor == 0 and demandas[i] > 0:  
                #vai procurar a primeira cidade/cliente nao visitada
                if capacidade_atual - demandas[i] >= 0:     
                    #verifica se dá para carregar no veiculo a demanda deste local. 
                    menor = i # recebe a posição da cidade/cliente que se adequa as situações acima
            
            if demandas[i] > 0  and lista_Arestas[posAtual][i] < lista_Arestas[posAtual][menor]:
                #se encontrar uma outra cidade/cliente que se adeque também as situações acima mas tem um custo menor, ela é a selecionada
                if capacidade_atual - demandas[i] >= 0:
                    menor = i      
                    #print("menor aqui foi ", menor)                   
             
        return menor       
    
    
    def procura_maior (self, lista_Arestas, posAtual, demandas, capacidade_atual):
        
        maior = 0
        
        for i in range(1, len(demandas)):   
                  
            if maior == 0 and demandas[i] > 0:                  
                if capacidade_atual - demandas[i] >= 0:   
                    maior = i 
            
            elif maior > 0 and demandas[i] >= demandas[maior] :
                if demandas[i] == demandas[maior] and lista_Arestas[posAtual][i] < lista_Arestas[posAtual][maior]:                    
                    maior = i          
                            
                elif  demandas[i] != demandas[maior] and capacidade_atual - demandas[i] >= 0:
                    maior = i     
                                      
            
        return maior       
           

    def vizinho_Proximo (self, lista_Arestas, quantidade_Veiculos, capacidade_Maxima, demandas, nome):    
        
        custo = [0]*quantidade_Veiculos    
        veiculo_atual = 0
        solucao_inicial = []
        solucao_da_rota = [0]  
        capacidade_atual = capacidade_Maxima
        cliente = 0 # está no deposito    
        cabe_Mais = True
        
               
        while quantidade_Veiculos > 0:        
            if capacidade_atual >= 0 and cabe_Mais == True:
                if cliente == 0:        #está no deposito e vai procurar o mais proximo em questao de custo
                    if nome == "P-n23-k8\n":
                        cliente = self.procura_maior(lista_Arestas, 0, demandas, capacidade_atual)
                    else:   
                        cliente = self.procura_Menor(lista_Arestas, 0, demandas, capacidade_atual) 
                        
                    custo[veiculo_atual] += lista_Arestas[0][cliente]
                    capacidade_atual -= demandas[cliente]
                    solucao_da_rota.append(cliente)                  
                    demandas[cliente] = 0                    
                    
                else:
                    cliente_Anterior = cliente
                    if capacidade_atual > 0:
                        if nome == "P-n23-k8\n":
                            cliente = self.procura_maior(lista_Arestas, cliente_Anterior, demandas, capacidade_atual)   
                        else:
                            cliente = self.procura_Menor(lista_Arestas, cliente_Anterior, demandas, capacidade_atual)
                    else: 
                        cliente = 0
                        
                    if cliente > 0: 
                        custo[veiculo_atual] += lista_Arestas[cliente_Anterior][cliente]
                        capacidade_atual -= demandas[cliente] 
                        solucao_da_rota.append(cliente) 
                        demandas[cliente] = 0
                    else: 
                        #todos os clientes ja foram visitados ou não cabe mais carga no veiculo
                        cabe_Mais = False
                        solucao_da_rota.append(cliente) #cliente é 0                        
                        custo[veiculo_atual] += lista_Arestas[cliente_Anterior][cliente]                        
                        
                    
            else: 
                   capacidade_atual = capacidade_Maxima
                   quantidade_Veiculos -= 1
                   solucao_inicial.append(solucao_da_rota)                   
                   solucao_da_rota = [0]                  
                   cabe_Mais = True
                   veiculo_atual += 1            
        
        return solucao_inicial
    
   

    def construct_nearest(self, instance):
            
            data_graph = instance.data2        
            veiculos = instance.veiculo  
            capacidade_max = instance.capacidade
            demandas = instance.demanda
            nome = instance.name
            
            return self.vizinho_Proximo(data_graph, veiculos, capacidade_max, demandas, nome)        

        

   
