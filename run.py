# -*- coding: utf-8 -*-

from src.utils.Arguments import Arguments
from src.utils.InstanceReader import InstanceReader
from src.ConstructionHeuristic import ConstructionHeuristic
#from src.utils.utils import calculate_cost, solution_to_string
from src.neighborhoodsearch import swap_method, one_opt_method, two_opt_method, vnd_method


def main(args):
    reader = InstanceReader()
    instance = reader.get_instance(args.instance)
    quantidade_de_veiculos = instance.veiculo
    construction = ConstructionHeuristic()
    initial_solution = []
    custo = []
    one_opt_solution = [quantidade_de_veiculos]
    custo_one_opt = [quantidade_de_veiculos]
    custo_total = 0

    if args.construction == 'nearest':
        initial_solution,custo = construction.construct_nearest(instance)        
        custo_total = 0
        
    for i in range(quantidade_de_veiculos):
        print("Rota %d: " %(i+1),initial_solution[i])
        print("Custo da rota %d = %d" % (i+1, custo[i]))
        custo_total += custo[i]
        if i == quantidade_de_veiculos-1:
            print("Custo total inicial = \n", custo_total)

         
    #nao vai funcionar        
    if args.method in ['1opt']: 
        custo_total = 0                      
        for i in range(quantidade_de_veiculos):
            one_opt_solution[i],custo_one_opt[i] = one_opt_method(initial_solution[i], custo[i], is_first=(args.improvement == 'first'))
            print("Rota %d do 1opt: " %(i+1),initial_solution[i])
            print("Custo da rota %d do 1opt = %d" % (i+1, custo[i]))
            custo_total += custo_one_opt[i]
            if i == quantidade_de_veiculos-1:
                print("Custo total do do 1opt = \n", custo_total)
          

    
    if args.method in ['2opt']:

        two_opt_solution = two_opt_method(initial_solution, is_first=(args.improvement == 'first'))
        print()
       # print("Solucao do 2-OPT: ", solution_to_string(two_opt_solution))
       # print("Custo do 2-OPT: ", calculate_cost(two_opt_solution))
        
        
    if args.method in ['swap']:
        
        swap = swap_method(initial_solution, is_first=(args.improvement == 'first'))
        print()
       # print("Solucao do SWAP: ", solution_to_string(swap))
       # print("Custo do SWAP: ", calculate_cost(swap))    
    

    if args.method in ['vnd']:        
        vnd_solution = vnd_method(initial_solution, args.vnd_methods)
        print()
       # print("Solucao do VND: ", solution_to_string(vnd_solution))
       # print("Custo do VND:", calculate_cost(vnd_solution))

       


if __name__ == '__main__':
    args = Arguments().args
    main(args)
    
