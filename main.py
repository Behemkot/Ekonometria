from sklearn import datasets
import hellwig as H

import numpy as np

if __name__ == "__main__":
    iris_data = datasets.load_iris()
    X = iris_data.data.tolist()
    Y = iris_data.target.tolist()
    Combinations = []

    new_X = []
    for i in range(len(X[0])):
        out = []
        for j in range(len(X)):
            out.append(X[j][i])
        new_X.append(out)

    new_X = np.array(new_X)
    X = new_X

    Hel = H.Hellwig(X, Y)

    '''
    print("Macierz R")
    print(Hel.R)
    print("")
    print("Macierz R0")
    print(Hel.R0)

    print("Elementy h:")
    for combination in Hel.h:
        print(combination)

    print("")

    print("Elementy H:")
    for combination in Hel.H:
        print(combination)

    print('')
    '''

    print(Hel)
