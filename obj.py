import random
import csv
import functions as fn

class User:

    def __init__(self):
        self.__generateKeys__()

    def __generateKeys__(self, file="primenumbers.csv"):
        with open(file, 'r') as fp:
            file = list(csv.reader(fp))

        p = int(file[random.randint(0,len(file))][0])
        q = int(file[random.randint(0,len(file))][0])

        # try e as random prime as its far more likely to get relative prime to n,phin
        self.public = int(file[random.randint(0,len(file))][0])

        self.n = p * q
        phiN = (p-1) * (q-1)

        # if not just update with other random
        while not fn.relativePrime(self.public, self.n, phiN):
            self.public = int(file[random.randint(0,len(file))][0])

        # generate private key
        self.private = fn.bezout(phiN, self.public)


    def __repr__(self):
        return 'Public: {}\nPrivate: {}'.format(self.public, self.private)

    def __str__(self):
        return 'Public: {}\nPrivate: {}'.format(self.public, self.private)
    
    def encrypt(self, message):
        
        if isinstance(message, str):
            newmessage = [chr(ord(char) ** self.public % self.n) for char in message]
            return ''.join(newmessage)
        return (message ** self.public) % self.n

    def decrypt(self, message):
        if isinstance(message, str):
            newmessage = [chr(ord(char) ** self.private % self.n) for char in message]
            return ''.join(newmessage)
        return (message ** self.private) % self.n



# usr = User()
# message = 'This is a sample message to be encoded'
# print('Message: ', message)
# print('Encrypted: ',usr.encrypt(message))
# print('Decrypted: ',usr.decrypt(usr.encrypt(message)))


