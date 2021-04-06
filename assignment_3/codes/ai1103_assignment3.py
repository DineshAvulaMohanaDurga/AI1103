import numpy as np
import matplotlib.pyplot as plt
import random as rand
num_trial=500
def fact(k):
    f=i=1
    while i<=k:
        f*=i
        i+=1
    return f

def comb(x,y):
    num=fact(x)
    num2=fact(x-y)*fact(y)
    comb=num/num2
    return comb

def term(r,p,n):
    term=comb(n,r)*pow(p,r)*pow(1-p,n-r)
    return term

probabilities=[1.0,0.1]
i=0
while i<num_trial:
    probabilities[i]=rand.random()
i=j=0
values=[0.0,0.0]
while i<num_trial:
    j=0
    while j<num_trial:
        values[i]=values[i]+term(i,probabilities[j],num_trial)
#plotting graph
probability=np.arange(probabilities)
plt.plot(probability,values)
plt.title('values vs Y')
plt.xlabel('Y')
plt.ylabel('value')

plt.savefig("figure1.png")
plt.show()
