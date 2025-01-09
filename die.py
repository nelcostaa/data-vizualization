from random import randint


class Die:
    """Classe que representa um unico dado"""

    def __init__(self, num_sides=6):
        """Faz a suposicao de que um dado tem seis lados"""
        self.num_sides = num_sides

    def roll(self):
        """Retorna um valor aleatorio entre 1 e o numero de lados"""
        return randint(1, self.num_sides)
