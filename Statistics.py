from math import ceil
import Data

MARRIED_STATUS = ["Married Women", "Unmarried Women"]

WOMEN_DICT = {
    "Married": {1, 2, 3},
    "Unmarried": {4, 5, 6, 7}
}


def sum_func(values):
    """
    This function receives a list of numbers and sum them.
    :param values:
    :return:
    """
    total_sum = 0
    for i in values:
        total_sum += i
    return total_sum


def mean(values):
    """
    This function uses the sum function we made before and divides the result by the length of the list
    to create a mean value.
    :param values:
    :return:
    """
    return sum_func(values) / len(values)


def median(values):
    """
    This function takes the list and create a new sorted one. If the list length is even then the formula is:
    X[n/2] + X[n/2 + 1] and divide by 2. Otherwise just take ceil value of X[n/2] and divide by 2.
    :param values:
    :return:
    """
    arr = sorted(values)
    length = len(arr)
    if length % 2 == 0:
        return (arr[int((length - 1) / 2)] + arr[int((length - 1) / 2) + 1]) / 2
    else:
        return arr[ceil((length - 1) / 2)]


def population_statistics(population, data, feature_1, feature_2, min_val, max_val,
                          statistics_functions):
    """
    This function uses the filter_by_features method that we created before in order to get the wanted dictionary.
    The function receives the population wanted (Men,Women, etc..), data dict, feature_1 which will be the value
    to filter by, feature_2 is the value we want it's data values, min and max val are referring to the first
    feature and sets it's boundaries, statistics_functions are mean and median methods we made before.
    After we call we call the filter method 2 times we have two dictionary, first one is data_wanted[0] which
    contains the wanted data (married women) and data_wanted[1] contains the unwanted data (unmarried women).
    We printed the min and max val lines and then we we have a for loop that runs two 2 times, inside we made an
    empty list (tmp_list) and again we loop through the methods and appending the data returned into the tmp_list.
    Notice that we needed the first for loop because we wanted to spare lines of code and we actually deals with
    both data_wanted[0] and data_wanted[1] one after another.
    Finally we print the data (MARRIED_STATUS is a dictionary the contains the 2 options (married and unmarried))
    and the feature_2 which in this case is "earnings"(capitalize) and the tmp_list which contains the mean and
    median values.
    :param population: population type such as: 'Men', 'Women', 'All'
    :param data: dictionary
    :param feature_1: feature to filter by
    :param feature_2: feature to receive it's data.
    :param min_val: int
    :param max_val: int
    :param statistics_functions: list of methods for statistics purposes
    :return:
    """
    new_data = Data.filter_by_features(Data.filter_by_features(data, "female", Data.POP_DICT[population])[0], feature_1,
                                       {i for i in range(min_val, max_val + 1)})
    data_wanted = Data.filter_by_features(new_data[0], "marital", WOMEN_DICT["Married"])
    # WOMEN_DICT is a dictionary that contains the relevant data (which numbers refer to married women and
    # which aren't)
    print(f"If {min_val}<=Y<={max_val}, then:")
    for i in range(2):
        tmp_list = []
        for method in statistics_functions:
            tmp_list.append(str(method(data_wanted[i][feature_2])))
        print(f"{MARRIED_STATUS[i]}:\n{feature_2.capitalize()}: {', '.join(tmp_list)}")
