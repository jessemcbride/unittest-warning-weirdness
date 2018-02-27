# Python 3.3 Unittest Weirdness

Run unittest in Python 3.3:

```
(3.3.6env) jesse:unittest-weirdness jesse$ python --version
Python 3.3.6

(3.3.6env) jesse:unittest-weirdness jesse$ python -m unittest discover tests/
..FF.FFF
======================================================================
FAIL: test_b (test_main.TestMain)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jesse/unittest-weirdness/tests/test_main.py", line 19, in test_b
    self.assertTrue(len(warning_list), 1)
AssertionError: 0 is not true : 1

======================================================================
FAIL: test_c (test_main.TestMain)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jesse/unittest-weirdness/tests/test_main.py", line 25, in test_c
    self.assertTrue(len(warning_list), 1)
AssertionError: 0 is not true : 1

======================================================================
FAIL: test_d (test_secondary.TestSecondary)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jesse/unittest-weirdness/tests/test_secondary.py", line 13, in test_d
    self.assertTrue(len(warning_list), 1)
AssertionError: 0 is not true : 1

======================================================================
FAIL: test_e (test_secondary.TestSecondary)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jesse/unittest-weirdness/tests/test_secondary.py", line 19, in test_e
    self.assertTrue(len(warning_list), 1)
AssertionError: 0 is not true : 1

======================================================================
FAIL: test_f (test_secondary.TestSecondary)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jesse/unittest-weirdness/tests/test_secondary.py", line 25, in test_f
    self.assertTrue(len(warning_list), 1)
AssertionError: 0 is not true : 1

----------------------------------------------------------------------
Ran 8 tests in 0.002s

FAILED (failures=5)
```

Observe that 5 of the 8 tests fail.


Run it in any other Python version:

```
jesse:unittest-weirdness jesse$ python --version
Python 2.7.13
jesse:unittest-weirdness jesse$ python -m unittest discover tests/
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK

jesse:unittest-weirdness jesse$ python --version
Python 3.4.7
jesse:unittest-weirdness jesse$ python -m unittest discover tests/
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```


Observe that the tests pass.

Why?