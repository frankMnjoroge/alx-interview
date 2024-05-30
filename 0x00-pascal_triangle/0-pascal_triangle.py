#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for y in range(n):
        row = []
        for z in range(y + 1):
            if z == 0 or z ==y:
                row.append(1)
            elif y > 0 and z > 0:
                row.append(triangle[y - 1][z - 1] + triangle[y - 1][z])
        triangle.append(row)
    return triangle
