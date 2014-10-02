# Imports
import numpy as np

from ctf.functions2d.function2d import Function2D



# Problem
class AbsoluteSkewed(Function2D):
    """ Absolute Skewed Function. """

    def __init__(self):
        """ Constructor. """
        # Information
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-np.inf, np.inf], [-np.inf, np.inf]])
        self.n = 2
        self.smooth = True
        self.info = [True, False, False]
        # Description
        self.latex_name = "Absolute Skewed Function"
        self.latex_type = "Bowl-Shaped"
        self.latex_cost = r"\[ f(\mathbf{x}) = | \mathbf{A}_{00} \mathbf{x}_0 + \mathbf{A}_{01} \mathbf{x}_1 | +" \
                          r"| \mathbf{A}_{10} \mathbf{x}_0 + \mathbf{A}_{11} \mathbf{x}_1 | \]"
        self.latex_desc = "Demonstration case where simple coordinate descent fails."
        # Constants
        self.skew = np.array([[2*np.cos(np.pi/4), -2*np.sin(np.pi/4)], [np.sin(np.pi/4), np.cos(np.pi/4)]])

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = np.abs(self.skew[0][0]*x[0] + self.skew[0][1]*x[1]) + np.abs(self.skew[1][0]*x[0] + self.skew[1][1]*x[1])
        # Return Cost
        return c