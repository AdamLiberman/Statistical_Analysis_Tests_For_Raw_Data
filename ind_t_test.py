import scipy.stats as stats
 
def ind_t_test_main(df, alpha):
    if df.size[1] != 2:
        print("The file's dimensions don't match the selected test")
    else:
        t_test, p_value = stats.ttest_ind(a=df[0], b=df[1], equal_var=True)
        print('p-value :',p_value)
        if p_value <  alpha:
            print("Reject Null Hypothesis")
        else:
            print("Fail to Reject Null Hypothesis")