# -*- coding: utf-8 -*-

import numpy as np
import re
from src.Instance import Instance
from src.Node import Node
from src.Neighbor import Neighbor


class InstanceReader():
    
    def get_instance(self, instance_path):
        
        name = ""
        dimension = ""
        veiculos = ""
        capacidade = "" 
        demanda = []
        data = []        
        
        
        with open(instance_path, 'r', encoding='utf-8') as file:
            
            name = file.readline().split(' ')[-1]
            dimension = int(file.readline().split(' ')[-1])
            veiculos = int(file.readline().split(' ')[-1])
            capacidade = int(file.readline().split(' ')[-1])
            demanda = []
            inicio_da_secao_Edge_Weight = 5
            
            file.readline()           #DEMAND_SECTION:
            
            for i in range(dimension):
                stringAuxiliar = file.readline()      
                stringAuxiliar2 = (re.findall('\d+', stringAuxiliar))# vai criar uma lista apenas com os valores (removendo os espaços)
                demanda.append(int(stringAuxiliar2[1])) #vai receber apenas o segundo valor na parte de demanda.
                inicio_da_secao_Edge_Weight += 1            
            inicio_da_secao_Edge_Weight += 2            
                
            file.readline()  #linha vazia antes do EDGE WEIGHT SECTION
            
            file_type = file.readline().strip()

            if file_type == 'EDGE_WEIGHT_SECTION': 
                                
                 data2 = [[0 for x in range(dimension)]for y in range(dimension)]  #matriz [Dimensao][Dimensao]
                 
                 fop = open(instance_path, "r")
                 arquivo = fop.readlines()
                
                 for i in range(dimension):
                     stringAuxiliar = arquivo[inicio_da_secao_Edge_Weight]
                     stringAuxiliar2 = (re.findall('\d+', stringAuxiliar))                     
                     for j in range(dimension):            
                        data2[i][j] = int(stringAuxiliar2[j]) 
                     inicio_da_secao_Edge_Weight += 1      
                     
                 data = self.__get_instance(file, dimension) 
                 
                 

        return Instance(name, dimension, veiculos, capacidade, demanda, data, data2)
    
   
    def __get_instance(self, file, dimension):
        data = np.zeros(shape=(dimension, dimension))

        for i in range(dimension):
            line = file.readline()
            numbers = []

            for item in line.split(' '):
                try:
                    number = float(item)
                    numbers.append(number)
                except ValueError:
                    pass
            data[i] = numbers  
            

        return self.__convert_to_graph(data, dimension)
    

    def __convert_to_graph(self, data, dimension, points=[]):
        nodes = [Node(i) for i in range(dimension)]

        for i, costs in enumerate(data):
            neighborhood = []

            for j, cost in enumerate(costs):
                neighborhood.append(Neighbor(node=nodes[j], cost=cost))

            nodes[i].neighborhood = neighborhood

        return nodes
