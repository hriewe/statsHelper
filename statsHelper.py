#Hayden Riewe
#github.com/hriewe
#This script will order a string of numbers and then
#calculate the mean, median, mode, variance, and stddev

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

home = [inquirer.List('home', message="Please select a function: ", choices=["List Evaluator", "Poisson Distribution", "Binomial Distribution"],),]
poissonOptions = [inquirer.List('poisson', message="Please select an option: ", choices=["Single Poisson", "Range Poisson"],),]
homeSelection = inquirer.prompt(home)

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

if homeSelection['home'] == "Poisson Distribution":
  os.system('clear')
  poissonAnswer = inquirer.prompt(poissonOptions)
  if poissonAnswer['poisson'] == "Single Poisson":
    os.system('clear')
    lam = float(input("Lambda: "))
    x = float(input("x: "))
    e = 2.71828

    temp = (lam ** x) * (e ** -lam)
    num = 1
    while x >= 1:
      num = num * x
      x = x - 1
    poisson = temp/num
    print("Poisson: " + str(poisson))
  else:
    os.system('clear')
    lam = float(input("Lambda: "))
    xmin = int(input("x min: "))
    xmax = int(input("x max: "))
    e = 2.71828
    totalPoisson = 0

    for i in range(xmin,xmax+1):
      temp = (lam ** i) * (e ** -lam)
      num = 1
      while i >= 1:
        num = num * i
        i = i - 1
      totalPoisson = totalPoisson + temp/num
    print("Poisson: " + str(totalPoisson))

if homeSelection['home'] == "Binomial Distribution":
  print("work in progress")
  sys.exit()