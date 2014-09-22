from examples.functions2d.utils import function_example

minima = [Bohachevsky1,
          Bohachevsky2,
          Bohachevsky3,
          Perm,
          RotatedHyperEllipsoid,
          Sphere,
          SumOfDifferentPowers,
          SumSquares,
          Trid]

name = ["bohachevsky_1",
        "bohachevsky_2",
        "bohachevsky_3",
        "perm",
        "rotated_hyper_ellipsoid",
        "sphere",
        "sum_of_different_powers",
        "sum_squares",
        "trid"]

for Func, name in zip(minima, name):
    func = Func()
    function_example(func, name)