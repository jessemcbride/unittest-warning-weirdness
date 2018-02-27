# Python 3.3 Unittest Weirdness

Run unittest in Python 3.3:

```
python -m unittest discover tests/
```

Observe that 5 of the 8 tests fail.


Run it in any other Python version:

```
python -m unittest discover tests/
```

Observe that the tests pass.

Why?