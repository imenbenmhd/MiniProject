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

Protocol `proto1` is configured to use the first 30 samples for each class in
the dataset for training, and the last 20 samples for each class for testing
our solution.  The samples are **not** randomized.  Results are present in
terms of Mean Absolute Error, in percentage.  The best
results are **bold faced**.

Single Variables
================

MAE for Linear Regression.

================== ========
   Protocol           MAE
================== ========
        1          8.3962e-16
        2             36%
        3              
================== ========


Two Variables
=============

CER only using any two variables together.

================== ================== ========
    Variable 1         Variable 2       CER
================== ================== ========
   sepal length       sepal width       16%
 **sepal length**   **petal length**   **1%**
   sepal length       petal width        3%
   sepal width        petal length       3%
   sepal width        petal width        5%
   petal length       petal width        5%
================== ================== ========


Three Variables
===============

CER only using any three variables together.

================== ================== ================== ========
    Variable 1         Variable 2         Variable 3       CER
================== ================== ================== ========
   sepal length       sepal width        petal length       3%
   sepal length       sepal width        petal width        5%
 **sepal length**   **petal length**   **petal width**    **1%**
   sepal width        petal length       petal width        5%
================== ================== ================== ========


All Variables
=============

The CER using all variables available in the dataset is **3%**.


Results for Protocol `proto2`
-----------------------------

Protocol `proto2` is configured to use the last 30 samples for each class in
the dataset for training, and the first 20 samples for each class for testing
our solution.  The samples are **not** randomized.  Results are present in
terms of total Classification Error Rate (CER), in percentage. The best results
are **bold faced**.
