# trabalho_apa

# Dificuldades encontradas
As 3 últimas instâncias (P-n50-k10.txt, P-n51-k10.txt e P-n55-k7) ao serem executadas pelo algorítmo 1opt, apresenta dificuldade de encontrar todas as rotas dos caminhões e não conclui seu procedimento;

Após passar pelo primeiro algoritmo de vizinhança e passar o resultado pro próximo algoritmo, ocorre uma alteração no deposito fazendo com que ele apareça em posições diferentes dentro da rota.

A instância P-n23-k8.txt utiliza-se de 8 veículos com capacidade máxima de 40 para cada veículo, mas as demandas dos cliente/cidades são consideravelmente altas para essa carga, dificultando o bom funcionamento do algoritmo. 
Da forma que foi implementada o algoritmo guloso do vizinho mais próximo, ele gera as 8 rotas, mas um cliente/cidade não é encaixado, ficando não visitado (o que também gera um custo menor da rota). 

# Pendente de implementação
Calcular o tempo de execução do algoritmo.


# Como rodar o programa
no terminal (dentro da pasta do arquivo do código fonte) digite:
python run.py instancias/"nome da instancia" -c nearest - m "algoritmo" --vnd-methods "algoritmos"(essa ultima parte é para o vnd)

exemplos:

python run.py instancias/P-n19-k2.txt -c nearest 

python run.py instancias/P-n19-k2.txt -c nearest - m swap

python run.py instancias/P-n19-k2.txt -c nearest - m vnd --vnd-methods 1opt 2opt swap
