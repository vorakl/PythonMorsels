#!/usr/bin/python3

def add(matrix1, matrix2):
    return [[d1+d2 for d1, d2 in zip(m1, m2)] 
            for m1, m2 in zip(matrix1, matrix2)]
