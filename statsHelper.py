#Hayden Riewe
#github.com/hriewe
#This script gives the user multiple options for computing 
#common statistical formulas

#import needed modules
import sys
import inquirer
import os

#Bubble Sort function to sort the data
def bubbleSort(unsorted):
    for num in range(len(unsorted)-1,0,-1):
        for i in range(num):
          if unsorted[i]>unsorted[i+1]:
            temp = unsorted[i]
            unsorted[i] = unsorted[i+1]
            unsorted[i+1] = temp

#Compute the factorial of x
def factorial(x):
  num = 1
  while x >= 1:
    num = num * x
    x = x - 1
  return num

#Compute poisson
def poisson(lam, x):
  e = 2.71828
  temp = (lam ** x) * (e ** -lam)
  num = factorial(x)
  return temp/num

#Compute binomial
def binomial(n, p, x):
  nCx = factorial(n) / (factorial(x) * (factorial(n-x)))
  nCx = nCx * (p**x)
  return (nCx) * ((1 - p) ** (n-x))

#Home screen
home = [inquirer.List('home', message="Please select a function: ", choices=["List Evaluator", "Poisson Distribution", "Binomial Distribution", "Z-Score"],),]
poissonOptions = [inquirer.List('poisson', message="Please select an option: ", choices=["Single Poisson", "Range Poisson"],),]
binomialOptions = [inquirer.List('binomial', message="Please select an option: ", choices=["Single Binomial", "Range Binomial"],),]
homeSelection = inquirer.prompt(home)

#LIST
if homeSelection['home'] == "List Evaluator":
  os.system('clear')

  #Get list of numbers from user
  numString = input("Please enter the list: ")
  numString = numString.strip("[]()\{\}")
  array = []

  #Split the list at the comma and add it to a python list
  if "," in numString:
    for num in numString.split(','):
      array.append(float(num))
  elif " " in numString:
    for num in numString.split(" "):
      array.append(float(num))
  elif ":" in numString:
    for num in numString.split(":"):
      array.append(float(num))
  else:
    print("Could not split your string, please enter a list seperated by: ',' ':' or a space.")
    sys.exit()

  #Call the bubbleSort function to sort the list
  bubbleSort(array)

  #Print the sorted list to the user on a single line
  print("\nSorted List: ", end=' ')
  for i in range (len(array)):
    print(array[i], end=' ')

  #Find the mean (average) of the list
  total = 0
  for i in range(len(array)):
    total = total + array[i]
  mean = total/len(array)
  print("\nMean: " + str(mean))

  #Find the median of the list
  if len(array) % 2 == 1:
    print("Median: " + str(array[(len(array)-1)//2]))
  else:
    upper = array[len(array) // 2]
    lower = array[(len(array) // 2) - 1]
    print("Median: " + str((upper + lower) / 2))

  #Find the mode of the list
  #I'm sure there is a better way to do this
  mode = 0
  modeOccur = 0
  modeS = ''
  modeDict = dict()
  valuesGreaterThanOne = 0
  for i in range(len(array)):
    modeDict[array[i]] = array.count(array[i])

  for key, value in modeDict.items():
    if value > 1:
      valuesGreaterThanOne += 1
    if value > mode:
      mode = key
      modeOccur = value

  if valuesGreaterThanOne == 0:
    print("There is no mode")
  else:
    for key, value in modeDict.items():
      if value == modeOccur:
        modeS = modeS + str(key) + '  '
    print("Mode(s): " + modeS)

  #Find the variance of the list
  varList = []
  varSum = 0
  for i in range(len(array)):
    varList.append(array[i] - mean)
    varList[i] = varList[i] * varList[i]
    varSum = varSum + varList[i]
    variance = varSum / (len(array) - 1)
  print("Variance: " + str(variance))

  #Find the standard deviation
  print("Standard Deviation: " + str(variance ** 0.5))

#POISSON
if homeSelection['home'] == "Poisson Distribution":
  os.system('clear')
  poissonAnswer = inquirer.prompt(poissonOptions)
  if poissonAnswer['poisson'] == "Single Poisson":
    os.system('clear')
    lam = float(input("Lambda: "))
    x = float(input("x: "))
    poisson = poisson(lam, x)
    print("Poisson: " + str(poisson))
  else:
    os.system('clear')
    lam = float(input("Lambda: "))
    xmin = int(input("x min: "))
    xmax = int(input("x max: "))
    totalPoisson = 0

    for i in range(xmin,xmax+1):
      totalPoisson = totalPoisson + poisson(lam, i)
    print("Poisson: " + str(totalPoisson))

#BINOMIAL
if homeSelection['home'] == "Binomial Distribution":
  os.system('clear')
  binomialAnswer = inquirer.prompt(binomialOptions)
  if binomialAnswer['binomial'] == "Single Binomial":
    os.system('clear')
    n = int(input("n: "))
    p = float(input("p: "))
    x = int(input("x: "))
    if p >= 1:
      p = p/100
    print("Binomial: " + str(binomial(n, p, x)))
  else:
    os.system('clear')
    n = int(input("n: "))
    p = float(input("p: "))
    xmin = int(input("x min: "))
    xmax = int(input("x max: "))
    totalBinomial = 0
    for i in range(xmin, xmax+1):
      totalBinomial = totalBinomial + binomial(n,p,i)
    print("Binomial: " + str(totalBinomial))

#ZSCORE
if homeSelection['home'] == "Z-Score":
  os.system('clear')
  x = float(input("X: "))
  mean = float(input("Mean: "))
  stdev = float(input("Standard deviation: "))
  print("Z-Score: " + str((x-mean)/stdev))

