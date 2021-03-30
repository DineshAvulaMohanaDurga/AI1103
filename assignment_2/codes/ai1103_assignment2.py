import numpy as np
import math
import matplotlib.pyplot as plt 
#number of stimulation trials
simlen=2000000
x=y=z=1.0
i=num=0
mean=1/6
variance=1/18

repeatitions=4
stimulation=[1,1,1,1]
for j in range(repeatitions):
  num=0
  trials=mean+math.sqrt(variance)*np.random.randn(3,simlen)
  for i in range(simlen):
    x=trials[0,i-1]
    y=trials[1,i-1]
    z=trials[2,i-1]
    if(x<y<z):
        num+=1
  stimulation[j-1]=num/simlen
print("The probability is :",num/simlen)
#plotting the graph

data=(1,10,21)
theoritical=(1/6,1/6,1/6,1/6)
no_groups=4
fig,ax=plt.subplots()
index=np.arange(no_groups)
bar_width=0.35
opacity=0.8
trial=('trial 1','trial 2','trial 3','trial 4')
rects1=plt.bar(index,stimulation,bar_width,alpha=opacity,color='b',label='stimulation value')
rects2=plt.bar(index+bar_width,theoritical,bar_width,alpha=opacity,color='g',label='theoritical value')
plt.xlabel('trial number')
plt.title('stimulation vs theoritical')
plt.ylabel('probability density')
plt.xticks(index+bar_width,trial)
plt.legend()

plt.tight_layout()
plt.savefig("figure1.png")
plt.show()
