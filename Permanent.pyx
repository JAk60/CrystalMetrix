# permanent.pyx
cimport cython
from libc.math cimport abs

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double permanent(list matrix):
    cdef int n = len(matrix)
    cdef int i, j
    cdef double result = 0.0
    cdef list submatrix

    if n == 1:
        return matrix[0][0]

    for j in range(n):
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        result += matrix[0][j] * permanent(submatrix)

    return result