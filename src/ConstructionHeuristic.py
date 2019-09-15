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
           

    def vizinho_Proximo (self, lista_Arestas, quantidade_Veiculos, capacidade_Maxima, demandas):    
        
        custo = [0]*quantidade_Veiculos    
        veiculo_atual = 0
        solucao_inicial = []
        solucao_da_rota = [0]  
        capacidade_atual = capacidade_Maxima
        cliente = 0 # está no deposito    
        cabe_Mais = True
        
        while quantidade_Veiculos > 0:        
            if capacidade_atual > 0 and cabe_Mais == True:
                if cliente == 0:        #está no deposito e vai procurar o mais proximo em questao de custo
                    cliente = self.procura_Menor(lista_Arestas, 0, demandas, capacidade_atual) 
                    custo[veiculo_atual] += lista_Arestas[0][cliente]
                    capacidade_atual -= demandas[cliente]
                    solucao_da_rota.append(cliente)                  
                    demandas[cliente] = 0
                    
                else:
                    cliente_Anterior = cliente
                    cliente = self.procura_Menor(lista_Arestas, cliente_Anterior, demandas, capacidade_atual)
                    
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
            
        
        return solucao_inicial, custo


  #  def construct_nearest(self, instance):
            
   #         data_graph = instance.data2        
    #        veiculos = instance.veiculo  
     #       capacidade_max = instance.capacidade
      #      demandas = instance.demanda
            
       #     return self.vizinho_Proximo(data_graph, veiculos, capacidade_max, demandas)        

        def construct_nearest(self, instance, inital=0):
            """Construct the inital solution
    
            Arguments:
                instance {Instance} -- instance object
    
            Returns:
                list -- initial solution
            """
            data_graph = instance.data
            initial_solution = [data_graph[inital]]
    
            while len(initial_solution) < instance.dimension:
                last_node = initial_solution[-1]
                nearest_nodes = sorted(last_node.neighborhood,
                                       key=(lambda x: x.cost))                
    
                for neighbor in nearest_nodes[1:]:
                    if neighbor.node.key not in [node.key for node in initial_solution]:
                        initial_solution.append(neighbor.node)
                        break
    
            return initial_solution  

   
