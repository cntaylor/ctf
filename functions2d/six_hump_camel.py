# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class SixHumpCamel(Function2D):
    """ Six Hump Camel Function. """

    def __init__(self):
        """ Constructor. """
        # Information
        self.min = np.array([[0.0898, -0.7126],
                             [-0.0898, 0.7126]])
        self.value = np.array([-1.0316])
        self.domain = np.array([[-3.0, 3.0], [-2.0, 2.0]])
        self.n = 2
        self.smooth = True
        self.info = [True, False, False]
        # Description
        self.latex_name = "Six Hump Camel Function"
        self.latex_type = "Valley Shaped"
        self.latex_cost = r'\[ f(x,y) = ... \]'
        self.latex_desc = "The function has six local minima.  "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = (4 - 2.1*x[0]**2 + x[0]**4/3)*x[0]**2 + x[0]*x[1] + (-4 + 4*x[1]**2)*x[1]**2
        # Return Cost
        return c