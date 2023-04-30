#!/usr/bin/python3
"""Matrix multiplication module using numpy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices"""
    return numpy.matmul(m_a, m_b)
