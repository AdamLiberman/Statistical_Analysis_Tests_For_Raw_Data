from main_analysis_sub_functions import read_file
from z_test.z_test_sub_function import z_computing
from os_t_test.os_t_test_sub_function import os_t_computation
from matched_t_test.matched_t_test_sub_function import matched_t_computation
from ind_t_test.ind_t_test_sub_function import ind_t_computation
from pearson_correlation.pearson_correlation_sub_function import r_computation

def test_z_test_main():
    df = read_file('z_test_data_final.xlsx')
    p_value, _, _ = z_computing(df, 7, 2.5)
    assert round(p_value, 3) == 0.167

def test_os_t_test_main():
    df = read_file('os_t_test_data.xlsx')
    _, p_value, _, _ = os_t_computation(df, 102, 'two-sided', 0.05)
    assert round(p_value, 3) == 0.023

def test_matched_t_test_main():
    df = read_file('matched_t_test_data.xlsx')
    _, p_value, _, _, _ = matched_t_computation(df,'two-sided', 0.05)
    assert round(p_value, 4) == 0.0005

def test_ind_t_test_main():
    df = read_file('ind_t_test_data.xlsx')
    _, p_value, _, _, _ = ind_t_computation(df,'two-sided', 0.05, True)
    assert round(p_value, 4) == 0.0009

def test_r_correlation_test_main():
    df = read_file('r_correlation_test_data.xlsx')
    r, _, _, _ = r_computation(df,'two-sided')
    assert round(r, 3) == 0.935