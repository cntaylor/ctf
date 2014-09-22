from examples.functions2d.utils import function_example
from ctf.functions1d import *

minima = [GramacyLee]

name = ["gramacy_lee"]

for Func, name in zip(minima, name):
    func = Func()
    function_example(func, name)