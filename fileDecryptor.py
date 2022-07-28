# Imports all the needed functions and classes
from fernetencryption import Fernet
from fileIterator import fileIterator
from decryptScript import lineReaderAndDecrypter

# Opens that file that contains the key and reads the contents of the file into the key variable
keyFile = open("key.txt", "r")
key = keyFile.readline()
keyFile.close()

# Calls the Fernet class and accepts the key as an argument. Key is string spliced because there is left over encoding
# information in the string. The key is then reencoded.
decrypter = Fernet(bytes(key[2:-1], 'utf8'))

# Function gets every file in the directory with the file extension ".txt"
listOfEncryptedTextFiles = fileIterator()
decryptionFileCount = 0

# The lineReaderAndDecrypter function runs for every file in the listOfEncryptedTextFiles array. (Function decrypts the
# file that's passed as an argument
for currentLine in listOfEncryptedTextFiles:
    lineReaderAndDecrypter(decrypter, currentLine)
    decryptionFileCount += 1
print("There were " + str(decryptionFileCount) + " files decrypted. Thank you for your business!")

