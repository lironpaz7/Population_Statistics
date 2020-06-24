import sys
from Data import *
from Statistics import *

WANTED_FEATURES = ["age", "earnings", "hours", "week"]
POPULATION = ["Men", "Women", "All"]
METHODS = [sum_func, mean, median]

FEATURES_Q2 = "female, education, earnings, marital"


def main(argv):
    """
    Prints the question title and the relevant details using the Data and Statistics methods.
    :param argv:
    :return:
    """
    path = argv[1]
    features = argv[2]
    print("Question 1:")
    print_details(POPULATION, load_data(path, features), WANTED_FEATURES, METHODS)

    print()

    print("Question 2:")
    population_statistics("Women", load_data(path, FEATURES_Q2), "education", "earnings", 0, 10, METHODS[1:])
    population_statistics("Women", load_data(path, FEATURES_Q2), "education", "earnings", 11, 20, METHODS[1:])


if __name__ == "__main__":
    main(sys.argv)
