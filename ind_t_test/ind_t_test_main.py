from ind_t_test.ind_t_test_sub_function import ind_t_get_input, ind_t_computation
from matched_t_test.matched_t_test_sub_function import matched_t_output

def ind_t_test_main(df, alpha):
    if df.shape[1] != 2:
        print("The file's dimensions don't match the selected test")
        exit()
    else:
        t_tail, equal_variances = ind_t_get_input()
        t_statistic,p_value, sam1_mean, sam2_mean, ci = ind_t_computation(df, t_tail, alpha, equal_variances)
        matched_t_output(alpha, t_statistic, p_value, sam1_mean, sam2_mean, ci)