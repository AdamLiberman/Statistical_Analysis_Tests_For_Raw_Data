import pandas as pd
from scipy.stats import pearsonr

def r_correlation_main(df, alpha):

    r, p-value = pearsonr(df[0], df[1],alternative=test)
    print('Pearsons correlation: %.3f' % corr)