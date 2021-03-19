from scipy.stats import binom
import numpy as np
#simlen=number of stimulation trials
simlen=5000000
#probability of item to be defective
p=5/100
k=1
n=10
prob_theor=binom.cdf(k,n,p)
data_binom=binom.rvs(n,p,size=simlen)
#stimulating the event of selecting 10 items with less than 1 defective item
err_ind=np.nonzero(data_binom<=k)
err_n =np.size(err_ind)
print("The following results are obtained by stimulation")
print("The probability that the sample contains atmost one defective item is",err_n/simlen,"\n")
print("The following value is obtained manually")
print("The probability that the sample contains atmost one defective item is",prob_theor)
print("as you can see the both values are close")
