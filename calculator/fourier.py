import cmath
import math

def RecursiveDFT(aList, pow):
  """
  RECURSIVE FOURIER FUNCTION:
  
  Parameters: 
    aList - a dict of complex numbers to transform (keys are the indices). Must have size 2^k
    pow - sign of exponent of e to be used in the transform
  Returns:
    a dictionary of complex numbers (keys are the indices) of size 2^k
  """
  n = len(aList)

  if n == 1: # Base case
    return aList
  else: # Recursive step
    omega = 1
    omega_n = cmath.rect(1, pow*2*math.pi/n)
    aEven = [aList[2*n] for n in range(math.floor(n//2))]
    aOdd = [aList[2*n+1] for n in range(math.floor(n//2))]
    aEvenTransform = RecursiveDFT(aEven, -1)
    aOddTransform = RecursiveDFT(aOdd, -1)
    aTransform = dict()
    for k in range(n//2):
      aTransform[k] = aEvenTransform[k] + omega*aOddTransform[k]
      aTransform[k+n//2] = aEvenTransform[k] - omega*aOddTransform[k]
      omega = omega*omega_n
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

