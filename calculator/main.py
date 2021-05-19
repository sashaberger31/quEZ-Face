# Main file for quEZ-Face
import math
import cmath

# q-Library
class qSeries:
  def __init__(self, initDict  = None):
    """
    Purpose: Initialize the q-series instance 
    Parameters: initDict - which is a dictionary with keys that are powers and values that are the coefficient of that power
    """
    self.termsDict = dict()
    if initDict:
      for power, coeff in initDict.items():
        self.termsDict[power] = coeff

  def qDeg(self):
    """
    Get the degree of a q-polynomial.
    """
    return max([power for power in self.termsDict.keys()])
    
  def qMultiply(self, q2, n):
    """
    Multiply two q-series and return a third, rounded to a maximum degree of n.
    """
    newDict = dict()
    for power1, coeff1 in self.termsDict.items():
      for power2, coeff2 in q2.termsDict.items():
        if power1+power2 in newDict:
          newDict[power1+power2] += coeff1*coeff2
        elif power1+power2 <= n:
          newDict[power1+power2] = coeff1*coeff2
    return qSeries(initDict = newDict)

  def __add__(self, q2, n):
    """
    Add two q-series and return a third, rounded to a maximum degree of n. 
    """
    newDict = self.qChop(n).termsDict
    # Do the addition
    for power, coeff in q2.termsDict.items():
      if power in newDict:
        newDict[power]+= coeff
      elif power <= n:
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
      current = current.qMultiply(self, n)
    return current

  def qDump(self):
    for i in range(self.qDeg() +1):
      if i in self.termsDict:
        print("q^%d: %d" % (i, self.termsDict[i]))



def qMZVPrimeUnmaxed(sList, m, n):
  # \sum\limits_{m>k_1>\cdots > k_d} stuff 
  # qMZV(sList, m, n) = \sum\limits_{k_1 = 1}^m *q^{k_1(s_1-1)} * geo(k1, n)^s_1 qMZV(sList[1:], k_1, n)
  finalMZV = qSeries(initDict = dict())

  if not sList:
    return qSeries(initDict = {0:1})
  for k_1 in range(1, m):
    qGeoGarbage = geo(k_1, n).qPow(sList[0], n)
    qMZVPrimeSmaller = qMZVPrimeUnmaxed(sList[1:], k_1, n)
    qAddedMZV = qMZVPrimeSmaller.qMultiply(qGeoGarbage, n).qMultiply(qSeries(initDict = {k_1*(sList[0]-1):1}), n)

    finalMZV = finalMZV.qAdd(qAddedMZV, n)
  
  return finalMZV


def qMZVPrime(sList, n): 
  longSum = qMZV()
  d = len(sList)
       longSum += (sList[i]-1) * (d-i)

  m = math.ceil((n - longSum)/(sList[0]-1))+1
  return qMZVPrimeUnmaxed(sList, m, n)

def sigma(sList, n):
  initBuffer = qSeries(initDict = {0:1})
  for i in range(len(sList))
    initBuffer = initBuffer.add(sigma(sList[1:], n-1))



def oSum (sList, n)  
  oSum = qMZV(sList) 
  l = len(sList)
  for i in range (1,l)
    oSum = oSum.qAdd(qMZVPrime(sList, n), n)
   return oSum 


def geo(k, n):
  # chop at n
  # 1/(1-q^k) = Σ_{i>-1} q^ki = \sum\limits_{i\ge 0} q^{ki}
  newDict = dict()
  for i in range(n//k+1):
    newDict[i*k] = 1
  return qSeries(initDict = newDict)

def KanekoYamamoto(k, sList, nMax, chop, qBuffer):
  


def multinom(kList):
  n = sum(kList)
  
  ans = math.factorial(n)
  for k in kList:
    ans /= math.factorial(k)
  
  return ans

class Polynom:
  """
  A class to capture the algebraic behavior of the polynomials 
  produced by the regularized (alternating) multiple zeta values.
  """
  def __init__(self, initDict = dict()):
    if initDict:
      self.termsDict = initDict
    else:
      self.termsDict = dict({0:1})
    
  def __int__ (self):
    return max([power for power in self.termsDict.keys()])
  
  def __add__ (self, other):
    newDict = self.termsDict
    for power in other.termsDict.keys():
      if power in newDict:
        newDict[power] += other.termsDict[power]
      else:
        newDict[power] = other.termsDict[power]
    return Polynom(power)
  
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

  def __str__(self, other):


"""
FAST FOURIER TRANSFORM IMPLEMENTATION
"""

def RecursiveDFT(n, aList = [])
  if n == 1:
    return aList
  omega = 1
  omega_n = cmath.rect(1, 2*math.pi/n)
  aEven = [aList[2n] for n in range(math.floor((n-2)/2))]
  aOdd = [aList[2n+1] for n in range(math.floor((n-2)/2))]
  aEvenTransform = RecursiveDFT(n/2, aEven)
  aOddTransform = RecursiveDFT(n/2, aOdd)
  aTransform = []
  for k in range(n/2):
    aTransform[k] = aEvenTransform[k] + omega*aOddTransform[k]
    aTransform[k+n/2] = aEvenTransform[k] - omega*aOddTransform[k]
    omega = omega*omega_n
  return aTransform
  
















print("Result 1")
#qMZVPrime([4,3], 11).qAdd(qMZVPrime([4,3], 11), 11).qAdd(qMZVPrime([4,3], 11), 11).qAdd(qMZVPrime([4,3], 11), 11).qAdd(qMZVPrime([3,4], 11), 11).qAdd(qMZVPrime([3,4], 11), 11).qAdd(qMZVPrime([3,4], 11), 11).qAdd(qMZVPrime([5,2], 11), 11).qDump()
print("Result 2")
#qMZVPrime([3,2,2], 11).qAdd(qMZVPrime([3,3,1], 11), 11).qAdd(qMZVPrime([4,2,1],11), 11).qAdd(qMZVPrime([2,1,4],11), 11).qAdd(qMZVPrime([2,2,3],11), 11).qAdd(qMZVPrime([3,1,3],11), 11).qAdd(qMZVPrime([3,2,2],11), 11).qAdd(qMZVPrime([2,4,1],7), 11).qAdd(qMZVPrime([3,3,1],11), 11).qDump()
print("quEZ-Face is my bestie:")
"""
i screwed up, they didn't match

qMZVPrime([s,l,i,s,t,numbers,go,here], max exponent)

AAA.qMultiply(BBB, maxExponent) = AAA * BBB
AAA.qAdd(BBB, maxExponent) = AAA + BBB
AAA.qPow(exponent, maxExponent) = AAA^exponent

AAA.qDump() = print the stuff into the console nicely

################################################
q1 = -1 + q + 5q^2 - 4q^4 +6 q^5
q2 = 2 + q^2 - 5q^3 + 7q^4
qproduct = -2 + 2q + 9q^2 + 6q^3 -15q^4 -6q^5 + 31q^6 + 26q^7, i hope
qProductSasha = {0: -2, 2: 9, 3: 6, 4: -15, 1: 2, 5: -6, 6: 31, 7: 26}
qsum = 1 + q + 6q^2 - 5q^3 +3q^4 + 6q^5

q1^4 = q(1^4)= q1 = 1 - 4 q - 14 q^2 + 56 q^3 + 107 q^4 - 352 q^5 - 470 q^6 + 1252 q^7
































"""