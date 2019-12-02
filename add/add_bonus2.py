#!/usr/bin/python3

def add(*matrices):

    def check(data):
        if data == 1:
            return True
        else:
            raise ValueError

    return [[sum(slice) for slice in zip(*row) if check(len(set(map(len, row))))] 
            for row in zip(*matrices) if check(len(set(map(len, matrices))))]
