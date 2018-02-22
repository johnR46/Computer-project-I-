import matplotlib.pyplot as plt
import time
import math
import numpy as np
start_time = time.time()

import numpy as np
def speeds(formula,x_range,xcenter,ycenter):
   
    x  =  xcenter*xcenter + ycenter*ycenter
    c = np.int(math.sqrt(x))
    x = np.array(x_range)  
    y = eval(formula)
    v =  (y-c/(time.time() - start_time ))
    
    print(v[1])
    print(y)
 
