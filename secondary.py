# Let's deprecate some stuff
import warnings


warnings.simplefilter('always')


def d():
    warnings.warn("deprecated", DeprecationWarning)


def e():
    warnings.warn("deprecated", DeprecationWarning)


def f():
    warnings.warn("deprecated", DeprecationWarning)
