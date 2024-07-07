import numpy as np
from scipy import stats
from z_test.z_test_sub_function import z_one_tail

t_tail_dict = {
    "two-sided": "The sample mean is different than the population mean",
    "less": "The sample mean is smaller than the  population mean",
    "greater": "The sample mean is greater than the population mean"
}

def os_t_get_input():
    try:
        print("Choose alternative hypothesis")
        print (t_tail_dict)
        tail_list = dict(enumerate(t_tail_dict.keys(), start=1))    
        tail_number = int(input(f"Choose a test type by its index: {tail_list}"))
        pop_mean = float(input("What is the population's mean? "))
    except ValueError:
        print("Please enter a number")
        exit()
    return tail_list[tail_number], pop_mean

def os_t_computation(df, pop_mean, t_tail, alpha):
    test_result = stats.ttest_1samp(df, pop_mean, alternative=t_tail)
    t_statistic = test_result.statistic[0]
    p_value = test_result.pvalue[0]
    sam_mean = np.mean(df.iloc[:, 0])
    confid_level = 1-alpha
    ci = test_result.confidence_interval(confidence_level=confid_level)
    return t_statistic, p_value, sam_mean, ci

def os_t_output(alpha, p_value, sam_mean, pop_mean, t_statistic, ci):
    print("--------------------------------------------------")
    print("Results:")
    print(f"Sample mean: {sam_mean:.4f}")
    print(f"population mean: {pop_mean:.4f}")
    print(f"t_statistic : {t_statistic:.4f}") 
    print(f"p-value : {p_value:.4f}")
    print(f"Confidence interval: ({ci.low[0]:.4f},{ci.high[0]:.4f})")
    z_one_tail(alpha, p_value)

  