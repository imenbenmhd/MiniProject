.. _activities_userguide:

============
 User Guide
============

This guide explains how to use this package and obtain results published in our
paper.  Results can be re-generated automatically by executing the following
command:

.. code-block:: sh

   (project) $ python result.py


For your reference, the tables and plots are repeated below, so you can check the
reproducibility of our solution.  You may also limit the output of the program
using command-line options.  You will find more information adding the
``--help`` flag on the command above:

.. code-block:: sh

   (project) $ python result.py --help



Results for Dataset 1 `winequality-white.csv`
-----------------------------

The samples are **not** randomized.  Results are present in
terms of Mean Absolute Error. 

If you choose a normalization method, it outputs tables for each model, 
and prints out the plot comparing MAE levels for each random state of each model.

For a chosen normalization 0 (minmax scaling):
================

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
=============

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

