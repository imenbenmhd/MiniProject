"""User script to conduct the first hypothesis in the course"""

import numpy as np

np.seterr(divide="ignore")

import database
import algorithm
import analysis
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

models = ["LinearRegression", "Regressiontree"]

def test_mae(data, norm):
    """Runs one single test, returns the MAE on the test set for chosen data and norm"""

    mae_tables = [pd.DataFrame(np.zeros((3, 2))), pd.DataFrame(np.zeros((3, 2)))]
    mae_tables[0].columns = ["random state", "MAE"]
    mae_tables[1].columns = ["random state", "MAE"]


    for i, model in enumerate(models):
        y_train, y_predict = algorithm.regression(data, norm, models[i])
        for j, seed in enumerate(database.seeds):
            mae_tables[i].iloc[j, 0] = j
            mae_tables[i].iloc[j, 1] = analysis.mean_abs_err(y_train[j], y_predict[j])

    return mae_tables


def test_plot(mae_tables):

    for i in range(len(mae_tables)):
        plt.plot(mae_tables[i].iloc[:, 0], mae_tables[i].iloc[:, 1], '-o', label= models[i])
    plt.xticks([0, 1, 2], ['proto1', 'proto2', 'proto3'], rotation = 30)
    plt.yticks(np.arange(0, 0.07, step=0.01))
    plt.xlabel('Protocol')
    plt.ylabel('MAE')
    plt.title("Comparison of different models for different seeds")
    plt.legend()
    plt.show()


def test_all_norms(data):

    y_lr = np.zeros(4)
    y_rt = np.zeros(4)
    norms = ['minmax', 'z-norm', 'poly-minmax', 'poly-znorm']

    for i in range(4):
        y_lr[i] = test_mae(data, i)[0].iloc[:, 1].mean()
        y_rt[i] = test_mae(data, i)[1].iloc[:, 1].mean()

    plt.plot(norms, y_lr, label= models[0])
    plt.plot(norms, y_rt, label= models[1])
    plt.xlabel('Normalization')
    plt.ylabel('MAE')
    plt.title("Comparison of different norms for a chosen dataset")
    plt.legend()
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.8, 
                    hspace=0.8)
    plt.show()


def test_explore():

    y_lr = np.zeros((3, 4))
    y_rt = np.zeros((3, 4))
    norms = ['minmax', 'z-norm', 'poly-minmax', 'poly-znorm']

    for i in range(3):
        for j in range(4):
            y_lr[i][j] = test_mae(i, j)[0].iloc[:, 1].mean()
            y_rt[i][j] = test_mae(i, j)[1].iloc[:, 1].mean()


    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex = True)
    fig.suptitle('Explorative view for each dataset')
    ax1.plot(norms, y_lr[0], label= models[0])
    ax1.plot(norms, y_rt[0], label= models[1])
    ax1.title.set_text('First database: ' + database.data_base[0])
    ax1.set_ylabel('MAE')
    ax2.plot(norms, y_lr[1], label= models[0])
    ax2.plot(norms, y_rt[1], label= models[1])
    ax2.title.set_text('Second database: ' + database.data_base[1])
    ax2.set_ylabel('MAE')
    ax3.plot(norms, y_lr[2], label= models[0])
    ax3.plot(norms, y_rt[2], label= models[1])
    ax3.title.set_text('Third database: ' + database.data_base[2])
    ax3.set_ylabel('MAE')
    ax1.legend()
    ax2.legend()
    ax3.legend()
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
    1. Returns plots for all datasets in the original report:
       $ python result.py
    2. Only prints results and plots for dataset 2 (for every normalization method):
       $ python result.py -d=2
    3. Only prints results and plots for dataset 2 and normalization 1:
       $ python result.py --dataset=2 --norm=1

    """

    parser = argparse.ArgumentParser(
        usage="python %(prog)s [options]",
        description="Performs Linear Regression and Regression Trees algorithms",
        epilog=example_doc,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--norm",
        choices=[0, 1, 2, 3],
        type=int,
        help="Chooses which normalization to apply (optional). If you choose '0', then "
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

    args = parser.parse_args()

    if args.dataset is not None:
        if args.norm is not None:
            mae_tables = test_mae(args.dataset, args.norm)
            for i, model in enumerate(models):
                print("MODEL : "+model)
                print(tabulate(mae_tables[i], headers='keys', tablefmt='psql'))
            test_plot(mae_tables)
        else:
            print("Dataset: ", database.data_base[args.dataset])
            for j in range(4):
                print("Normaliation method: ", j)
                mae_tables = test_mae(args.dataset, j)
                for i, model in enumerate(models):
                    print("MODEL: ", model)
                    print(tabulate(mae_tables[i], headers='keys', tablefmt='psql'))
                test_plot(mae_tables)
            test_all_norms(args.dataset)
            
    else:
        if args.norm is not None:
            print(example_doc)
        else:
            test_explore()

if __name__ == "__main__":
    main()
