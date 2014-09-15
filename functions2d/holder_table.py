# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class HolderTable(Function2D):
    """ Holder Table Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([[8.05502, 9.66459],
                             [-8.05502, 9.66459],
                             [8.05502, -9.66459],
                             [-8.05502, -9.66459]])
        self.value = np.array([-19.2085, -19.2085, -19.2085, -19.2085])
        self.domain = np.array([[-15.0, -5.0], [-3.0, 3.0]])
        self.smooth = False
        self.info = [True, False, False]
        self.latex_name = "Holder Table Function"
        self.latex_type = "Many Local Minima"
        self.latex_cost = r'\[ f(x, y) = ... \]'
        self.latex_desc = "The Holder Table function has many local minima, with four global minima. "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = -np.abs(np.sin(x[0])*np.cos(x[1])*np.exp(np.abs(1 - np.sqrt(x[0]**2 + x[1]**2)/np.pi)))
        # Return Cost
        return c