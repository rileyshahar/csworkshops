"""Compute the first 8 fibonacci numbers."""


def fib_step(fibs):
    """Update fibs to add the next fibonacci number."""
    # f(n) = f(n-1) + f(n-2)
    fibs.append(fibs[-1] + fibs[-2])


def first_n_fib(n):
    """Return a list of the first n fibonacci numbers."""

    # if n<2, ret's seed will be too large, so we need special cases
    if n == 0:
        return []

    if n == 1:
        return [1]

    # stores the computed values for later return
    ret = [1, 1]

    # repeat n-2 times; 2 iterations already done by intial conditions
    for _ in range(n - 2):
        fib_step(ret)

    return ret


def print_list(to_print):
    """Print each value in to_print."""
    for val in to_print:
        print(val)


lst = first_n_fib(8)
print_list(lst)


def test_first_n_fib_0():
    """Test that `first_n_fib` is correct for n=0."""
    assert first_n_fib(0) == []


def test_first_n_fib_1():
    """Test that `first_n_fib` is correct for n=1."""
    assert first_n_fib(1) == [1]


def test_first_n_fib_2():
    """Test that `first_n_fib` is correct for n=2."""
    assert first_n_fib(2) == [1, 1]


def test_first_n_fib_10():
    """Test that `first_n_fib` is correct for n=10."""
    assert first_n_fib(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
