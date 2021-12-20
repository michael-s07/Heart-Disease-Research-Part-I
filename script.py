# import libraries
#import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test
# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

chol_hd = yes_hd.chol

print(np.mean(chol_hd))


tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)

chol_no_hd = no_hd.chol

print(np.mean(chol_no_hd))

tstat, pval = ttest_1samp(chol_no_hd, 240)
print(pval/2)

num_patients = len(heart)
print(num_patients)

num_highfbs_patients = np.sum(heart.fbs)
print(num_highfbs_patients)

print(0.08*num_patients)

pval = binom_test(num_highfbs_patients, num_patients, .08, alternative='greater')
print(pval)