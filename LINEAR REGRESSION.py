#LINEAR REGRESSION
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats

x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]
slope,intercept,r,p,std_err=stats.linregress(x,y)
def myfunc(x):
    return slope*x+intercept+std_err
mymodel=list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()

