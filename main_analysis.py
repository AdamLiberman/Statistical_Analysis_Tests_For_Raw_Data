from main_analysis_sub_functions import input_file, read_file, choose_test, execute_test

def main():
    file, alpha = input_file()
    df = read_file(file)
    test_list, test_number = choose_test()
    execute_test(test_list, test_number, alpha, df)