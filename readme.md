## Continuous Testing Functions for Optimisation

A module containing continuous testing functions for optimisation in one, two and multi-dimensional implementations. Intended for testing the performance of mathematical optimisation routines. Many are taken from http://www.sfu.ca/~ssurjano/optimization.html.

Each test function is implemented as a class with up to three methods for calculating the *cost*, *gradient* and *Hessian* information of the test functions. Additional information such as the global minimum value and position, the function's domain and cost function are also provided.


### Test Function Implementation

Each test function has up to three methods which calculate the *cost*, *gradient* and *Hessian* information. It also contains much other useful information. The implementation of the 2D Rosenbrock is shown below.

```python
class Rosenbrock(Function2D):
    """ Rosenbrock Function. """

    def __init__(self):
        """ Constructor. """
        # Information
        self.min = np.array([1.0, 1.0])
        self.value = 0.0
        self.domain = np.array([[-np.inf, np.inf], [-np.inf, np.inf]])
        self.n = 2
        self.smooth = True
        self.info = [True, True, True]
        # Description
        self.latex_name = "Rosenbrock Function"
        self.latex_type = "Valley Shaped"
        self.latex_cost = r"\[ f(\boldsymbol{x}) = \sum_{i=0}^{d-2} \left[ 100 \left(x_{i+1} 
                                - x_{i}^{2}\right)^{2} + \left(x_{i} - 1\right)^{2}\right] \]"
        self.latex_desc = "The Rosenbrock function, also referred to as the Valley or Banana function, is a popular " \
                          "test problem for gradient-based optimization algorithms. It is shown in the plot above in " \
                          "its two-dimensional form. The function is unimodal, and the global minimum lies in a " \
                          "narrow, parabolic valley. However, even though this valley is easy to find, convergence " \
                          "to the minimum is difficult."

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = 100.0*(x[1] - x[0]**2.0)**2.0 + (x[0] - 1.0)**2.0
        # Return Cost
        return c

    def grad(self, x):
        """ Grad function. """
        # Grad
        g = np.zeros(x.shape)
        # Calculate Grads
        g[0] = -400.0*x[0]*(x[1] - x[0]**2.0) + 2.0*(x[0] - 1.0)
        g[1] = 200.0*(x[1] - x[0]**2.0)
        # Return Grad
        return g

    def hess(self, x):
        """ Hess function. """
        # Hess
        h = np.zeros((2, 2) + x.shape[1:])
        # Calculate Hess
        h[0][0] = -400.0*x[1] + 1200.0*x[0]**2.0 + 2.0
        h[0][1] = -400.0*x[0]
        h[1][0] = h[0][1]
        h[1][1] = 200.0
        # Return Hess
        return h
```


### Code Demonstration

The following example shows how the module can be used.

```python
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> from ctf.functions2d import Beale
>>> func = Beale()
>>> func.latex_desc
The Beale function is multimodal, with sharp peaks at the corners of the input domain. 
>>> func.domain
[[-4.5  4.5]
 [-4.5  4.5]]
>>> func.cost(np.array([2.0, 0.0]))
0.703125
>>> func.grad(np.array([2.0, 0.0]))
[-0.75 -2.  ]
>>> func.hess(np.array([2.0, 0.0]))
[[  6.  -5.]
 [ -5.  10.]]
>>> func.plot_cost()
>>> plt.show()
```

![Beale Function](/examples/functions2d/images/beale.png)


### Requirements and Dependencies

Requires Python 3 and depends on Numpy and MatPlotLib.


## Included Test Functions

### 1D Test Functions

**Many Local Minima**

  1. [Gramacy and Lee Function](/examples/functions1d/images/gramacy_lee.png)


**Bowl Shaped**

  1. [Quadratic](/examples/functions1d/images/quadratic.png)


**Steep**

  1. [Absolute](/examples/functions1d/images/absolute.png)


**Other**

  1. [Forrester Function](/examples/functions1d/images/forrester.png)


### 2D Test Functions

