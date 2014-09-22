from examples.functions2d.utils import function_example
from ctf.functions2d import *

minima = [Booth,
          Matyas,
          McCormick,
          PowerSum,
          Zakharov]

name = ["booth",
        "matyas",
        "mccormick",
        "power_sum",
        "zakharov"]

for Func, name in zip(minima, name):
    func = Func()
    function_example(func, name)