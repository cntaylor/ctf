""" Utility functions for producing examples. """


# Imports
import matplotlib.pyplot as plt


# Functions
def function_example(func):
    # Function Name
    print(func.latex_name)
    # Function Landscape
    func.plot_cost()
    plt.show()