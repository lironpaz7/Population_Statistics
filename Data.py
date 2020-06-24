import pandas
import Statistics
from math import log10

POP_DICT = {
    "Men": {0},
    "Women": {1},
    "All": {0, 1}
}


def load_data(path, features):
    """
    This function receives the path of the .csv file and a string of features (separated by comma).
    First we load the csv file to the main memory and and convert it to a dict (data) with pandas library.
    Then we converted the string into a list by removing spaces and split each word separated by comma.
    We created a new dict (data_chosen) that copies the data values only if it inside the features list.
    Then we converted the earnings list into log base 10 values and finally returned the dictionary.
    :param path: path to csv file
    :param features: string of features wanted from full data.
    :return:
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    # removes spaces, and then creates words that were separated by commas
    features = features.replace(" ", "").split(',')
    # creates the dictionary with the features we wanted.
    data_chosen = dict([(i, data[i]) for i in features])
    # execute the log operation on every value of earnings.
    data_chosen["earnings"] = [log10(i) for i in data_chosen["earnings"]]
    return data_chosen


def filter_by_features(data, feature, values):
    """
    This function receives a dictionary, a feature (age, earnings, etc..) and values which is a set of numbers
    which is allowed for filtering. We created two new dictionaries that will contain the wanted data
    and the unwanted data. The first for loop copies the key from the original dict(data) and an empty list.
    We created a zipped_new_data which is a set of tuples (value of the feature in the original dict, index). Finally
    we check for each key and for each tuple whether the data value (tuple[0]) is in values range (meets the set
    requirements) and copies the data to the wanted_data dict, otherwise (if the values aren't in the set) copies
    to the unwanted_data dict. Then we returned the two dictionary (Python return them as a tuple of two dict).
    :param data: dictionary
    :param feature: feature from data
    :param values: set of numbers
    :return:
    """
    wanted_data = dict()
    unwanted_data = dict()

    for key in data.keys():
        wanted_data.update({key: []})
        unwanted_data.update({key: []})

    zipped_new_data = [(i, j) for i, j in zip(data[feature], range(len(data[feature])))]
    # list of tuples that consist the feature value and an index so we can loop through the wanted data only
    # if exist in values set.
    for key in data.keys():
        for value_index in zipped_new_data:
            if value_index[0] in values:
                wanted_data[key].append(data[key][value_index[1]])
            else:
                unwanted_data[key].append(data[key][value_index[1]])

    return wanted_data, unwanted_data


def print_details(population, data, features, statistic_functions):
    """
    This function receives population list that consist: Men, Women, All, data dictionary, relevant features:
    such as: age, female, earnings, etc. and the statistic methods from Statistic.py.
    We run in a for loop through the population type, then we run over all the features and making a new tuple list
    that consist couples of (feature_value, index) only if it's matching the gender.
    Then we created a new list (new_data) that consist all of the values from the zipped list, (because k[0]
    is the individual tuple and position 0 which is the value). Finally we run all over the methods we received
    and execute them on the (new_data) while appending each of results into a new list and then print out
    as a string.
    :param population: list of population types
    :param data: dictionary
    :param features: list of features from data
    :param statistic_functions: list of methods for statistics purposes
    :return:
    """
    for gender in population:
        print(f"{gender.capitalize()}:")
        for feature in features:
            zipped_new_data = [(i, j) for i, j in zip(data[feature], range(len(data[feature]))) if
                               data["female"][j] in POP_DICT[gender]]
            # list of tuples that consist the feature value and an index only if the data is matching the gender.
            new_data = [k[0] for k in zipped_new_data]
            features_list = []
            for method in statistic_functions:
                features_list.append(str(method(new_data)))
            print(f"{feature.capitalize()}: " + ", ".join(features_list))
