from matched_t_test_sub_function import matched_t_get_input, matched_t_computation, matched_t_output

def matched_t_test_main(df, alpha):
    if df.size[1] != 2:
        print("The file's dimensions don't match the selected test")
        exit()
    else:
        t_tail = matched_t_get_input()
        t_statistic, p_value, sam1_mean, sam2_mean,ci = matched_t_computation(df, t_tail)
        matched_t_output(alpha, t_statistic, p_value, sam1_mean, sam2_mean, ci)