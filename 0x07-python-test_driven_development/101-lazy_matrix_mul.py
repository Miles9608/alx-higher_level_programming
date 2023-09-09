zy_matrix_mul function.

This function directs one module, lazy_matrix_mul().
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Return a new matrix where each element has been divided by div.

    Args:
        m_a (list): list of lists of integers or floats.
        m_b (list): list of lists of integers or floats.
    """

    return np.dot(m_a, m_b)
