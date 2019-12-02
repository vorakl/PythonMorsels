#!/usr/bin/python3

def add(*matrixes):
    return [[sum(slice) for slice in zip(*row)] 
            for row in zip(*matrixes)]
