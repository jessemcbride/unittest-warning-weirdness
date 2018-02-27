# Let's deprecate some stuff
import warnings


warnings.simplefilter('always')


def a():
    warnings.warn("deprecated", DeprecationWarning)


def b():
    warnings.warn("deprecated", DeprecationWarning)


def c():
    warnings.warn("deprecated", DeprecationWarning)
