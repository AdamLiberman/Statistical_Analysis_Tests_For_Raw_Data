import numpy as np
import scipy.stats as stats

def z_one_tail(alpha, p_value):
    if p_value <  alpha:
        print("The sample mean is significantly different than the population mean, Null Hypothesis is rejected")
    else:
        print("The sample mean is not significantly different than the population mean, Null Hypothesis cannot be rejected")

def z_two_tail(alpha, p_value):
    if p_value <  alpha/2:
        print("The sample mean is significantly different than the population mean, Null Hypothesis is rejected")
    else:
        print("The sample mean is not significantly different than the population mean, Null Hypothesis cannot be rejected")

z_tail_dict = {"one-tail": z_one_tail, "two-tail": z_two_tail}

def z_get_input():
    try:
        print("Choose alternative hypothesis")
        tail_list = dict(enumerate(z_tail_dict.keys(), start=1))    
        tail_number = int(input(f"Choose a test by its index: {tail_list}"))
        pop_mean = float(input("What is the population mean? "))
        pop_std = float(input("What is the population std? "))
    except ValueError:
        print("Please enter a number")
        exit()
    return tail_list[tail_number],pop_mean,pop_std

def z_computing(df, pop_mean, pop_std):
    sam_mean = np.mean(df.iloc[:, 0])
    z_score = (((sam_mean-pop_mean)*np.sqrt(len(df)))/pop_std)
    if pop_mean > sam_mean:
        p_value = stats.norm.cdf(z_score)
    if pop_mean <= sam_mean:
        p_value = 1-stats.norm.cdf(z_score)
    return p_value, z_score, sam_mean

def z_output(alpha, p_value, tail_input, sam_mean, pop_mean, z_score):
    print("--------------------------------------------------")
    print("Results:")
    print(f"Sample mean: {sam_mean:.4f}")
    print(f"population mean: {pop_mean:.4f}")
    print(f"Z-Score : {z_score:.4f}") 
    print(f"p-value : {p_value:.4f}")
    if tail_input in z_tail_dict.keys():
        z_tail_dict[tail_input](alpha, p_value)
    else:
        print("Please choose a tail test")
        exit()

        