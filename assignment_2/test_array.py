"""
Tests for our array class
"""

from array_class import Array

# 1D tests (Task 4)


def test_str_1d():
    """
    Checking that our Array class returns a string.

    """
    inst = Array((1,), 1)
    expected = "The Array has shape (1,1) and elements [1]"

    assert (inst.__str__() == expected)

def test_add_1d():
    """
    Checking that our Arrayclass __add__ method is implemented properly.
    """
    inst = Array((3,), 1,1,1)
    i = 10
    expected = [11,11,11]
    computed = inst + i

    assert (expected == computed)

def test_sub_1d():
    """
    Checking that our Arrayclass __sub__ method is implemented properly.
    """
    inst = Array((3,), 10,10,10)
    inst2 = Array((3,), 5,5,5)
    expected = [5,5,5]
    computed = inst - inst2

    assert (expected == computed)


def test_mul_1d():
    """
    Checking that our Arrayclass __mul__ method is implemented properly.
    """
    inst = Array((3,), 1,2,3)
    i = 10
    expected = [10, 20, 30]
    computed = inst * i

    assert (expected == computed)


def test_eq_1d():
    """
    Checking that our Arrayclass __eq__ method is implemented properly.
    """
    inst = Array((3,), 1, 2, 3)
    inst2 = Array((3,), 2, 2, 2)
    i = [1, 2, 3]
    expected = [2, 4, 6]
    computed = inst * inst2

    assert (inst.values == i)
    assert (expected == computed)


def test_same_1d():
    """
    Checking that our Arrayclass is_equal method is implemented properly.
    """
    inst = Array((3,), 1,1,1)
    inst2 = Array((3,), 1,1,1)

    assert all(inst.is_equal(inst2))



def test_smallest_1d():
    """
    Checking that our Arrayclass min_element method is implemented properly.
    """
    inst = Array((3,), 1, 10, 23)
    expected = 1
    computed = inst.min_element()

    assert (computed == expected)

def test_mean_1d():
    """
    Checking that our Arrayclass mean_element method is implemented properly.
    """
    inst = Array((3,), 0, 5, 10)
    expected = 5
    computed = inst.mean_element()

    assert (expected == computed)


# 2D tests (Task 6)


def test_add_2d():
    pass


def test_mult_2d():
    pass


def test_same_2d():
    pass


def test_mean_2d():
    pass


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
