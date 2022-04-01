Unit tests
============

Unit tests can be excuted by the use of the python library pytest. The unit tests of each modules are seperated in
4 differents files that are ran as seen after.

Database
---------
.. code-block:: shell

  (project) $ conda install pytest
  (project) $ pytest -sv test.py
============================= test session starts ==============================
platform linux -- Python 3.9.11, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /.../envs/miniproject/bin/python
cachedir: .pytest_cache
rootdir: /.../MiniProject
collected 3 items                                                              

test-database.py::test_load_1 PASSED
test-database.py::test_split_1 PASSED
test-database.py::test_split_2 PASSED

============================== 3 passed in 0.36s ===============================


In case of problems, please get in touch with us `by e-mail
<mailto:imen.benmhd@gmail.com>`_.

