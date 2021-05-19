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
    for i in range(int(self)):
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
    return Polynom(power, self.var)

  def __mult__(self, other):
    selfEval = 
  def __mult__(self,other):
    newDict = dict()
    for power1, coeff1 in self.termsDict.items():
      for power2, coeff2 in q2.termsDict.items():
        if power1+power2 in newDict:
          newDict[power1+power2] += coeff1*coeff2
        elif power1+power2 <= n:
          newDict[power1+power2] = coeff1*coeff2
    return Polynom(initDict = newDict)
  
  def __pow__

  def listify(self):
    retList = []
    for i in range(int(self)):
      if i in self.termsDict:
        retList.append(self.termsDict[i])
      else: 
        retList.append(0)
    return retList
