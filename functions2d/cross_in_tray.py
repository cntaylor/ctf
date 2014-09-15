# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class CrossInTray(Function2D):
    """ Cross in Tray Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([[1.34941, 1.34941],
                             [1.34941, -1.34941],
                             [-1.34941, 1.34941],
                             [-1.34941, -1.34941]])
        self.value = np.array([-2.06261, -2.06261, -2.06261, -2.06261])
        self.domain = np.array([[-10.0, 10.0], [-10.0, 10.0]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Ackley's Function"
        self.latex_type = "Many Local Minima"
        self.latex_cost = r'\[ f(x, y) = -0.0001 \left( \left| \sin \left(x\right) \sin \left(y\right) \exp \left( \left|100 - \frac{\sqrt{x^{2} + y^{2}}}{\pi} \right|\right)\right| + 1 \right)^{0.1} \]'
        self.latex_desc = "The Cross-in-Tray function has multiple global minima."

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = np.zeros(1)
        # Calculate Cost
        cost[0] = -0.0001*(np.abs(np.sin(x[0])*np.sin(x[1])*np.exp(np.abs(100 - np.sqrt(x[0]**2 + x[1]**2)/np.pi))) + 1)**0.1
        # Return Cost
        return cost
