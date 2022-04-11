.. _activities_userguide:

============
 User Guide
============

This guide explains how to use this package and obtain results published in our
paper.  Results can be re-generated automatically by executing the following
command:

.. code-block:: sh

   (project) $ tgibm-result


For your reference, the tables and plots are repeated below, so you can check the
reproducibility of our solution.  You may also limit the output of the program
using command-line options.  You will find more information adding the
``--help`` flag on the command above:

.. code-block:: sh

   (project) $ tgibm-result --help
   
::

   options:
  -h, --help            show this help message and exit
  -n {0,1,2,3}, --norm {0,1,2,3}
                        Chooses which normalization to apply (optional). If you choose '0', 
                        then you would apply the minmax scaler. If you choose '1', then you 
                        would apply the z-normalization. If you choose '2', you would apply 
                        the polynomial features scaler first, and then the minmax scaler. If    
                        you choose '4', then you would apply the polynomial features scaler 
                        first, and then the z-normalization scaler. By default, if no specific  
                        case is select, prints all results.
  -d {0,1,2}, --dataset {0,1,2}
                        Decides which dataset to use for reporting results.
                        Options are 0, 1, 2 (0: winequality-white, 1: winequality-red, 2: housing)


Example of a pipeline
---------------------

Command-line arguments can help you select different parameters of the pipeline.

For example, to run both models on the Wine quality (white wine) dataset 
with a given normalization method Z-normalization, you should run:

.. code-block:: sh

    $ tgibm-result -d=0 -n=1





Results for Dataset 1 `winequality-white.csv`
---------------------------------------------

The samples are **not** randomized.  Results are present in
terms of Mean Absolute Error. 

If you choose a normalization method, it outputs tables for each model, 
and prints out the plot comparing MAE levels for each random state of each model.

For a chosen normalization 0 (minmax scaling):
==============================================

MAE for Linear Regression.

================== ============
   random state        MAE
================== ============
        0           8.3962e-16
        1           2.05534e-16
        2           1.90706e-15   
================== ============

MAE for Regression Trees.

================== ============
   random state        MAE
================== ============
        0           1.14615e-15
        1           0.0566081
        2           1.15857e-15   
================== ============

The plot can be accessed `here <https://github.com/imenbenmhd/MiniProject/tree/main/docs/img/minmax_00.png>`__.

For a chosen normalization 1 (z-norm scaling):
==============================================

MAE for Linear Regression.

================== ============
   random state        MAE
================== ============
        0           6.21605e-16
        1           5.45699e-16
        2           9.45084e-16   
================== ============

MAE for Regression Trees.

================== ============
   random state        MAE
================== ============
        0           0.00315739
        1           0.0603942
        2           0.0305857   
================== ============

The plot can be accessed `here <https://github.com/imenbenmhd/MiniProject/tree/main/docs/img/znorm_01.png>`__.

If a normalization is not chosen (the parameter is optional), it outputs 4 sets of tables for each 
normalization method, and 4 plots, together with the plot comparing mean values of MAE for different
normalization methods.

Plot comparison can be accessed `here <https://github.com/imenbenmhd/MiniProject/tree/main/docs/img/all_norms_0.png>`__.
