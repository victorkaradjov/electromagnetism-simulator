import numpy as np
import pytest
from fdtd.fields import initialize_fields


def test_initialize_fields_dimensions():
    e_x, h_y = initialize_fields(10)

    assert e_x.shape == (11,)
    assert h_y.shape == (10,)


def test_initialize_fields_initial_values():
    e_x, h_y = initialize_fields(10)

    np.testing.assert_array_equal(e_x, np.zeros(11))
    np.testing.assert_array_equal(h_y, np.zeros(10))


def test_initialize_fields_invalid_N():
    with pytest.raises(ValueError):
        initialize_fields(0)


def test_initialize_fields_non_integer_N():
    with pytest.raises(ValueError):
        initialize_fields(2.5)


def test_initialize_fields_boolean_N():
    with pytest.raises(ValueError):
        initialize_fields(True)
