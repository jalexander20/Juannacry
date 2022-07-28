
def lineReaderAndEncrypter(fernetKey, testFileName):
    # Opens the file with read and writing(+) capabilities.
    file1 = open(testFileName, "r+")
    # Reads line by line and puts each line of text from the file into an index of an array
    linesInFile = file1.readlines()
    encryptedLines = []
    # Sets the pointer back to the beginning of the file
    file1.seek(0)
    for currentLine in linesInFile:
        # Encrypts the line in the file. Note: Line must be in bytes to encrypt (.encode)
        encryptedText = fernetKey.encrypt(currentLine.encode())
        # Adds the encrypted line to the array with the rest of the encrypted lines
        encryptedLines.append(encryptedText)
    # Writes all the encrypted lines to the file Note: Lines must be in string format to write to a file
    file1.writelines(str(encryptedLines))
    file1.close()

