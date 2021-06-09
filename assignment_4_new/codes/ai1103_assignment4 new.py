import matplotlib.pyplot as plt
import math

num_trial=100
input_values=[]
i=0
while i<num_trial:
  input_values.append(i)
  i+=1

output_values=[]
j=0
while j<num_trial:
  temp=0
  temp=temp+math.exp(-j)*(1-math.exp(-1))
  output_values.append(temp)
  j+=1


#plotting graph
fig=plt.figure(figsize=(10,5))
plt.plot(input_values,output_values)
plt.title('Probability distribution')
plt.xlabel('K')
plt.ylabel('P(Y=K)')

fig.savefig("Figure_1.png")
plt.show()
