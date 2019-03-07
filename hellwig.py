from itertools import combinations

import numpy as np
import scipy as sp

# wczytac z pliku liste X z pliku CSV
class Hellwig:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.N = len(self.X)
        self.Combinations = self.All(self.X)
        self.R0 = self.CreateR0()
        self.R = self.CreateR()
        self.h = self.Createh()
        self.H = self.CreateH()
        self.Answer = np.array(self.Combinations[np.argmax(self.H)])

    def __str__(self):
        return str(self.Answer)


    def n(self, arr, n):
        if len(arr) == 1:
            #val = arr[0]
            #return np.array([[val, val]])
            pass
        return list(combinations(arr, n))

    def All(self, arr):
        output = []
        N = range(len(arr))
        for n in N:
            n += 1
            tmp = self.n(N, n)
            for i in range(len(tmp)):
                output.append(list(tmp[i]))
        return np.array(output)

    def CreateR0(self):
        tmp = np.zeros(self.N)
        for i in range(self.N):
            tmp[i] = sp.stats.pearsonr(self.Y, self.X[i])[0]
        return tmp


    def CreateR(self):
        self.R = np.array
        tmp = np.zeros((self.N, self.N))
        for i in range(self.N):
            for j in range(self.N):
                tmp[i][j] = sp.stats.pearsonr(self.X[i], self.X[j])[0]
        return tmp

    def Createh(self):
        tmp = self.Combinations
        output = []
        for i in range(len(tmp)):
            o = []
            mianownik = 0
            for j in range(len(tmp[i])):
                mianownik += np.absolute(self.R[tmp[i][0]][tmp[i][j]])
            for j in range(len(tmp[i])):
                o.append(self.R0[tmp[i][j]]**2/mianownik)
            output.append(o)
        return np.array(output)


    def CreateH(self):
        tmp = []
        for combination in self.h:
            tmp.append(np.sum(combination))
        return np.array(tmp)
