import math
import cmath
import mpmath as mpm

"""
Set up mpmath
"""
PRECISION = 100
def updatePrecision(p = 100):
    PRECISION = p
    mpm.mp.dps = PRECISION

"""
________________________________________________________________________________
ALGORITHMS
________________________________________________________________________________
"""

# The Discrete Fourier Transform

def RecursiveDFT(aList, sign):

    n = len(aList)

    if n == 1: # Base case
        return aList
    else: # Recursive step
        aEven = [aList[2*n] for n in range(math.floor(n//2))]
        aOdd = [aList[2*n+1] for n in range(math.floor(n//2))]
        aEvenTransform = RecursiveDFT(aEven, sign)
        aOddTransform = RecursiveDFT(aOdd, sign)
        aTransform = dict()
        for k in range(n//2):
            aTransform[k] = aEvenTransform[k] + mpm.rect(1, k*sign*2*mpm.mpf(mpm.pi)/n)*aOddTransform[k]
            aTransform[k+n//2] = aEvenTransform[k] - mpm.rect(1, k*sign*2*mpm.mpf(mpm.pi)/n)*aOddTransform[k]
        return aTransform

def DFT(aList):
    """
    Use the RecursiveDFT function to perform a DFT of aList. Expects and returns a list.
    """
    transformDict = RecursiveDFT(aList, -1)
    return transformDict

def InverseDFT(aList):
    """
    Use the RecursiveDFT function to perform an inverse DFT of aList. Expects and returns a list.
    """
    transformDict = RecursiveDFT(aList, 1)
    newDict = {}
    for key, item in transformDict.items():
        newDict[key] = (1/len(aList)) * transformDict[key]
    return newDict

class Polynom:
    """
    A class to capture the algebraic behavior of the polynomials.
    """
    def __init__(self, initDict = dict(), var = "x"):
        self.termsDict = dict()
        if initDict:
            for pow, coeff in initDict.items():
                self.termsDict[pow] = mpm.mpc(initDict[pow])
        else:
            self.termsDict = dict({0:1})
        self.var = var

    def __int__ (self):
        return max([power for power in self.termsDict.keys()])

    def __str__ (self):
        outStr = ""
        for i in range(int(self)+1):
            if i in self.termsDict:
                outStr += str(mpm.mpmathify(self.termsDict[i])) + self.var + "^" + str(i) + " + "
        return outStr[:-3]

    def __add__ (self, other):
        newDict = self.termsDict
        for power in other.termsDict.keys():
            if power in newDict:
                newDict[power] += other.termsDict[power]
            else:
                newDict[power] = other.termsDict[power]
        return Polynom(initDict= newDict, var = self.var)

    def __mul__(self, other):
        selfList = self.listify()
        otherList = other.listify()
        len1 = self.nearest2(len(selfList))
        len2 = self.nearest2(len(otherList))
        newLen = 2*max(len1, len2)
        selfPadded = selfList + [0]*(newLen - len(selfList))
        otherPadded = otherList + [0]*(newLen - len(otherList))

        selfEval = DFT(selfPadded)
        otherEval = DFT(otherPadded)
        pointwiseProd = []
        for i in range(newLen):
          pointwiseProd.append(selfEval[i]*otherEval[i])
        inverted = InverseDFT(pointwiseProd)
        return Polynom(initDict = inverted, var = self.var)

    def __pow__(self, power):
        # Will use the exponentiation by squaring technique to compute powers quickly, i.e. in log2(power) steps.
        if power == 1:
            return Polynom(initDict = self.termsDict, var = self.var)
        elif power == 0:
            return Polynom(var = self.var)
        else:
            current = self
            baseNumber = math.floor(math.log2(power))
            for i in range(baseNumber):
                current = current*current
            residual = self ** (power - 2 **baseNumber)
            return current * residual

    def listify(self):
        retList = []
        for i in range(int(self)+1):
            if i in self.termsDict:
                retList.append(self.termsDict[i])
            else:
                retList.append(0)
        return retList

    def nearest2(self, num):
        return 2**(math.ceil(math.log2(num)))



updatePrecision(100)
p1 = Polynom(initDict = {0:1, 1:1}, var= "x")
print(p1)
hi = p1**10
updatePrecision(5)
print(hi)
