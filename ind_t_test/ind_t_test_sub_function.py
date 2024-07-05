import numpy as np
import scipy.stats as stats
from matched_t_test.matched_t_test_sub_function import matched_t_output

t_tail_dict = {
    "two-sided": "The sample mean is different than the population mean",
    "less": "The sample mean is smaller than the  population mean",
    "greater": "The sample mean is greater than the population mean"
}

def ind_t_get_input():
    try:
        print(t_tail_dict)
        tail_list = dict(enumerate(t_tail_dict.keys(), start=1))    
        test_number = int(input(f"Choose a test type by its index: {tail_list}"))
        equal_variances = input("Should assume equal variances? y/n")
        if equal_variances == "y":
            equal_variances = True
        elif equal_variances == "n":
            equal_variances = False
        else:
            print("Please write only y/n")
            exit()
    except TypeError:
        print("Please enter a number")
        exit()
    return tail_list[test_number], equal_variances

def ind_t_computation(df, t_tail, alpha, equal_variances):
    test_result = stats.ttest_ind(a=df[0], b=df[1], equal_var=equal_variances, alternative=t_tail)
    t_statistic = test_result.statistic
    p_value = test_result.pvalue
    sam1_mean = np.mean(df[0])
    sam2_mean = np.mean(df[1])
    confid_level = 1-alpha
    ci = test_result.confidence_interval(confidence_level=confid_level)
    return t_statistic,p_value, sam1_mean, sam2_mean, ci
 
def ind_t_test_main(df, alpha):
    if df.size[1] != 2:
        print("The file's dimensions don't match the selected test")
        exit()
    else:
        t_tail, equal_variances = ind_t_get_input()
        t_statistic,p_value, sam1_mean, sam2_mean, ci = ind_t_computation(df, t_tail, alpha, equal_variances)
        matched_t_output(alpha, t_statistic, p_value, sam1_mean, sam2_mean, ci)
