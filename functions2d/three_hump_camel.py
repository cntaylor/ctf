# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class ThreeHumpCamel(Function2D):
    """ Three Hump Camel Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-5.0, 5.0], [-5.0, 5.0]])
        self.smooth = True
        self.info = [True, True, True]
        self.latex_name = "Three Hump Camel Function"
        self.latex_type = "Valley Shaped"
        self.latex_cost = r'\[ f(x,y) = 2x^{2} - 1.05x^{4} + \frac{x^{6}}{6} + xy + y^{2} \]'
        self.latex_desc = "The function has three local minima.  "

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = np.zeros(1)
        # Calculate Cost
        cost[0] = 2.0*x[0]**2.0 - 1.05*x[0]**4.0 + (x[0]**6.0)/6.0 + x[0]*x[1] + x[1]**2.0
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Grad
        grad = np.zeros(2)
        # Calculate Grads
        grad[0] = 4.0*x[0]**1.0 - 4.2*x[0]**3.0 + 1.0*x[0]**5.0 + x[1]
        grad[1] = x[0] + 2.0*x[1]**1.0
        # Return Grad
        return grad

    def hess(self, x):
        """ Hess function. """
        # Hess
        hess = np.zeros(1)
        # Calculate Hess
        hess[0][0] = -12.6*x[0]**2.0 + 5.0*x[0]**4.0 + 4.0
        hess[0][1] = 1.0
        hess[1][0] = hess[0][1]
        hess[1][1] = 2.0
        # Return Hess
        return hess