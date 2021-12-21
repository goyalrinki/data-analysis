import numpy as np
import ast
import collections

## Entropy Based Discretization :
# Finds a potential split that will split data with lower entropy
# 1. Calculate entropy for whole data set
# 2. For each potential split, calculate entropy for each bin, net entropy and then entropy gain
# 3. Select split with highest entropy gain



def make_splits(data_set, overall_entropy):
    print(data_set)
    info_gain_of_splits = {}
    # Create splits by using average of adjacent values
    # Convert data into 2 bins
    for i in range(len(data_set)-1):
        split_at = (int(data_set[i, 0]) + int(data_set[i+1, 0])) / 2
        print(f'Split at {split_at}')
        mask1 = data_set[:, 0].astype(float) <= split_at
        mask2 = data_set[:, 0].astype(float) > split_at
        # calculate entropy gain i.e. Initial entropy - net entropy of split
        info_gain_of_splits[split_at] = overall_entropy - calculate_net_entropy(data_set[mask1, :], data_set[mask2, :])
    # Find best split
    best_split = max(info_gain_of_splits, key=info_gain_of_splits.get)
    print(f'Best Split is at {best_split} with info gain {info_gain_of_splits.get(best_split)}')


def calculate_entropy(data_set_dict):
    # entropy is calculated for each bin -summation(p(i) * log p(i))
    # where p(i) is the probability of each label
    total = sum(data_set_dict.values())
    entropy = 0
    for key, value in data_set_dict.items():
        probability = value/total
        entropy += probability * np.log2(probability)
    round_entropy = round(-entropy, 3)
    print(f'Entropy for dataset {data_set_dict} is {round_entropy}')
    return round_entropy


def calculate_net_entropy(less_than_equal, greater_than):
    # Calculate net entropy of a split
    less_than_equal_shape = np.shape(less_than_equal)[0]
    greater_than_shape = np.shape(greater_than)[0]
    total = less_than_equal_shape + greater_than_shape
    net_entropy = (less_than_equal_shape / total * calculate_entropy(collections.Counter(less_than_equal[:, 1]))) + (
                greater_than_shape / total * calculate_entropy(collections.Counter(greater_than[:, 1])))
    print(f'Net Entropy is {net_entropy}')
    return net_entropy


if __name__ == "__main__":
    # Get the data from user in form of matrix
    arr = np.array(ast.literal_eval(input("Enter your 2d matrix (in format : [[2,3],[4,5]])\n")))

    make_splits(arr, calculate_entropy(collections.Counter(arr[:, 1])))
