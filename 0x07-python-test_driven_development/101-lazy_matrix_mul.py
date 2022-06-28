#!/usr/bin/python3
"""Module for matrices calculations using numpy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''multipy 2 matrices with numpy'''
    return np.dot(m_a, m_b)
