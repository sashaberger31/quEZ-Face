# Main file for quEZ-Face

import math

# q-Library
class qSeries:
  def __init__(self, initDict  = None):
    self.termsDict = dict()
    if initDict:
      for power, coeff in initDict.items():
        self.termsDict[power] = coeff

  def qDeg():
    return max([power for power in self.termsDict.keys()])
    
  def qMultiply(self, q2):
    # q2 is the other qSeries instance to multiply by
    newDict = dict()
    for power1, coeff1 in self.termsDict.items():
      for power2, coeff2 in q2.termsDict.items():
        if power1+power2 in newDict:
          newDict[power1+power2] += coeff1*coeff2
        else:
          newDict[power1+power2] = coeff1*coeff2
    return qSeries(initDict = newDict)

  def qAdd(self, q2):
    newDict = self.termsDict
    # Do the addition
    for power, coeff in q2.termsDict.items():
      if power in newDict:
        newDict[power]+= coeff
      else:
        newDict[power] = coeff
    return qSeries(initDict = newDict)
  
  def qChop(self, n):
    newDict = dict()
    
    for k in range(1,n+1):
      if k in self.termsDict:
        newDict[k] = self.termsDict[k]
    return qSeries(initDict = newDict)
  
  def qPow(self, k, n):
    current = self
    for i in range(k-1):
      current = current.qMultiply(self).qChop(n)
    return current
  
  # def qPow(self, k, n):
  #   n = sum
  #     current = current.qMultiply(self)
  #   return current
    



q1 = qSeries(initDict= {0:1, 1:2, 2:3})
q2 = qSeries(initDict = {0:1, 2:5, 4:7})

print(q1.add(q2).termsDict)

def qMZV(sList, n):
  depth = len(sList)

  buffer = 0
  for j in range(1, depth+1):
    buffer += kList[j]*(sList)
  currentProd = qSeries(initDict = {:1 })
  for j in range(1, len(sList)+1):
    currentProd.qMultiply(geo(kList[j], n).qPow(sList[j], n))

  
def geo(k, n):
  # chop at n
  # 1/(1-q^k) = Σ_{i>-1} q^ki = \sum\limits_{i\ge 0} q^{ki}
  newDict = dict()
  for i in range(n//k+1):
    newDict[i*k] = 1
  return qSeries(initDict = newDict)


def multinom(kList):
  n = sum(kList)
  
  ans = math.factorial(n)
  for k in kList:
    ans /= math.factorial(k)
  
  return ans
  

"""
def qMZV(s):
"""