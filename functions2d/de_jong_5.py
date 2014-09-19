# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D
from itertools import product


# Problem
class DeJong5(Function2D):
    """ De Jong No. 5 Function. """

    def __init__(self):
        """ Constructor. """
        # Constants
        self.a = np.array(list(product(range(-32, 33, 16), range(-32, 33, 16))))
        # Information
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-65.536, 65.536], [-65.536, 65.536]])
        self.n = 2
        self.smooth = True
        self.info = [True, False, False]
        # Description
        self.latex_name = "De Jong No. 5"
        self.latex_type = "Steep"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "The fifth function of De Jong is multimodal, with very sharp drops on a mainly flat surface.  "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = 1.0/(0.002 + np.sum([1.0/(i + (x[0] - self.a[i][0])**6 + (x[1] - self.a[i][1])**6) for i in range(0, 25)], axis=0))
        # Return Cost
        return c