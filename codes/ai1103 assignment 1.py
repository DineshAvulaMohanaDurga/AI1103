import random as rand

num=200000
defective=non_defective=i=j=num_non_defective=0
for i in range(num):
    defective=non_defective=j=0
    while j<10:
        temp=rand.randint(1,100)
        if(temp<=5):
            defective+=1
        else:
            non_defective+=1
        j+=1
    if(defective<=1):
        num_non_defective+=1
    i+=1
probability=num_non_defective/num
print("The following value is obtained by stimulation")
print("The probability that the sample contains atmost one defective item is",probability,"\n")
print("The following value is obtained manually")
print("The probability that the sample contains atmost one defective item is 0.913862")
print("as you can see the both values are close")
