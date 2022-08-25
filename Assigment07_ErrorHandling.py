# -----------------------------------#
#        Title: Error Handling       #
#  Created by: Dennis Negron-Rivera  #
#        Date: August 19, 2022       #
#                                    #
# This script will attempt to show   #
# various exceptions and how Python  #
# can handle them.                   #
#                                    #
# Assumption: no input validation    #
# except where necessary             #
#                                    #
#          Change Log:               #
# 8/19/22: created by DNR            #
# -----------------------------------#
import math

# Global Variable
lstAirlines = ["American","Delta","United","Southwest","Frontier","Spirit","JetBlue","Alaska"]

def pythonErrorPrint(e):
    print("This is what Python would say:")
    print(e)
    print()
    input("Press enter to continue...\n")

print("Let's run through a few scenarios where exceptions are thrown.\n")
print("Let's start with IndexError and TypeError exceptions.\n")
print("I have a list of major US airlines: ")
print(str(lstAirlines))

index=int(input("Select a number between 0-7: "))
print("You've picked "+lstAirlines[index]+"\n")
index = int(input("Now, select a number outside that range: "))
try:
    print("You've picked "+lstAirlines[index]+"\n")
except IndexError as e:
    print("You picked a number outside the range and triggered an IndexError exception.")
    pythonErrorPrint(e)

try:
    index2 = input("Now enter something other than a number: ")
    print("You've picked "+lstAirlines[index2]+"\n")
except TypeError as e:
    print("By entering something other than a number, you triggered a TypeError exception.")
    pythonErrorPrint(e)

print("Now, let's look at a ZeroDivisionError exception.")
intNum1=int(input("Enter an integer other than zero: "))
intNum2=int(input("Enter another one: "))
print("As it turns out "+str(intNum1)+" divided by "+str(intNum2)+ " is "+str(float(intNum1)/float(intNum2)))
input("But if we make the second number a 0...(press enter)\n")
try:
    fltQuot = intNum1/0
except ZeroDivisionError as e:
    print("We just triggered a ZeroDivisionError by dividing by 0.")
    pythonErrorPrint(e)

print("Here's an example of a ValueError.")
intNum3 = int(input("Enter a positive integer: "))
print("The square root of that number is: "+str(float(math.sqrt(intNum3))))
intNum4 = int(input("Now give me a negative number: "))
try:
    math.sqrt(intNum4)
except ValueError as e:
    print("You tried finding the square root of a negative number, triggering a ValueError exception.")
    pythonErrorPrint(e)

print("Finally, let's look at the IOError.")
fileName = input("What's the filename you want to read from? Don't forget the extension: ")
try:
    fileHandler = open(fileName,"r")
except IOError as e:
    print("Turns out the file doesn't exist and you triggered an IOError exception.")
    pythonErrorPrint(e)

print("All errors handled effectively and the program is allowed to end.")
input("Press enter to exit.")