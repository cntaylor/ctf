from examples.functions2d.utils import function_example
from ctf.functions2d import *

minima = [DeJong5,
          Easom,
          Michalewicz]

name = ["de_jong_5",
        "easom",
        "michalewicz"]

for Func, name in zip(minima, name):
    func = Func()
    function_example(func, name)