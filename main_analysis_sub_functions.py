
import argparse
import pandas as pd
from z_test.z_test_main import z_test_main
from on_t_test.os_t_test_main import os_t_test_main
from matched_t_test.matched_t_test_main import matched_t_test_main
from ind_t_test.ind_t_test_main import ind_t_test_main
from pearson_correlation.pearson_correlation_main import r_correlation_main


test_dict = {
    "Z-test": z_test_main,
    "One-sample t-test": os_t_test_main,
    "Two-sample matched t-test": matched_t_test_main,
    "Two-sample independent t-test": ind_t_test_main,
    "Pearson Correlation": r_correlation_main
}


def input_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', help= 'Excel file with data')
    parser.add_argument('alpha', help= 'Choose a confidence level', type=float)
    args = parser.parse_args()
    filename = args.FILE
    alpha = args.alpha
    return filename, alpha


def read_file(filename):
    df = pd.read_excel(filename)
    return df


def choose_test():
    test_list = dict(enumerate(test_dict.keys(), start=1))
    test_number = int(input(f"Choose a test by its index: {test_list}"))
    return test_list[test_number]


def execute_test(test_input, alpha, df):
    if test_input in test_dict.keys():
        test_dict[test_input](df, alpha)
    else:
        print("Please choose a test from the list")
        exit()