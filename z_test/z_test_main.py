from z_test_sub_function import z_get_input, z_computing, z_output

def z_test_main(df, alpha):
    if df.size[1] != 1:
        print("The file's dimensions don't match the selected test")
        exit()
    else:
        tail_input, pop_mean, pop_std = z_get_input()
        sam_mean, z_score, p_value = z_computing(df, pop_mean, pop_std)
        z_output(alpha, p_value, tail_input, sam_mean, pop_mean, z_score)