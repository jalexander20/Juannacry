# Function decrypts any file that is passed to it as long as the key is the same key used to encrypt it
# (Symmetric Encryption)
def lineReaderAndDecrypter(fernetKey, testFileName):
    # Opens and reads the lines of the file that is being decrypted
    fileToBeDecrypted = open(testFileName, "r+")
    encryptedLines = fileToBeDecrypted.readlines()
    # Splits each element up by where the "," is into a separate elements in an array
    joinedLines = ",".join(encryptedLines).split(",")

    # Sets the cursor in the program to the beginning
    fileToBeDecrypted.seek(0)
    # For each line in the array, the program decrypts the line and writes it to the document.
    for currentLine in joinedLines:
        # currentLine had to be reencoded to pass through the .decrypt function. String splicing was used to get rid
        # of some extra characters left over after reading the file into the encryptedLines variable
        decryptedText = fernetKey.decrypt((bytes(currentLine[2:-1], 'utf8')))
        # writes the decrypted text to the file. String splicing is used to get rid of some of the encoding
        # characters
        fileToBeDecrypted.write(str(decryptedText)[2:-3])
        # Moves onto the next line
        fileToBeDecrypted.write("\n")

    # Adds another line so that the last character doesn't get cut off during encryption
    fileToBeDecrypted.write("\n")
    # Removes the encrypted lines that are still present.
    fileToBeDecrypted.truncate()
    # Closes the file
    fileToBeDecrypted.close()
