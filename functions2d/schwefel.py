# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class Schwefel(Function2D):
    """ Schwefel Function. """

    def __init__(self):
        """ Constructor. """
        # Information
        self.min = np.array([420.9687, 420.9687])
        self.value = 0.0
        self.domain = np.array([[-500, 500], [-500, 500]])
        self.n = 2
        self.smooth = True
        self.info = [True, False, False]
        # Description
        self.latex_name = "Schwefel Function"
        self.latex_type = "Many Local Minima"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "The Schwefel function is complex, with many local minima."

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = 418.9829*2 - x[0]*np.sin(np.sqrt(np.abs(x[0]))) - x[1]*np.sin(np.sqrt(np.abs(x[1])))
        # Return Cost
        return c