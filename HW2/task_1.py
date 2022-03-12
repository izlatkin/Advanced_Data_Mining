import math
import numpy as np
import scipy.stats

from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig

def task1_2():
    A = [1, 2, 3, 4]
    B = [1, 2, 3, 4]
    data = np.array([A,B])
    covMatrix = np.cov(data, bias=True)
    print (covMatrix)
    r = np.corrcoef(A, B)
    print(r)
    w = scipy.stats.pearsonr(A, B)
    print(w)


def task3():
    # define a matrix
    A = [1, 2, 3, 4]
    B = [1, 2, 3, 4]

    A = [1.25, 1.25]
    B = [1.25, 1.25]

    A = array([A,B])
    print(A)
    # calculate the mean of each column
    M = mean(A.T, axis=1)
    print(M)
    # center columns by subtracting column means
    C = A - M
    print(C)
    # calculate covariance matrix of centered matrix
    V = cov(C.T)
    print(V)
    # eigendecomposition of covariance matrix
    values, vectors = eig(V)
    print("vector")
    print(vectors)
    print("values")
    print(values)
    # project data
    # P = vectors.T.dot(C.T)
    # print(P.T)


def main():
    task3()




if __name__ == "__main__":
    main()
