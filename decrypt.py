import pyAesCrypt

password = input('Password: ')

#encrypt
#pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

#decypt
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)
