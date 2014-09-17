# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class SumOfDifferentPowers(Function2D):
    """ Sum of Different Powers Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-1, 1], [-1, 1]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Sum of Different Powers Function"
        self.latex_type = "Bowl-Shaped"
        self.latex_cost = "\[ f(x,y) = \sum_{i=1}^d  |x_i|^{i+1} \]"
        self.latex_desc = " The Sum of Different Powers function is unimodal. It is shown here in its two-dimensional" \
                          " form.  "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = np.sum([np.abs(x[i])**(i+2) for i in range(0, 2)])
        # Return Cost
        return c
