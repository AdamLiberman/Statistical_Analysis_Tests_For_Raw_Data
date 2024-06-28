import scipy.stats as stats
 
def matched_t_test_main(df, alpha):
    if df.size[1] != 2:
        print("The file's dimensions don't match the selected test")
    else:
        _ , p_value = stats.ttest_rel(a=df[0], b=df[1])
        print('p-value :',p_value)
        if p_value <  alpha:
            print("Reject Null Hypothesis")
        else:
            print("Fail to Reject Null Hypothesis")