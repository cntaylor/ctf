# Imports
import numpy as np

from ctf.functions2d.function2d import Function2D



# Problem
class Zakharov(Function2D):
    """ Zakharov Function. """

    def __init__(self, n):
        """ Constructor. """
        # Information
        self.min = np.array([0.0 for i in range(0, n)])
        self.value = 0.0
        self.domain = np.array([[-5, 10.0] for i in range(0, n)])
        self.n = n
        self.smooth = True
        self.info = [True, True, True]
        # Description
        self.latex_name = "Zakharov Function"
        self.latex_type = "Plate-Shaped"
        self.latex_cost = r"\[ f(\mathbf{x}) = \sum_{i=0}^{d-1} x_i^2 + \left ( \sum_{i=0}^{d-1} 0.5 (i+1) x_i \right )^2 + \left ( \sum_{i=0}^{d-1} 0.5 (i+1) x_i \right )^4  \]"
        self.latex_desc = "Single global minimum plate-like function."

    def cost(self, x):
        """ Cost function. """
        # Calculate Cost
        c = np.sum([x[i]**2 for i in range(self.n)], axis=0) + \
            np.sum([0.5*(i+1)*x[i] for i in range(self.n)], axis=0)**2 + \
            np.sum([0.5*(i+1)*x[i] for i in range(self.n)], axis=0)**4
        # Return Cost
        return c

    def grad(self,x):
        g = np.zeros(x.shape)
        n = self.n
        internal_sum = 0
        for k in range(n):
            internal_sum += (k+1)*x[k]
        internal_sum *= 0.5
        for i in range(n):
            g[i] = 2*x[i] +  internal_sum*(i+1) + \
                2 * internal_sum**3 * (i+1)
        return g

    def hess(self,x):
        n = self.n
        h = np.zeros((n,n))
        internal_sum = 0
        for k in range(n):
            internal_sum += (k+1)*x[k]
        internal_sum *= 0.5
        for i in range(n):
            for j in range(n):
                if i==j:
                    h[i,i] = 2 + 0.5*(i+1)**2 + \
                        3 * (i+1)**2 * internal_sum**2
                else:
                    h[i,j] = (i+1)*(j+1)*0.5 + \
                        3 * (i+1) * (j+1) * internal_sum**2
        return h