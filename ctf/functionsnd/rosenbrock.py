# Imports
import numpy as np

from ctf.functions2d.function2d import Function2D



# Problem
class Rosenbrock(Function2D):
    """ Rosenbrock Function. """

    def __init__(self, n):
        """ Constructor. """
        # Information
        self.min = np.array([1.0 for i in range(0, n)])
        self.value = 0.0
        self.domain = np.array([[-np.inf, np.inf] for i in range(0, n)])
        self.n = n
        self.smooth = True
        self.info = [True, True, True]
        # Description
        self.latex_name = "Rosenbrock Function"
        self.latex_type = "Valley Shaped"
        self.latex_cost = r"\[ f(\boldsymbol{x}) = \sum_{i=0}^{d-2} \left[ 100 \left(x_{i+1} - x_{i}^{2}\right)^{2} + \left(x_{i} - 1\right)^{2}\right] \]"
        self.latex_desc = "The Rosenbrock function, also referred to as the Valley or Banana function, is a popular " \
                          "test problem for gradient-based optimization algorithms. It is shown in the plot above in " \
                          "its two-dimensional form. The function is unimodal for (n<4), and the global minimum lies in a " \
                          "narrow, parabolic valley. However, even though this valley is easy to find, convergence " \
                          "to the minimum is difficult."

    def cost(self, x):
        """ Cost function. """
        # Calculate Cost
        c = np.sum([100*(x[i+1] - x[i]**2)**2 + (x[i] - 1)**2 for i in range(0, self.n-1)])
        # Return Cost
        return c

    #math for grad and hess function found on:
    #https://docs.scipy.org/doc/scipy-0.14.0/reference/tutorial/optimize.html#unconstrained-minimization-of-multivariate-scalar-functions-minimize

    def grad(self, x):
        g = np.zeros(x.shape)
        n = self.n
        g[0] = -400*x[0]*(x[1] - x[0]**2.0) + 2.0*(x[0]-1.)
        for i in range(1,n-1):
            g[i] = -400*x[i]*(x[i+1] - x[i]**2.0) + 2.0*(x[i]-1.) + 200.0*(x[i] - x[i-1]**2.0)
        g[n-1] = 200*(x[n-1] - x[n-2]**2.0)
        return g

    def hess(self, x):
        n = self.n
        h=np.zeros((n,n))
        h[0,0] = 2.0 + 1200.0 * x[0]**2.0 - 400*x[1]
        h[0,1] = -400 * x[0]
        h[1,0] = -400 * x[0]
        for i in range(1,n-1):
            h[i,i] = 202.0 + 1200.0 * x[i]**2. - 400*x[i+1]
            h[i,i+1] = -400*x[i]
            h[i+1,i] = h[i,i+1]
        h[n-1,n-1] = 200.0
        return h