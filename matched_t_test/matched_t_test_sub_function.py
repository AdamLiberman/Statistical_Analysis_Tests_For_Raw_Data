import numpy as np
import scipy.stats as stats
from z_test.z_test_sub_function import z_one_tail

t_tail_dict = {
    "two-sided": "The sample mean is different than the population mean",
    "less": "The sample mean is smaller than the  population mean",
    "greater": "The sample mean is greater than the population mean"
}

def matched_t_get_input():
    try:
        print (t_tail_dict)
        tail_list = dict(enumerate(t_tail_dict.keys(), start=1))    
        test_number = int(input(f"Choose a test type by its index: {tail_list}"))
    except TypeError:
        print("Please enter a number")
        exit()
    return tail_list[test_number]

def matched_t_computation(df, t_tail, alpha):
    test_result = stats.ttest_rel(a=df[0], b=df[1], alternative=t_tail)
    t_statistic = test_result.statistic
    p_value = test_result.pvalue
    sam1_mean = np.mean(df[0])
    sam2_mean = np.mean(df[1])
    confid_level = 1-alpha
    ci = test_result.confidence_interval(confidence_level=confid_level)
    return t_statistic,p_value, sam1_mean, sam2_mean, ci

def matched_t_output(alpha, t_statistic, p_value, sam1_mean, sam2_mean, ci):
    print(f"Group 1 mean: {sam1_mean}")
    print(f"Group 2 mean: {sam2_mean}")
    print(f"t-statistic: {t_statistic}")
    print(f"p-value: {p_value}")
    print(f"Confidence interval: {ci}")
    z_one_tail(alpha, p_value)






