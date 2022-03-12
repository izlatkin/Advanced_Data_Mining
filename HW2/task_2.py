import math
import numpy as np
import scipy.stats
import scipy.stats as stats

from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig



def task3():
    A = [200, 300, 400, 600, 1000]
    data = np.array(A)
    print(stats.zscore(data))
    b = np.std(data)
    print(b)




def main():
    task3()




if __name__ == "__main__":
    main()
