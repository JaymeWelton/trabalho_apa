# -*- coding: utf-8 -*-

import argparse


class Arguments():
    """Handle the arguments

    Attributes:
        args {Object} -- object with the arguments
    """

    def __init__(self):
        """Arguments constructor
        """

        parser = argparse.ArgumentParser()
        parser.add_argument(
            'instance', help="arquivo com instancias", type=str)
        parser.add_argument('-c', '--construction', help="Construcao heuristica",
                            choices=['nearest', 'meta'], default='', type=str)
        parser.add_argument('-m', '--method', help="Algoritmos de vizinhanca",
                            choices=['swap','1opt' ,'2opt', 'vnd', 'all'], default='all', type=str)        
        parser.add_argument('--vnd-methods', help="Sequencia de metodos usado no VND",
                            nargs='*', choices=['swap', '2opt', '1opt'], default=['swap', '2opt'], type=str)
              
        
        self.args = parser.parse_args()
