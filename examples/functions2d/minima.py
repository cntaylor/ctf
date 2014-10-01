from examples.functions2d.utils import function_example
from ctf.functions2d import *

minima = [Ackley,
          Bukin6,
          CrossInTray,
          DropWave,
          Eggholder,
          Griewank,
          HolderTable,
          Levy13,
          Rastrigin,
          Schaffer2,
          Schaffer4,
          Schwefel,
          Shubert]

name = ["ackley",
        "bukin_6",
        "cross_in_tray",
        "drop_wave",
        "eggholder",
        "griewank",
        "holderTable",
        "levy_13",
        "rastrigin",
        "schaffer_2",
        "schaffer_4",
        "schwefel",
        "shubert"]

for Func, name in zip(minima, name):
    func = Func()
    function_example(func, name)