from scipy.stats import binom
import numpy as np
k=1
n=10
p=5/100
prob_stim = binom.cdf(k,n,p)
print("The probability that the sample contains less than one defective is",prob_stim)
