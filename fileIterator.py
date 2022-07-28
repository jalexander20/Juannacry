# Function is used to get all the text file names in the directory that the program is in.
import os


def fileIterator():
    # Gets the name of all the files in the directory
    listOfFiles = os.listdir()
    filesToEncrypt = []
    # Looks at each file name. If the file name ends with doesn't end with ".txt" and isn't the key file,
    # then the name of the file is added to the filesToEncrypt array.
    for currentFile in listOfFiles:
        if currentFile.endswith(".txt"):
            if currentFile == "key.txt":
                continue
            else:
                filesToEncrypt.append(currentFile)
    # returns the filesToEncrypt array
    return filesToEncrypt

