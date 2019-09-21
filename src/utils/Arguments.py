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
            'instance', help="File with instances", type=str)
        parser.add_argument('-c', '--construction', help="Construction heuristic",
                            choices=['nearest'], default='nearest', type=str)
        parser.add_argument('-m', '--method', help="Heuristic approach",
                            choices=['swap','1opt' ,'2opt', 'vnd', 'all'], default='all', type=str)
        parser.add_argument('-i', '--improvement', help="Type of improvement choice",
                            choices=['best', 'first'], default='best', type=str)
        parser.add_argument('--vnd-methods', help="Sequence of the methods used in VND approach",
                            nargs='*', choices=['swap', '2opt', '1opt'], default=['swap', '2opt'], type=str)
              
        
        self.args = parser.parse_args()
