import numpy as np


def get_user_input():
    while True:
        try:
            technique_input = int(input('''Please select the data transformation technique you want to use (for 1d set):
                                    1. Logarithmic Transformation
                                    2. K-step single moving average
                                    3. Aggregation
                                    4. Min Max Normalization
                                    5. Standardization
                                    '''))
        except ValueError:
            print("Sorry, Please select a correct option.\n")
            continue

        if 1 <= technique_input <= 5:
            break
        else:
            print("Sorry, your select should be between 1 and 5.\n")
            continue

    return technique_input


def get_data_set():
    while True:
        test = input("Please enter comma seperated list of numbers\n")
        test_list = test.split(',')
        try:
            data_set = [float(x.strip()) for x in test_list]
        except:
            print('please try again, with only numbers separated by commas (e.g. "1,2,3")\n')
            continue
        else:
            print(data_set)
            break
    return data_set


def log_transformation(test_data):
    return print(repr(np.log(test_data)))


def k_step_average(test_data):
    # k step average replaces each values with the average of k-1 elements before it
    # get k value here
    k = 3
    transformed_data = []
    for i in range(len(test_data)):
        if i < k-1:
            transformed_data.append(test_data[i])
        else:
            sum_of_values = 0
            for j in range(1, k+1):
                sum_of_values += test_data[i-k+j]
            transformed_data.append(sum_of_values/k)
    return print(repr(transformed_data))


def aggregation(test_data):
    # takes the average of 2 adjacent values
    transformed_data = []
    for i in range(0, len(test_data), 2):
        transformed_data.append((test_data[i] + test_data[i+1])/2)
    return print(repr(transformed_data))


def min_max_normalization(test_data):
    min_test_data = np.min(test_data)
    max_test_data = np.max(test_data)
    diff = max_test_data - min_test_data
    return print(repr([(x - min_test_data)/diff for x in test_data]))


def standardization(test_data):
    mean_test_data = np.mean(test_data)
    standard_deviation_test_data = np.std(test_data)
    return print(repr([(x - mean_test_data)/standard_deviation_test_data for x in test_data]))


# Data Transformation Types
if __name__ == "__main__":
    # get the transformation name from user
    user_input = get_user_input()

    data = get_data_set()
    # Perform data transformation
    perform_data_transformation = \
        {1: log_transformation, 2: k_step_average, 3: aggregation, 4: min_max_normalization, 5: standardization}
    perform_data_transformation[user_input](data)

