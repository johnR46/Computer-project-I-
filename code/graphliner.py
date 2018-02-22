import matplotlib.pyplot as plt
import time
import math
import numpy as np


import numpy as np
def graph(formula,x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x,y)
    plt.xlabel('cout post')
    plt.ylabel('distance of post')
    plt.show()

