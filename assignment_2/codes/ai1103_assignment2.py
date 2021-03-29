import random as rand
import numpy as np
import math
#number of stimulation trials
simlen=2000000
x=y=z=1.0
i=num=0
mean=1/6
variance=1/18
trials=mean+math.sqrt(variance)*np.random.randn(3,simlen)
for i in range(simlen):
    x=trials[0,i-1]
    y=trials[1,i-1]
    z=trials[2,i-1]
    if(x<y<z):
        num+=1
print("The probability is :",num/simlen)
