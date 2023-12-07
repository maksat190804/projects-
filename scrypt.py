import pyAesCrypt 

password = input('Введите пароль для шифрования файла: ')

#encrypt 
# pyAesCrypt.encryptFile('lolo.txt', 'lolo.txt.a', password)

# decrypt 
pyAesCrypt.decryptFile('lolo.txt.a', 'loloout.txt', password )