# trabalho_apa

# Precisa arrumar: 

1opt está criando loops em algumas situações. Precisa analisa-lo ou troca-lo. 

# Pendente de implementação
Calcular o tempo de execução do algoritmo.


# Como rodar o programa
no terminal (dentro da pasta do arquivo do código fonte) digite:
python run.py instancias/"nome da instancia" -c nearest - m "algoritmo" --vnd-methods "algoritmos"(essa ultima parte é para o vnd)

exemplos:

python run.py instancias/P-n19-k2.txt -c nearest 

python run.py instancias/P-n19-k2.txt -c meta

python run.py instancias/P-n19-k2.txt -c nearest -m swap

python run.py instancias/P-n19-k2.txt -c nearest -m vnd --vnd-methods 1opt 2opt swap
