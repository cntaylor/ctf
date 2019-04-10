# Imports
import numpy as np

from ctf.functions2d.function2d import Function2D



# Problem
class Trid(Function2D):
    """ Trid Function. """

    def __init__(self, n):
        """ Constructor. """
        # Information
        #Create the min for a n-dimensional object...
        min_list = [n]
        tmp = n-2
        while tmp > 0:
            min_list.append(tmp+min_list[-1])
            tmp -=2
        if tmp < 0:
            min_list.extend(min_list[-2::-1])
        else:
            min_list.extend(min_list[::-1])
        self.min = np.array([float(val) for val in min_list]).reshape(n,1)
        #implementing a recursive formula to determine what the minimum value will be...
        xc = 2
        inc_c = 5
        inc_inc_c = 4
        for i in range(n-2):
            xc += inc_c
            inc_c += inc_inc_c
            inc_inc_c += 1
        self.value = -xc
        self.domain = np.array([[-np.inf, np.inf] for i in range(0, n)])
        self.n = n
        self.smooth = True
        self.info = [True, True, True]
        # Description
        self.latex_name = "Trid Function"
        self.latex_type = "Bowl-Shaped"
        self.latex_cost = "\[ f(\mathbf{x}) = \sum_{i=0}^{d-1} (x_i - 1)^2 - \sum_{i=1}^{d-1} x_i x_{i-1} \]"
        self.latex_desc = "The Trid function has no local minimum except the global one. It is shown here in its" \
                          "two-dimensional form. "

    def cost(self, x):
        """ Cost function. """
        # Calculate Cost
        c = np.sum([(x[i]-1)**2 for i in range(0, self.n)], axis=0) - np.sum([x[i]*x[i-1] for i in range(1, self.n)], axis=0)
        # Return Cost
        return c

    def grad(self, x):
        g = np.zeros(x.shape)
        n = self.n
        g[0] = 2.0 * (x[0]-1) - x[1]
        g[n-1] = 2.0 * (x[n-1]-1) - x[n-2]
        for i in range(1,n-1):
            g[i] = 2.0 * (x[i]-1) - x[i-1] - x[i+1]
        return g

    def hess(self, x):
        n = self.n
        h = np.zeros((n,n))
        h[0,0] = 2.0
        h[0,1] = -1.
        h[n-1,n-1] = 2.0
        h[n-1,n-2] = -1.
        for i in range(1,n-1):
            h[i,i]=2.
            h[i,i-1]=-1.
            h[i,i+1]=-1.
        return h