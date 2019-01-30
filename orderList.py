#Hayden Riewe
#github.com/hriewe
#This script will order a string of numbers and then
#calculate the mean, median, mode, variance, and stddev

#import needed modules
import sys

#Bubble Sort function to sort the data
def bubbleSort(unsorted):
    for num in range(len(unsorted)-1,0,-1):
        for i in range(num):
          if unsorted[i]>unsorted[i+1]:
            temp = unsorted[i]
            unsorted[i] = unsorted[i+1]
            unsorted[i+1] = temp

#Get list of numbers from user
numString = input("Please enter the list, delimited by your cli argument: ")
numString = numString.strip("[]()\{\}")
array = []

#Split the list at the comma and add it to a python list
if sys.argv[1] == ",":
  for num in numString.split(','):
    array.append(int(num))
elif sys.argv[1] == " ":
  for num in numString.split(" "):
    array.append(int(num))
elif sys.argv[1] == ":":
  for num in numString.split(":"):
    array.append(int(num))
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