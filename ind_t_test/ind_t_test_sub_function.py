import numpy as np
import scipy.stats as stats
from os_t_test.os_t_test_sub_function import t_tail_dict

def ind_t_get_input():
    try:
        print("Choose alternative hypothesis")
        print(t_tail_dict)
        tail_list = dict(enumerate(t_tail_dict.keys(), start=1))    
        tail_number = int(input(f"Choose a test type by its index: {tail_list}"))
        equal_variances = input("Should assume equal variances? y/n")
        if equal_variances == "y":
            equal_variances = True
        elif equal_variances == "n":
            equal_variances = False
        else:
            print("Please write only y/n ")
            exit()
    except ValueError:
        print("Please enter a number")
        exit()
    return tail_list[tail_number], equal_variances

def ind_t_computation(df, t_tail, alpha, equal_variances):
    test_result = stats.ttest_ind(a=df[0], b=df[1], equal_var=equal_variances, alternative=t_tail)
    t_statistic = test_result.statistic
    p_value = test_result.pvalue
    sam1_mean = np.mean(df[0])
    sam2_mean = np.mean(df[1])
    confid_level = 1-alpha
    ci = test_result.confidence_interval(confidence_level=confid_level)
    return t_statistic,p_value, sam1_mean, sam2_mean, ci
 
