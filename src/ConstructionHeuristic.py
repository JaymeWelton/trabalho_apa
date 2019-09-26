# -*- coding: utf-8 -*-

import random
from src.utils.utils import calculate_cost 
from src.neighborhoodsearch import swap_method

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
                        capacidade_atual -= demandas[cliente] 
                        solucao_da_rota.append(cliente) 
                        demandas[cliente] = 0
                    else: 
                        #todos os clientes ja foram visitados ou não cabe mais carga no veiculo
                        cabe_Mais = False
                        solucao_da_rota.append(cliente) #cliente é 0                        
                                             
                        
                    
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
    
   
       
            
    def construct_random(self, varianca, lista_Arestas, capacidade_Maxima, demanda):
        
        cliente = 0 # está no deposito 
        rotafinal = [0]        
        capacidade_atual = capacidade_Maxima
        menor = maior = 0
        cabe_Mais = True
        LCR = []
        cidade_random = 0
        demandas = demanda.copy()
         
        while cabe_Mais == True:
            
            if cliente == 0: 
                
                for i in range(1, len(demandas)):
                                            
                    if menor == 0 and demandas[i] > 0 or lista_Arestas[0][i] < menor and demandas[i] > 0:
                            if capacidade_atual - demandas[i] >= 0: 
                                menor = lista_Arestas[0][i]
                            if maior == 0:
                                maior = lista_Arestas[0][i]
                            
                    elif lista_Arestas[0][i] > maior:
                            maior = lista_Arestas[0][i]
                            
                            
                for i in range(1, len(demandas)):
                    if lista_Arestas[0][i] <= (menor + (varianca*(maior - menor))) and demandas[i] > 0:                        
                        LCR.append(i)
                        
                       
                cidade_random = random.sample(LCR, 1)      
                capacidade_atual -= demandas[cidade_random[0]] 
                demandas[cidade_random[0]] = 0 
                rotafinal.append(cidade_random[0])
                cliente = 1
                    
                            
            else:                     
                cliente_anterior = cidade_random[0]                    
                LCR = []
                
                if capacidade_atual > 0:    
                    
                    menor = maior = 0
                    
                    for i in range(1, len(demandas)):
                        
                        if menor == 0 and demandas[i] > 0 or lista_Arestas[cliente_anterior][i] < menor and demandas[i] > 0:
                            if capacidade_atual - demandas[i] >= 0: 
                                menor = lista_Arestas[cliente_anterior][i]
                            if maior == 0:
                                maior = lista_Arestas[cliente_anterior][i]
                            
                        elif lista_Arestas[cliente_anterior][i] > maior:
                            maior = lista_Arestas[cliente_anterior][i]
                              
                    for i in range(1, len(demandas)):        
                        if lista_Arestas[cliente_anterior][i] > 0 and lista_Arestas[cliente_anterior][i] <= (menor + (varianca*(maior - menor))):
                           
                            if capacidade_atual - demandas[i] >= 0 and demandas[i] > 0:  
                                LCR.append(i)                        
                                           
                    
                    if len(LCR) > 0:
                        cidade_random = random.sample(LCR, 1)                         
                        capacidade_atual -= demandas[cidade_random[0]] 
                        demandas[cidade_random[0]] = 0
                        #print(demandas)
                        rotafinal.append(cidade_random[0])
                        
                    else:
                        #provavelmente não há mais cidades que caibam nessa rota, então ela deve encerrar. 
                        cabe_Mais = False
                        rotafinal.append(0) #volta para o deposito
                    
                else:              
                    cabe_Mais = False
                    rotafinal.append(0)       
                    
        #print(rotafinal)            
        return rotafinal, demandas                 
                                          
   
    def construct_meta(self, instance, graspMax, demandas):
        
        lista_Arestas = instance.data2    
        capacidade_max = instance.capacidade          
        solucao_final = []
        melhorcusto = 0
        
        for i in range(graspMax):
            melhor_rota, newdemanda  = self.construct_random(0, lista_Arestas, capacidade_max, demandas)            
            busca_local = swap_method(melhor_rota, lista_Arestas)
            
            custo_atual = calculate_cost(busca_local, lista_Arestas)
            
            if custo_atual < melhorcusto or melhorcusto == 0:
                melhorcusto = custo_atual
                solucao_final = busca_local
                melhor_demanda = newdemanda
        
        return solucao_final, melhor_demanda
        



      
        
   
        
        

   
