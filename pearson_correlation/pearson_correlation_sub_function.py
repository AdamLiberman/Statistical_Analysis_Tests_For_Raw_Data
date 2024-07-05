import numpy as np
from scipy.stats import pearsonr
from z_test.z_test_sub_function import z_one_tail

r_tail_dict= {
    "two-sided": "the correlation is nonzero",
    "less": "the correlation is negative",
    "greater": "the correlation is positive"
}

def r_correlation_main(df, alpha):
    if df.size[1] != 2:
        print("The file's dimensions don't match the selected test")
        exit()
    else:
        test_type = r_get_input()
        r_result = pearsonr(df[0], df[1],alternative=test_type)
        r = r_result.statistic
        p_value = r_result.pvalue
        sam1_mean = np.mean(df[0])
        sam2_mean = np.mean(df[1])
        print(f"Group 1 mean: {sam1_mean}")
        print(f"Group 2 mean: {sam2_mean}")
        print(f'Pearsons correlation: {r}')
        print(f'P-value: {p_value}')
        z_one_tail(alpha, p_value)

def r_get_input():
    print("Choose alternative hypothesis")
    print(r_tail_dict)
    tail_list = dict(enumerate(r_tail_dict.keys(), start=1))    
    tail_number = int(input(f"Choose a test type by its index: {tail_list}"))
    return tail_list[tail_number]