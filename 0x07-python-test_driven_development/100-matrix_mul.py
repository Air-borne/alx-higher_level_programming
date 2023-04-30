#!/usr/bin/python3
"""Matirx multiplication module"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices"""
    if isinstance(m_a, list) is False:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list) is False:
        raise TypeError("m_b must be a list")

    if all(isinstance(x, list) for x in m_a) is False:
        raise TypeError("m_a must be a list of lists")

    if all(isinstance(x, list) for x in m_b) is False:
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or all(len(x) > 0 for x in m_a) is False:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or all(len(x) > 0 for x in m_b) is False:
        raise ValueError("m_b can't be empty")

    if all(all(isinstance(x, (int, float)) for x in row)
            for row in m_a) is False:
        raise TypeError("m_a should contain only integers or floats")

    if all(all(isinstance(x, (int, float)) for x in row)
            for row in m_b) is False:
        raise TypeError("m_b should contain only integers or floats")

    mx_len = len(m_a[0])
    if (all(len(row) == mx_len for row in m_a)) is False:
        raise TypeError("each row of m_a must be of the same size")

    mx_len = len(m_b[0])
    if (all(len(row) == mx_len for row in m_b)) is False:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    n_len = len(m_a)
    p_len = len(m_b[0])
    m_len = len(m_b)
    result_matrix = [[0 for x in range(p_len)] for y in range(n_len)]
    for i in range(n_len):
        for j in range(p_len):
            sum = 0
            for k in range(m_len):
                sum += m_a[i][k] * m_b[k][j]
            result_matrix[i][j] = sum
    return result_matrix
