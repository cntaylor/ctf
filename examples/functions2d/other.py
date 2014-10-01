from examples.functions2d.utils import function_example
from ctf.functions2d import *

minima = [Beale,
          Branin,
          GoldsteinPrice,
          StyblinskiTang]

name = ["beale",
        "branin",
        "goldstein_price",
        "styblinski_tang"]

for Func, name in zip(minima, name):
    func = Func()
    function_example(func, name)