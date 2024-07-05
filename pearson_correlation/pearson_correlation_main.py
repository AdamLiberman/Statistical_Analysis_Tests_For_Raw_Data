from pearson_correlation_sub_function import r_get_input, r_computation, r_output

def r_correlation_main(df, alpha):
    if df.size[1] != 2:
        print("The file's dimensions don't match the selected test")
        exit()
    else:
        test_type = r_get_input()
        r, p_value, sam1_mean, sam2_mean = r_computation(df, test_type)
        r_output(alpha, r, p_value, sam1_mean, sam2_mean)