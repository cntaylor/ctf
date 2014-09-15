# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class Ackley(Function2D):
    """ Ackley's Function. """

    def __init__(self):
        """ Constructor. """
        # Meta Information
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-5.0, 5.0], [-5.0, 5.0]])
        self.smooth = True
        self.info = [True, True, True]
        self.latex_name = "Ackley's Function"
        self.latex_type = "Many Local Minima"
        self.latex_cost = r'$\displaystyle f(x, y)  = -20\exp\left(-0.2\sqrt{0.5\left(x^{2}+y^{2}\right)}\right) -\exp\left(0.5\left(\cos\left(2\pi x\right)+\cos\left(2\pi y\right)\right)\right) + 20 + e $'
        self.latex_desc = "It is characterized by a nearly flat outer region, and a large hole at the centre. The " \
                          "function poses a risk for optimization algorithms, particularly hillclimbing algorithms, " \
                          "to be trapped in one of its many local minima. "

    def cost(self, x):
        """ Cost function. """
        # Calculate Cost
        cost = -20.0*exp(-0.2*sqrt(0.5*(x[0]**2 + x[1]**2))) - exp(0.5*(cos(2.0*pi*x[0]) + cos(2.0*pi*x[1]))) + 20.0 + exp(1.0)
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Calculate Grads
        dx = 2.0*x[0]*exp(-0.2*sqrt(0.5*x[0]**2 + 0.5*x[1]**2))/sqrt(0.5*x[0]**2 + 0.5*x[1]**2) + 1.0*pi*exp(0.5*cos(2.0*pi*x[0]) + 0.5*cos(2.0*pi*x[1]))*sin(2.0*pi*x[0])
        dy = 2.0*x[1]*exp(-0.2*sqrt(0.5*x[0]**2 + 0.5*x[1]**2))/sqrt(0.5*x[0]**2 + 0.5*x[1]**2) + 1.0*pi*exp(0.5*cos(2.0*pi*x[0]) + 0.5*cos(2.0*pi*x[1]))*sin(2.0*pi*x[1])
        # Return Grad
        return np.array([dx, dy])

    def hess(self, x):
        """ Hess function. """
        # Hess
        hess = np.zeros((2, 2))
        # Hesses
        hess[0][0] = -0.2*x[0]**2*exp(-0.2*sqrt(0.5*x[0]**2 + 0.5*x[1]**2))/(0.5*x[0]**2 + 0.5*x[1]**2) - 1.0*x[0]**2*exp(-0.2*sqrt(0.5*x[0]**2 + 0.5*x[1]**2))/(0.5*x[0]**2 + 0.5*x[1]**2)**(3/2) - 1.0*np.pi**2*exp(0.5*cos(2.0*np.pi*x[0]) + 0.5*cos(2.0*np.pi*x[1]))*sin(2.0*np.pi*x[0])**2 + 2.0*np.pi**2*exp(0.5*cos(2.0*np.pi*x[0]) + 0.5*cos(2.0*np.pi*x[1]))*cos(2.0*np.pi*x[0]) + 2.0*exp(-0.2*sqrt(0.5*x[0]**2 + 0.5*x[1]**2))/sqrt(0.5*x[0]**2 + 0.5*x[1]**2)
        hess[0][1] = -0.2*x[0]*x[1]*exp(-0.2*sqrt(0.5*x[0]**2 + 0.5*x[1]**2))/(0.5*x[0]**2 + 0.5*x[1]**2) - 1.0*x[0]*x[1]*exp(-0.2*sqrt(0.5*x[0]**2 + 0.5*x[1]**2))/(0.5*x[0]**2 + 0.5*x[1]**2)**(3/2) - 1.0*np.pi**2*exp(0.5*cos(2.0*np.pi*x[0]) + 0.5*cos(2.0*np.pi*x[1]))*sin(2.0*np.pi*x[0])*sin(2.0*np.pi*x[1])
        hess[0][1] = hess[1][0]
        hess[1][1] = -0.2*x[1]**2*exp(-0.2*sqrt(0.5*x[0]**2 + 0.5*x[1]**2))/(0.5*x[0]**2 + 0.5*x[1]**2) - 1.0*x[1]**2*exp(-0.2*sqrt(0.5*x[0]**2 + 0.5*x[1]**2))/(0.5*x[0]**2 + 0.5*x[1]**2)**(3/2) - 1.0*np.pi**2*exp(0.5*cos(2.0*np.pi*x[0]) + 0.5*cos(2.0*np.pi*x[1]))*sin(2.0*np.pi*x[1])**2 + 2.0*np.pi**2*exp(0.5*cos(2.0*np.pi*x[0]) + 0.5*cos(2.0*np.pi*x[1]))*cos(2.0*np.pi*x[1]) + 2.0*exp(-0.2*sqrt(0.5*x[0]**2 + 0.5*x[1]**2))/sqrt(0.5*x[0]**2 + 0.5*x[1]**2)
        # Return Hess
        return hess