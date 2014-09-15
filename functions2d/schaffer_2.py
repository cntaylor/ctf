# Imports
import numpy as np
from problems.problems2d.problem2d import Problem2D


# Problem
class Schaffer2(Problem2D):
    """ Schaffer No. 2 Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-100.0, -100.0], [-100.0, 100.0]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Schaffer No. 2 Function"
        self.latex_type = "Many Local Minima"
        self.latex_cost = r'$\displaystyle f(x, y)  = ... $'
        self.latex_desc = "The second Schaffer function has many local minima. "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = 0.5 + (np.sin(x[0]**2 - x[1]**2)**2 - 0.5)/(1 + 0.001*(x[0]**2 + x[1]**2))**2
        # Return Cost
        return c