from examples.functions2d.utils import function_example
from ctf.functions2d import *

minima = [ThreeHumpCamel,
          SixHumpCamel,
          DixonPrice,
          Rosenbrock]

name = ["three_hump_camel",
        "six_hump_camel",
        "dixon_price",
        "rosenbrock"]

for Func, name in zip(minima, name):
    func = Func()
    function_example(func, name)