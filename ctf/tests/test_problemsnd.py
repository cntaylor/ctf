# Imports
import numpy as np
import test_funcs
from ctf.functionsnd import *

#Note that many ND functions don't have grad or hess, so not included...

#I have arbitrarily put in 5 dimensional objects as test.  I think it needs to be
#bigger than 2 to really test, but otherwise, fairly arbitrary.  That said, as the
#dimensionality increases, the numerical testing routines seem to fail sometimes
#when I don't think they should, so...  maybe 5 is just a good number

# Test Functions
class TestRosenbrock():

    def setup(self):
        self.f = Rosenbrock(5)

    def teardown(self):
        pass

    def test_cost(self):
        """ Test if the cost at the minimum is what is expected. """
        assert check_cost(self.f)

    def test_grad(self):
        """ Test if the gradient at the minimum is sufficiently close to zero. """
        assert check_grad(self.f) and check_grad_numerically(self.f)

    def test_hess(self):
        """ Test if the gradient at the minimum is sufficiently positive semi-definite. """
        assert check_hess(self.f) and check_hess_numerically(self.f)


class TestZakharov():

    def setup(self):
        self.f = Zakharov(5)

    def teardown(self):
        pass

    def test_cost(self):
        """ Test if the cost at the minimum is what is expected. """
        assert check_cost(self.f)

    def test_grad(self):
        """ Test if the gradient at the minimum is sufficiently close to zero. """
        assert check_grad(self.f) and check_grad_numerically(self.f)

    def test_hess(self):
        """ Test if the gradient at the minimum is sufficiently positive semi-definite. """
        assert check_hess(self.f) and check_hess_numerically(self.f)


class TestTrid():

    def setup(self):
        self.f = Trid(5)

    def teardown(self):
        pass

    def test_cost(self):
        """ Test if the cost at the minimum is what is expected. """
        assert check_cost(self.f)

    def test_grad(self):
        """ Test if the gradient at the minimum is sufficiently close to zero. """
        assert check_grad(self.f) and check_grad_numerically(self.f)

    def test_hess(self):
        """ Test if the gradient at the minimum is sufficiently positive semi-definite. """
        assert check_hess(self.f) and check_hess_numerically(self.f)


class TestPerm():

    def setup(self):
        self.f = Perm(5)

    def teardown(self):
        pass

    def test_cost(self):
        """ Test if the cost at the minimum is what is expected. """
        assert check_cost(self.f)

    def test_grad(self):
        """ Test if the gradient at the minimum is sufficiently close to zero. """
        assert check_grad(self.f) and check_grad_numerically(self.f)

    def test_hess(self):
        """ Test if the gradient at the minimum is sufficiently positive semi-definite. """
        assert check_hess(self.f) and check_hess_numerically(self.f)


