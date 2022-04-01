"""User script to conduct the first hypothesis in the course"""

import logging
import itertools

import numpy as np

numpy.seterr(divide="ignore")

import database
import preprocessor
import algorithm
import analysis

variables = [database.wine_variables, database.housing_variables]
models = ["LinearRegression", "RegressionTrees"]

def test_mae(dat, nor):
    """Runs one single test, returns the MAE on the test set"""

    data = database.data_base.index(dat)
    norm = algorithm.normalization[nor]

    y_train = np.zeros((3, 3))
    y_predict = np.zeros((3, 3))

    mae = np.zeros((3, 3))

    # 3. trains our logistic regression system
    for i in enumerate(models):
        for j in enumerate(database.seeds):

            y_train[i][j], y_predict[i][j] = algorithm.regression(data, norm, models[i])[j]
            mae[i][j] = analysis.mean_abs_err(y_train[i][j], y_predict[i][j])

    return mae


def test_impact_of_variables_single(tabnum, protocols):
    """Builds the first table of my report"""

    for n, p in enumerate(protocols):

        print(
            "\nTable %d: Single variables for Protocol `%s`:" % (n + tabnum, p)
        )
        print(60 * "-")

        for k in database.VARIABLES:
            result = test_one(p, [k])
            print(("%-15s" % k), "| %d%%" % (100 * result,))

    return len(protocols)


def test_impact_of_variables_2by2(tabnum, protocols):
    """Builds the first table of my report"""

    for n, p in enumerate(protocols):

        print(
            "\nTable %d: Variable combinations, 2x2 for Protocol `%s`:"
            % (n + tabnum, p)
        )
        print(60 * "-")

        for k in itertools.combinations(database.VARIABLES, 2):
            result = test_one(p, k)
            print(("%-30s" % " + ".join(k)), "| %d%%" % (100 * result,))

    return len(protocols)


def test_impact_of_variables_3by3(tabnum, protocols):
    """Builds the first table of my report"""

    for n, p in enumerate(protocols):

        print(
            "\nTable %d: Variable combinations, 3x3 for Protocol `%s`:"
            % (n + tabnum, p)
        )
        print(60 * "-")

        for k in itertools.combinations(database.VARIABLES, 3):
            result = test_one(p, k)
            print(("%-45s" % " + ".join(k)), "| %d%%" % (100 * result,))

    return len(protocols)


def test_impact_of_variables_all(tabnum, protocols):
    """Builds the first table of my report"""

    for k, p in enumerate(protocols):

        print("\nTable %d: All variables for Protocol `%s`:" % (k + tabnum, p))
        print(60 * "-")

        result = test_one(p, database.VARIABLES)
        print(
            ("%-45s" % " + ".join(database.VARIABLES)),
            "| %d%%" % (100 * result,),
        )

    return len(protocols)


def main():
    """Main function to be called from the command line"""

    import argparse

    example_doc = """\
examples:
    1. Returns all tables in the original report:
       $ python result.py
    2. Only prints results for dataset 2:
       $ python result.py -d=2
    3. Only prints results for dataset 2 and normalization 1:
       $ python result.py --dataset=2 --norm=1
    """

    parser = argparse.ArgumentParser(
        usage="python %(prog)s [options]",
        description="Performs Linear Regression and Regression trees algorithms",
        epilog=example_doc,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--normalization",
        choices=[0, 1, 2, 3],
        type=int,
        help="Chooses which normalization to apply.  If you choose '0', then "
             "you would apply the minmax scaler. If you choose '1', "
             "then you would apply the z-normalization. If you choose '2', "
             "you would apply the polynomial features scaler first, and then "
             "the minmax scaler. If you choose '4', then you would apply "
             "the polynomial features scaler first, and then the z-normalization "
             "scaler. By default, if no specific case is select, prints all results.",
             )

    parser.add_argument(
        "-d",
        "--dataset",
        choices=["0", "1", "2"],
        type=int,
        help="decides which dataset to use for reporting results. "
             "Options are %(default)s (0: winequality-white, 1: winequality-red,"
             " 2: housing)",
        )

    args = parser.parse_args()

    # keeps a nice sequential table number
    tabnum = 1

    if args.norm is not None:

        if args.norm == 0:
            test_impact_of_variables_single(tabnum, args.protocol)
        elif args.norm == 1:
            test_impact_of_variables_2by2(tabnum, args.protocol)
        elif args.norm == 2:
            test_impact_of_variables_3by3(tabnum, args.protocol)
        elif args.norm == 3:
            test_impact_of_variables_all(tabnum, args.protocol)

    else:
        tabnum += test_impact_of_variables_single(tabnum, args.protocol)
        tabnum += test_impact_of_variables_2by2(tabnum, args.protocol)
        tabnum += test_impact_of_variables_3by3(tabnum, args.protocol)
        test_impact_of_variables_all(tabnum, args.protocol)


if __name__ == "__main__":
    main()
