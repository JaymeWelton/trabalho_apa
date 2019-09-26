# -*- coding: utf-8 -*-

from src.utils.Arguments import Arguments
from src.utils.InstanceReader import InstanceReader
from src.ConstructionHeuristic import ConstructionHeuristic
from src.utils.utils import calculate_cost
from src.neighborhoodsearch import swap_method, one_opt_method, two_opt_method, vnd_method


def main(args):
    reader = InstanceReader()
    instance = reader.get_instance(args.instance)
    quantidade_de_veiculos = instance.veiculo
    matriz_de_Custos = instance.data2
    construction = ConstructionHeuristic()
    
    initial_solution = []
    meta_solution = []
    custo = [0]*quantidade_de_veiculos    
    one_opt_solution = [0]*quantidade_de_veiculos   
    two_opt_solution=[0]*quantidade_de_veiculos 
    swap = [0]*quantidade_de_veiculos
    vnd_solution = [0]*quantidade_de_veiculos
    custo_total = 0
    

    if args.construction == 'meta':        
        
        for i in range(quantidade_de_veiculos):
            
            if i == 0:
                meta_solution, novademanda = construction.construct_meta(instance, 100, instance.demanda, args.vnd_methods)
                initial_solution.append(meta_solution)
            else:
                meta_solution, novademanda = construction.construct_meta(instance, 100, novademanda, args.vnd_methods) 
                initial_solution.append(meta_solution)
            
            print("Rota %d pelo GRASP: " %(i+1), meta_solution)
            custo[i] = calculate_cost(meta_solution, matriz_de_Custos)
            print("Custo da rota %d = %d" % (i+1, custo[i]))
            custo_total += custo[i]
            if i == quantidade_de_veiculos-1:
                print("Custo total pelo GRASP = %d\n" %custo_total) 
                print(novademanda)#printa a lista de demanda para saber se tem clientes que estão ficando de fora
      
        
    if args.construction == 'nearest':
        initial_solution = construction.construct_nearest(instance)  
        custo_total = 0
        
        for i in range(quantidade_de_veiculos):
            print("Rota %d: " %(i+1),initial_solution[i])
            custo[i] = calculate_cost(initial_solution[i], matriz_de_Custos)
            print("Custo da rota %d = %d" % (i+1, custo[i]))
            custo_total += custo[i]
            if i == quantidade_de_veiculos-1:
                print("Custo total pelo algoritmo guloso = %d\n" %custo_total)     
    

                  
    if args.method in ['1opt']: 
        custo_total = 0    
                  
        for i in range(quantidade_de_veiculos):
            one_opt_solution[i] = one_opt_method(initial_solution[i], matriz_de_Custos)
            print("Rota %d do 1opt: " %(i+1),one_opt_solution[i])
            custo[i] = calculate_cost(one_opt_solution[i], matriz_de_Custos)
            print("Custo da rota %d do 1opt = %d" % (i+1, custo[i]))
            custo_total += custo[i]
            if i == quantidade_de_veiculos-1:
                print("Custo total do 1opt = %d\n" %custo_total)
          

    
    if args.method in ['2opt']:
        custo_total = 0  
        
        for i in range(quantidade_de_veiculos):
            two_opt_solution[i] = two_opt_method(initial_solution[i], matriz_de_Custos)
            print("Rota %d do 2opt: " %(i+1),two_opt_solution[i])
            custo[i] = calculate_cost(two_opt_solution[i], matriz_de_Custos)
            print("Custo da rota %d do 2opt = %d" % (i+1, custo[i]))
            custo_total += custo[i]
            if i == quantidade_de_veiculos-1:
                print("Custo total do 2opt = %d\n" %custo_total)
        
        
    if args.method in ['swap']:
        custo_total = 0          
        
        for i in range(quantidade_de_veiculos):
            swap[i] = swap_method(initial_solution[i], matriz_de_Custos)
            print("Rota %d do swap: " %(i+1),swap[i])
            custo[i] = calculate_cost(swap[i], matriz_de_Custos)
            print("Custo da rota %d do swap = %d" % (i+1, custo[i]))
            custo_total += custo[i]
            if i == quantidade_de_veiculos-1:
                print("Custo total do swap = %d\n" %custo_total)  
    

    if args.method in ['vnd']:     
        custo_total = 0  
        
        for i in range(quantidade_de_veiculos):
            vnd_solution[i] = vnd_method(initial_solution[i], args.vnd_methods, matriz_de_Custos)            
            print("Rota %d do VND: " %(i+1),vnd_solution[i])
            custo[i] = calculate_cost(vnd_solution[i], matriz_de_Custos)
            print("Custo da rota %d do VND = %d" % (i+1, custo[i]))
            custo_total += custo[i]
            if i == quantidade_de_veiculos-1:
                print("Custo total do VND = %d\n" %custo_total)  

       


if __name__ == '__main__':
    args = Arguments().args
    main(args)
    
