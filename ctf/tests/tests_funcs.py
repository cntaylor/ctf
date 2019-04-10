import numpy as np

tol = 1E-4
step_size = .0001
#The numerical checking stuff is really sensitive as you can have large
#derivatives, and the changes are several digits down, but still close to
#tol because the derivative was so large.

# Support Functions
def check_cost(f):
    """ Checks cost is within tolerances. """
    return (f.cost(f.min) - f.value) < tol


def check_grad(f):
    """ Checks cost is within tolerances. """
    return np.linalg.norm(f.grad(f.min)) < tol


def check_hess(f):
    """ Checks Hessian is positive semi-definite. """
    #try:
    #    np.linalg.cholesky(f.hess(f.min))
    #except:
    #    return False
    #else:
    #    return True
    return np.all(np.linalg.eigvals(f.hess(f.min)) >= 0.0)
    #return True

def find_random_point(f):
    n = f.n
    #First, I need to find a random point that is in the domain
    xc  = np.random.randn(n,1) + f.min.reshape(n,1)
    for i in range(n): #Check that each value is in the domain
        while not (f.domain[i,0] < xc[i] < f.domain[i,1]):
            xc[i] = np.random.randn + f.min.reshape[i]
    return xc

def check_grad_numerically(f):
    n = f.n
    xc = find_random_point(f)
    #Now compute a numerical derivative and compare it with what is computed
    gc = f.grad(xc)
    fc = f.cost(xc)
    for i in range(n): #Derivative in each direction
        xd = xc.copy()
        xd[i] += step_size
        fd = f.cost(xd)
        if abs(gc[i]*step_size - (fd-fc)) > tol:
            return False #Bad gradient
    return True

def check_hess_numerically(f):
    n = f.n
    xc = find_random_point(f)
    #While moving in each direction, find the derivative in that direction,
    #compare against Hessian predicted change
    gc = f.grad(xc)
    hc = f.hess(xc)

    for i in range(n): #Derivative in each direction
        xd = xc.copy()
        xd[i] += step_size
        gd = f.grad(xd)
        if not np.all((hc[i,:].reshape(n,1)*step_size - (gd-gc)) < tol):
            return False #Bad hessian (assuming gradients are good ... :)
    return True


