# -*- coding: utf-8 -*-


class Instance():
    """Instance element

    Attributes:
         name {str} -- nome da instancia
            dimension {int} -- demensão da instancia
            veiculo {int} -- quantidade de veiculos da instancia
            capacidade {int} -- capacidade de cada veiculo
            demanda {list} -- quantidade de carga que cada cliente/cidade vai demandar
            data {list} -- tabela com o custo da distancia entre as cidades/clientes
    """

    def __init__(self, name, dimension, veiculo, capacidade, demanda, data, data2):
        """Constructor

        Arguments:
            name {str} -- nome da instancia
            dimension {int} -- demensão da instancia
            veiculo {int} -- quantidade de veiculos da instancia
            capacidade {int} -- capacidade de cada veiculo
            demanda {list} -- quantidade de carga que cada cliente/cidade vai demandar
            data {list} -- tabela com o custo da distancia entre as cidades/clientes
        """
        self.name = name
        self.dimension = dimension
        self.veiculo = veiculo
        self.capacidade = capacidade
        self.demanda = demanda
        self.data = data #armazena a matriz edge_weight em forma de nós (node)
        self.data2 = data2 #armazena a matriz edge_weight em forma de lista de inteiros