**Many Local Minima**

  1. [Ackley Function](/examples/functions2d/images/ackley.png)
  1. [Bukin Function No. 6](/examples/functions2d/images/bukin_6.png)
  1. [Cross-in-Tray Function](/examples/functions2d/images/cross_in_tray.png)
  1. [Drop-Wave Function](/examples/functions2d/images/drop_wave.png)
  1. [Eggholder Function](/examples/functions2d/images/eggholder.png)
  1. [Griewank Function](/examples/functions2d/images/griewank.png)
  1. [Holder Table Function](/examples/functions2d/images/holder_table.png)
  1. [Levy Function No. 13](/examples/functions2d/images/levy_13.png)
  1. [Rastrigin Function](/examples/functions2d/images/rastrigin.png)
  1. [Schaffer Function No. 2](/examples/functions2d/images/schaffer_2.png)
  1. [Schaffer Function No. 4](/examples/functions2d/images/schaffer_4.png)
  1. [Schwefel Function](/examples/functions2d/images/schwefel.png)
  1. [Shubert Function](/examples/functions2d/images/shubert.png)


**Bowl Shaped**

  1. [Bohachevsky No. 1 Function](/examples/functions2d/images/bohachevsky_1.png)
  1. [Bohachevsky No. 2 Function](/examples/functions2d/images/bohachevsky_2.png)
  1. [Bohachevsky No. 3 Function](/examples/functions2d/images/bohachevsky_3.png)
  1. [Perm Function](/examples/functions2d/images/perm.png)
  1. [Rotated Hyper-Ellipsoid Function](/examples/functions2d/images/rotated_hyper_ellipsoid.png)
  1. [Sphere Function](/examples/functions2d/images/sphere.png)
  1. [Sum of Different Powers Function](/examples/functions2d/images/sum_of_different_powers.png)
  1. [Sum Squares Function](/examples/functions2d/images/sum_squares.png)
  1. [Trid Function](/examples/functions2d/images/trid.png)


**Plate-Shaped**

  1. [Booth Function](/examples/functions2d/images/booth.png)
  1. [Matyas Function](/examples/functions2d/images/matyas.png)
  1. [McCormick Function](/examples/functions2d/images/mccormick.png)
  1. [Power Sum Function](/examples/functions2d/images/power_sum.png)
  1. [Zakharov Function](/examples/functions2d/images/zakharov.png)


**Valley-Shaped**

  1. [Three-Hump Camel Function](/examples/functions2d/images/three_hump_camel.png)
  1. [Six-Hump Camel Function](/examples/functions2d/images/six_hump_camel.png)
  1. [Dixon-Price Function](/examples/functions2d/images/dixon_price.png)
  1. [Rosenbrock Function](/examples/functions2d/images/rosenbrock.png)


**Steep Ridges/Drops**

  1. [Absolute](/examples/functions2d/images/absolute.png)
  1. [Absolute Skewed](/examples/functions2d/images/absolute_skewed.png)
  1. [De Jong Function No. 5](/examples/functions2d/images/de_jong_5.png)
  1. [Easom Function](/examples/functions2d/images/easom.png)
  1. [Michalewicz Function](/examples/functions2d/images/michalewicz.png)


**Other**

  1. [Beale Function](/examples/functions2d/images/beale.png)
  1. [Branin Function](/examples/functions2d/images/branin.png)
  1. [Goldstein-Price Function](/examples/functions2d/images/goldstein_price.png)
  1. [Styblinski-Tang Function](/examples/functions2d/images/styblinski_tang.png)


### ND Test Functions

**Many Local Minima**

  1. Ackley Function
  1. Griewank Function
  1. Rastrigin Function
  1. Schwefel Function


**Bowl Shaped**

  1. Perm Function
  1. Rotated Hyper-Ellipsoid Function
  1. Sphere Function
  1. Sum of Different Powers Function
  1. Sum Squares Function
  1. Trid Function


**Plate-Shaped**

  1. Power Sum Function
  1. Zakharov Function


**Valley-Shaped**

  1. Dixon-Price Function
  1. Rosenbrock Function


**Steep Ridges/Drops**

  1. Michalewicz Function


**Other**

  1. Styblinski-Tang Function


