import numpy as np
import matplotlib.pyplot as plt
def graph(formula,x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x,y)
    plt.xlabel('count post')
    plt.ylabel('distance of post')
    plt.show()
