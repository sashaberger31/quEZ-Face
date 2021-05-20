import math
import cmath
from fourier import *

class Polynom:
  """
  A class to capture the algebraic behavior of the polynomials.
  """
  def __init__(self, initDict = dict(), var = "x", resolution = 10e-9):
    if initDict:
      self.termsDict = initDict
    else:
      self.termsDict = dict({0:1})
    self.var = var
    self.resolution = resolution

    toCull = []
    for power, coeff in self.termsDict.items():
      if abs(coeff) < resolution:
        toCull.append(power)
      elif abs(complex(coeff).imag) < resolution:
        self.termsDict[power] = complex(coeff).real
      elif abs(complex(coeff).real) < resolution:
        self.termsDict[power] = 0+complex(coeff).imag*1j
    for power in toCull:
      del self.termsDict[power]
  
  def __int__ (self):
    return max([power for power in self.termsDict.keys()])

  def __str__ (self):
    outStr = ""
    for i in range(int(self)+1):
      if i in self.termsDict:
        outStr += str(self.termsDict[i]) + self.var + "^" + str(i) + " + "
    return outStr[:-3]
      
  def __add__ (self, other):
    newDict = self.termsDict
    for power in other.termsDict.keys():
      if power in newDict:
        newDict[power] += other.termsDict[power]
      else:
        newDict[power] = other.termsDict[power]
    return Polynom(initDict= newDict, var = self.var, resolution = self.resolution)

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
    return Polynom(initDict = inverted, var = self.var, resolution = self.resolution)

  def __pow__(self, power):
    # Will use the exponentiation by squaring technique to compute powers quickly, i.e. in log2(power) steps.
    if power == 1:
      return Polynom(initDict = self.termsDict, var = self.var, resolution = self.resolution)
    elif power == 0:
      return Polynom(var = self.var, resolution = self.resolution)
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




p1 = Polynom(initDict = {0:1, 1:1}, var= "x")

print(p1**1000)
