"""User script to conduct the first hypothesis in the course"""

import logging
import itertools
import string

import numpy as np

np.seterr(divide="ignore")

import database
import algorithm
import analysis
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

variables = [database.wine_variables, database.housing_variables]
models = ["LinearRegression", "Regressiontree"]

def test_mae(data, norm):
    """Runs one single test, returns the MAE on the test set for chosen data and norm"""

    mae_tables = [pd.DataFrame(np.zeros((3, 2))), pd.DataFrame(np.zeros((3, 2)))]
    mae_tables[0].columns = ["protocol", "MAE"]
    mae_tables[1].columns = ["protocol", "MAE"]


    for i, model in enumerate(models):
        y_train, y_predict = algorithm.regression(data, norm, models[i])
        for j, seed in enumerate(database.seeds):
            mae_tables[i].iloc[j, 0] = j+1
            mae_tables[i].iloc[j, 1] = analysis.mean_abs_err(y_train[j], y_predict[j])

    return mae_tables

def test_plot(mae_tables):
    for i in range(len(mae_tables)):
        plt.plot(mae_tables[i].iloc[:, 0], mae_tables[i].iloc[:, 1], '-o', label= models[i])
    plt.xticks(range(0, 5, 1))
    plt.xlabel('Protocol')
    plt.ylabel('MAE')
    plt.title("Comparison of different models for different seeds")
    plt.legend()
    plt.show()

def test_allnorms(data):
    tables = []
    for i in range(4):
        tables.append(test_mae(data, i))
    return tables

def test_explore():

    y_lr = np.zeros((3, 4))
    y_rt = np.zeros((3, 4))
    norms = ['minmax', 'z-norm', 'poly-minmax', 'poly-znorm']

    for i in range(3):
        for j in range(4):
            #print(test_mae(i, j)[0])#.iloc[:, 1])#.mean())
            y_lr[i][j] = test_mae(i, j)[0].iloc[:, 1].mean()
            y_rt[i][j] = test_mae(i, j)[1].iloc[:, 1].mean()


    fig=plt.figure(figsize=(18, 6), dpi= 80, facecolor='w', edgecolor='k')
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex = True, sharey = True)
    fig.suptitle('Explorative view for each dataset')
    ax1.plot(norms, y_lr[0], label= models[0])
    ax1.plot(norms, y_rt[0], label= models[1])
    ax1.title.set_text('First database: ' + database.data_base[0])
    ax2.plot(norms, y_lr[1], label= models[0])
    ax2.plot(norms, y_rt[1], label= models[1])
    ax2.title.set_text('Second database: ' + database.data_base[1])
    ax3.plot(norms, y_lr[2], label= models[0])
    ax3.plot(norms, y_rt[2], label= models[1])
    ax3.title.set_text('Third database: ' + database.data_base[2])
    plt.ylabel('MAE')
    plt.legend()
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.8, 
                    hspace=0.8)
    plt.show()



def main():
    """Main function to be called from the command line"""

    import argparse

    example_doc = """\
examples:
    1. Returns all tables and plots for all datasets in the original report:
       $ python result.py
    2. Only prints results and plots for dataset 2:
       $ python result.py -d=2
    3. Only prints results and plots for dataset 2 and normalization 1:
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
        "--norm",
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
        choices=[0, 1, 2],
        type=int,
        help="Decides which dataset to use for reporting results. "
             "Options are %(choices)s (0: winequality-white, 1: winequality-red,"
             " 2: housing)",
        )

    parser.add_argument(
        "-e",
        "--explore",
        choices=[False, True],
        type=bool,
        default=False,
        help="Determines whether to compare all 4 normalization methods on one graph. "
        "If you choose True, it will output the explorative comparison, otherwise not."
        "Default is False. ",
        )

    args = parser.parse_args()

    if (args.dataset is not None):
        arg_dataset = args.dataset
    else:
        print("Dataset argument not specified, running with default = 0")
        arg_dataset = 0

    if args.norm is not None:
        arg_norm = args.norm
    else:
        print("Normalization argument not specified, running with default = 0")
        arg_norm = 0

    if args.explore is not False:
        test_explore()
    else:
        mae_tables = test_mae(arg_dataset, arg_norm)
        for i, model in enumerate(models):
            print("MODEL : "+model)
            print(tabulate(mae_tables[i], headers='keys', tablefmt='psql'))
        test_plot(mae_tables)

if __name__ == "__main__":
    main()
