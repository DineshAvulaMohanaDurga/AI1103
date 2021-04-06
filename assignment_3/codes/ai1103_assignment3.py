import matplotlib.pyplot as plt
import random as rand
num_trial=800
def fact(k):
    f=i=1
    while i<=k:
        f=f*i
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

probabilities=[]
i=0
lists=[]
while i<num_trial:
  temp=rand.uniform((i+num_trial)/(num_trial*2+1),(i+1+num_trial)/(num_trial*2+1))
  probabilities.append(temp)
  lists.append(i)
  i+=1
j=0
i=0
probabilities.sort()
values=[]
while i<num_trial:
    j=temp=0
    while j<num_trial:
        temp=temp+term(i,probabilities[j],num_trial)
        j+=1
    i+=1
    values.append(temp)

#plotting graph
fig=plt.figure(figsize=(10,5))
plt.plot(lists,values)
plt.title('values vs Y')
plt.xlabel('Y')
plt.ylabel('value')

fig.savefig("figure1.png")
plt.show()
