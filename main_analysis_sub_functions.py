import argparse
import pandas as pd
from z_test_function import z_test_main
from os_t_test_function import os_t_test_main
from matched_t_test import matched_t_test_main
from ind_t_test import ind_t_test_main
from pearson_correlation import r_correlation_main

def input_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', help= 'Excel file with data')
    parser.add_argument('alpha', help= 'Choose a confidence level', type=float)
    args = parser.parse_args()
    filename = args.FILE
    alpha = args.alpha
    return filename, alpha

def read_file(filename):
    df = pd.read_excel(filename, index_col=0)
    return df

def choose_test():
    test_list = {"1":"Z-test", "2":"one-sample t-test", "3":"Two-sample matched t-test","4":"Two-sample independent t-test","5":"Pearson Correlation"}
    test_number = input(f"Choose a test: {test_list}")
    return test_list, test_number

def execute_test(test_list, test_number, alpha, df):
    if test_list[test_number] == 1:
        z_test_main(df, alpha)
    if test_list[test_number] == 2:
        os_t_test_main(df, alpha)
    if test_list[test_number] == 3:
        matched_t_test_main(df, alpha)
    if test_list[test_number] == 4:
        ind_t_test_main(df, alpha)
    if test_list[test_number] == 5:
        r_correlation_main(df, alpha)
    else: 
        print("Please choose a test from the list")
