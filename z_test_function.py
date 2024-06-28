import pandas as pd
import numpy as np
import scipy.stats as stats

def z_test_main(df, alpha):
    if df.size[1] != 1:
        print("The file's dimensions don't match the selected test")
    else:
        test_type = input("what kind of test would you like to preform? one-tail/two-tail")
        pop_mean = input("What is the population's mean? ")
        pop_std = input("What is the population's std? ")
        sam_mean = np.mean(df.iloc[1])
        z_score = (((sam_mean-pop_mean)*np.sqrt(len(df)))/pop_std)
        print('Z-Score :',z_score) 
        if test_type == "two-tail":
            if pop_mean > sam_mean:
                p_value = stats.norm.cdf(z_score)
            if pop_mean < sam_mean:
                p_value = 1-stats.norm.cdf(z_score)
            print('p-value :',p_value)
            if p_value <  alpha/2:
                print("Reject Null Hypothesis")
            else:
                print("Fail to Reject Null Hypothesis")
        if test_type == "one-tail":
            h_1 = input("Do you hypothesize that your mean is bigger of smaller than the population's mean? bigger/smaller")
            if h_1 == "bigger":
                p_value = 1-stats.norm.cdf(z_score)
            if h_1 == "smaller":
                p_value = stats.norm.cdf(z_score)
            print('p-value :',p_value)
            if p_value <  alpha:
                print("Reject Null Hypothesis")
            else:
                print("Fail to Reject Null Hypothesis")
        else:
            print("Please choosa a tail test")
        