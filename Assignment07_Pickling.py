# -----------------------------------#
#        Title: Pickling             #
#  Created by: Dennis Negron-Rivera  #
#        Date: August 19, 2022       #
#                                    #
# This script will attempt to show   #
# what Pickling is and how it works  #
#                                    #
#          Change Log:               #
# 8/19/22: created by DNR            #
# -----------------------------------#

#Import the Pickle module
import pickle

#Different data types to pickle
intNumber = 64 #The ASCII character for this is '@'
strSentence = "Python is cool"
lstCountries = ["United States", "Canada", "Mexico"]
dctPresidents = {'Washington':1,'Lincoln':16,'FDR':32}

print("I have four data types to pickle: an integer, a string, a list, and a dictionary.\n")
print("Here is the integer: "+str(intNumber))
print("Pickling the integer now...")
fileHandler = open("pickledData.dat","wb")
pickle.dump(intNumber,fileHandler)
print("Pickled the integer")
input("Press enter to pickle the string.")

print("\nHere is the string: "+strSentence)
print("Pickling the string now...")
pickle.dump(strSentence,fileHandler)
print("Pickled the string")
input("Press enter to pickle the list")

print("\nHere is the list: "+str(lstCountries))
print("Pickling the list now...")
pickle.dump(lstCountries,fileHandler)
print("Pickled the list")
input("Press enter to pickle the dictionary")

print("\nHere is the dictionary: "+str(dctPresidents))
print("Pickling the dictionary now...")
pickle.dump(dctPresidents,fileHandler)
print("Pickled the dictionary\n")
fileHandler.close()


input("Press enter to unpickle the contents\n")
fileHandler = open("pickledData.dat","rb")
intUPNumber = pickle.load(fileHandler)
strUPSentence = pickle.load(fileHandler)
lstUPList = pickle.load(fileHandler)
dctUPDct = pickle.load(fileHandler)
print("Here is the unpickled integer: "+str(intUPNumber))
print("Here is the unpickled String: "+strUPSentence)
print("Here is the unpickled list: "+str(lstUPList))
print("Here is the unpickled dictionary: "+str(dctUPDct))
fileHandler.close()

print("\nReview the file on the explorer for the contents.\n")

input("Press enter to exit")
