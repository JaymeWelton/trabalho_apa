# -*- coding: utf-8 -*-

from copy import copy
from src.utils.utils import  calculate_cost,swap_neighborhood,calculate_swap_cost, swap_2opt, swap_1opt


def swap_method(initial_solution, matriz):
    
    current_solution = copy(
        initial_solution)       # Copy initial solution as current solution 
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution, matriz)
    
    size_points = len(initial_solution)     # Get the number of points
    has_improvement = True      # Check if has improvement

    while has_improvement:
        has_improvement = False

        for i in range(1, size_points - 2):
            for j in range(i+1, size_points-1):

                # Calculate swap cost
                candidate_cost = min_cost + calculate_swap_cost(current_solution, i, j, matriz)

                # Check if the candidate's cost is the lowest
                if candidate_cost < min_cost:
                    has_improvement = True
                    min_cost = candidate_cost      # Change the lowest cost
                    current_solution = swap_neighborhood(
                        current_solution, i, j)     # Change the best solution
                          

           

    return current_solution



def one_opt_method(initial_solution, matriz):
   
    current_solution = copy(initial_solution) # Copy initial solution as current solution   
    # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution, matriz)
    
    size_points = len(initial_solution)     # Get the number of points
    has_improvement = True      # Check if has improvement  

    while has_improvement:
        has_improvement = False

        for i in range(1, size_points - 1):
            for j in range(i+1, size_points):

                # Swap
                candidate_cost = min_cost + calculate_swap_cost(current_solution, i, j, matriz, False)

                # Check if the candidate's cost is the lowest
                if candidate_cost < min_cost:
                    has_improvement = True
                    min_cost = candidate_cost       # Change the lowest cost
                    # Change the best solution
                    current_solution = swap_1opt(current_solution, i, j)
                    

    return current_solution



def two_opt_method(initial_solution, matriz):
   
     # Copy initial solution as current solution
    current_solution = copy(initial_solution)      
     # Caculate the cost of the solution
    min_cost = calculate_cost(initial_solution, matriz)
    
    size_points = len(initial_solution)     # Get the number of points
    has_improvement = True      # Check if has improvement
   
    while has_improvement:
        has_improvement = False

        for i in range(1,size_points - 1):
            for j in range(i+1, size_points):

                # Swap                
                candidate_cost = min_cost + calculate_swap_cost(current_solution, i, j, matriz, True)

                # Check if the candidate's cost is the lowest
                if candidate_cost < min_cost:
                    has_improvement = True
                    min_cost = candidate_cost       # Change the lowest cost
                    # Change the best solution
                    current_solution = swap_2opt(current_solution, i, j)


    return current_solution


def vnd_method(solucao_inicial, metodos, matriz):
    
    solucao_atual = copy(
        solucao_inicial)       # Copia a solução inicial
    
    # Caculate the cost of the solution
    menor_custo = calculate_cost(solucao_inicial, matriz)
   
    k = 0
    
    methods_dict = {'swap': swap_method, '2opt': two_opt_method, '1opt': one_opt_method}
    
    while k < len(metodos):
        # Procura a melhor solução usando os algorítmos de vizinhança
        metodo_selecionado = ""

        if k == 0:
            metodo_selecionado = 'swap'
        elif k == 1:
            metodo_selecionado = '2opt'
        elif k == 2:
            metodo_selecionado = '1opt'

        melhor_candidato = methods_dict[metodo_selecionado](solucao_atual, matriz)
        # Calcula o custo da nova solução encontrada
        custo_candidato = calculate_cost(melhor_candidato, matriz)

        # Verifica se a solução encontrada é melhor, se for, repete o while
        #com k=0, caso contrário, ele soma k+1 e testa o proximo
        #método de vizinhança até k=3 e sai do laço com a resposta ótima
        if custo_candidato < menor_custo:
            solucao_atual = melhor_candidato
            menor_custo = custo_candidato       
            k = 0       # Reinicia a contagem
        else:
            k += 1      # Próximo algorítmo

    return solucao_atual


