#Anthony Barnes
#Grade Analyzer 4th Assignment
#Code Grade Analyzer
#11/2/24

# Variables
sName1 = "Louis"
sName2 = "Kady"
var = "iTest1 == iTest2 == iTest3 == iTest4"
sDropLowGrd = str
fAverage = float
fLowest = float
sGradeNum = str
sName = "sName1 == sName1 and sName2 == sName2"

# Input that is needed to get results

sName = input("Name of person that we are calculating the grades for: ")


iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("Test 4: "))

sDropLowGrd = input("Do you wish to Drop the Lowest Grade Y or N? ")

# Check test scores to make sure they are valid.
# It will calculate each test with less than equal to make sure the number is higher then 0


if iTest1 <= 0 or iTest2 <= 0 or iTest3 <= 0 or iTest4 <= 0:
           raise SystemExit("Test scores must be greater then 0.")


#Calculation
#It will compute which test is the lowest by using Test1,2,3,4 till it find Lowest number.

if sDropLowGrd != 'Y' and sDropLowGrd != 'N':

    raise SystemExit("Enter Y or N to Drop the Lowest Grade.")

    if  iTest1 < iTest2  and iTest1 < iTest3 and iTest1 < iTest4:
         fLowest = iTest1
    elif iTest2 < iTest1 and iTest2 < iTest3 and iTest2 < iTest4:
        fLowest = iTest2
    elif iTest3 < iTest1 and iTest3 < iTest2 and iTest3 < iTest4:
        fLowest = iTest3
else:
    fLowest = iTest4

#Calculation
#It will determine the lowest and average from all the test.

if sDropLowGrd == 'Y':
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4 - fLowest) / 3
else:
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4

# Determine Letter Grade from the average

if fAverage >= 97.0:
    sGradeNum = "A+"
elif fAverage >= 94.0:
  sGradeNum = "A"
elif fAverage >= 90.0:
  sGradeNum = "A-"
elif fAverage >= 87.0:
  sGradeNum = "B+"
elif fAverage >= 84.0:
  sGradeNum = "B"
elif fAverage >= 80.0:
  sGradeNum = "B-"
elif fAverage >= 77.0:
  sGradeNum = "C+"
elif fAverage >= 74.0:
  sGradeNum = "C"
elif fAverage >= 70.0:
  sGradeNum = "C-"
elif fAverage >= 67.0:
  sGradeNum = "D+"
elif fAverage >= 64.0:
  sGradeNum = "D"
elif fAverage >= 60.0:
  sGradeNum = "D-"
else:
    sGradeNum = "F"

#Output the persons grade and there average

print(f"{sName} test average is: {fAverage:.1f}")
print(f"Letter Grade for the test is: {sGradeNum}")

