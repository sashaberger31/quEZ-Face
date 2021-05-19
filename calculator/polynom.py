import math
import cmath
from fourier import *

class Polynom:
  """
  A class to capture the algebraic behavior of the polynomials.
  """
  def __init__(self, initDict = dict(), var = "x"):
    if initDict:
      self.termsDict = initDict
    else:
      self.termsDict = dict({0:1})
    self.var = var
    
  def __int__ (self):
    return max([power for power in self.termsDict.keys()])

  def __str__ (self):
    outStr = ""
    for i in range(int(self)+1):
      if i in self.termsDict:
        outStr += "(" + str(self.termsDict[i]) + ")" + self.var + "^" + str(i) + " + "
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
    print(pointwiseProd)
    print(inverted)
    return Polynom(initDict = inverted, var = self.var)

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


# Test Code
p1 = Polynom(initDict = {0:1, 1: 1, 2: 2}, var= "x")
p2 = Polynom(initDict = {0:2, 1: 5, 2: -2}, var = "x")
print(p1)
print(p2)
print(p1*p2)