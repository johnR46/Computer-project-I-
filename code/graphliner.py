import matplotlib.pyplot as plt
import time
import math
import numpy as np
start_time = time.time()


import numpy as np
def graph(formula,x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x,y)
    plt.xlabel('cout post')
    plt.ylabel('distance of post')
    
    for y in y :
        convert_y_to_x(y)
        print(",")
        print(y)
   
    plt.show()
    #print(x,y)



# convert ycenter to xpost
def convert_y_to_x(a):
    b = math.sqrt(-0.0056 * a + 6.768465)
    ans_xpost = (1.8517 - b)/0.0028
    print(ans_xpost)
    return ans_xpost

#convert ycenter(t)     
def calculator_y_time(formula,x):
    ans_ydiscount = eval(formula)
    print(ans_ydiscount)
    start_time = time.time()
    return ans_ydiscount


def speeds():
       
    times = time.time()
  
    discount_y_1 = calculator_y_time('x**-0.0014 + 1.8517*x + 596.37',times - start_time) #timestart
    xpost_1 = convert_y_to_x(discount_y_1)


    
    discount_y_2 = calculator_y_time('x**-0.0014 + 1.8517*x + 596.37',time.time() - start_time) #timenow
    xpost_2 = convert_y_to_x(discount_y_2)
    
    V = (xpost_2 - xpost_1) / (time.time() - times)
    
    print(V)
    return V
    
