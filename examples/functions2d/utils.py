""" Utility functions for producing examples. """


# Imports
import matplotlib.pyplot as plt


# Functions
def function_example(func, name):
    # Function Name
    print(func.latex_name)
    # Function Landscape
    func.plot_cost()
    # Save Figure
    plt.savefig(r'images/' + name + r'.png')
    # Show Figure
    plt.show()