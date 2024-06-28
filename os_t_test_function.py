import numpy as np
from scipy import stats

# Given student scores
def os_t_test_main(df, alpha):
    if df.size[1] != 1:
        print("The file's dimensions don't match the selected test")
    else:
        test_type = input("what kind of test would you like to preform? one-tail/two-tail")
        pop_mean = input("What is the population's mean? ")
        t_stat, p_value = stats.ttest_1samp(df, pop_mean)
        if test_type == "two-tail":
            print("p-value:", p_value)
            if p_value <  alpha:
                print("Reject Null Hypothesis")
            else:
                print("Fail to Reject Null Hypothesis")
        if test_type == "one-tail":
            print("p-value:", p_value/2)
            if p_value/2 <  alpha:
                print("Reject Null Hypothesis")
            else:
                print("Fail to Reject Null Hypothesis")
        else: 
            print("Please choose type of tail test")
        
       
  