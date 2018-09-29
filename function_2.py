import data_holder
import os

#User Input
userInput = raw_input("Enter the name of the file: ")

#CSV file name
Procurement_CSV_File = "government-procurement-via-gebiz.csv"

#file invalid
if not os.path.isfile(Procurement_CSV_File):
    print("File does not exist. Please enter valid file.".format(Procurement_CSV_File))

#Read CSV File
with open('government-procurement-via-gebiz.csv') as key:
    key.readline()
    userInput = key.read()
key.close()

def createFolder():
    test = './new python2/'
    try:
        if not os.path.exists(test):
            os.makedirs(test)
    except OSError:
        print ('Error: Creating directory. ' + test)

agencylist = []

def writetxt():
    for i in agencylist:
        file = open(os.path.join(createFolder(),i+".txt", "w"))
        file.write(i)

        file.close()

def txtdetails():
    agency_to_procurements = data_holder.create_dict_for_list(data_holder.procurements, 'agency')
    for agency in agency_to_procurements:
        agencylist.append(agency)

        file1 = open(completeName, "w")
        toFile = raw_input("Write what you want into the field")

        file1.write(toFile)
        #print the field names
        print ''.join(toFile)

        #print out each column of a row
        for column in row:
            print("", column)

        file1.close()
