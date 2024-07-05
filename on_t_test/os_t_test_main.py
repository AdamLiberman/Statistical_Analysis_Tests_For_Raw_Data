from os_t_test_sub_function import os_t_get_input, os_t_computation, os_t_output

def os_t_test_main(df, alpha):
    if df.size[1] != 1:
        print("The file's dimensions don't match the selected test")
        exit()
    else:
        t_tail, pop_mean = os_t_get_input()
        t_statistic, p_value, sam_mean, ci = os_t_computation(df, pop_mean, t_tail)
        os_t_output(alpha, p_value, sam_mean, pop_mean, t_statistic, ci)