# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class RotatedHyperEllipsoid(Function2D):
    """ Rotated Hyper-Ellipsoid Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-65.536, 65.536], [-65.536, 65.536]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Rotated Hyper-Ellipsoid Function"
        self.latex_type = "Bowl-Shaped"
        self.latex_cost = "\[ f(x,y) = \sum_{i=1}^d \sum_{j=1}^i x_j^2 \]"
        self.latex_desc = "The Rotated Hyper-Ellipsoid function is continuous, convex and unimodal. It is an " \
                          "extension of the Axis Parallel Hyper-Ellipsoid function, also referred to as the Sum " \
                          "Squares function. The plot shows its two-dimensional form. "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = np.sum([np.sum([x[j]**2 for j in range(0, i+1)], axis=0) for i in range(0, 2)], axis=0)
        # Return Cost
        return c
