import numpy as np
from scipy.stats import pearsonr
from z_test.z_test_sub_function import z_one_tail

r_tail_dict= {
    "two-sided": "the correlation is nonzero",
    "less": "the correlation is negative",
    "greater": "the correlation is positive"
}

def r_get_input():
    try:
        print("Choose alternative hypothesis")
        print(r_tail_dict)
        tail_list = dict(enumerate(r_tail_dict.keys(), start=1))    
        tail_number = int(input(f"Choose a test type by its index: {tail_list}"))
    except ValueError:
        print("Please choose a number")
        exit()
    return tail_list[tail_number]

def r_computation(df, test_type):
    r_result = pearsonr(df[0], df[1],alternative=test_type)
    r = r_result.statistic
    p_value = r_result.pvalue
    sam1_mean = np.mean(df[0])
    sam2_mean = np.mean(df[1])
    return r,p_value,sam1_mean,sam2_mean

def r_output(alpha, r, p_value, sam1_mean, sam2_mean):
    print(f"Group 1 mean: {sam1_mean}")
    print(f"Group 2 mean: {sam2_mean}")
    print(f'Pearsons correlation: {r}')
    print(f'P-value: {p_value}')
    z_one_tail(alpha, p_value)
