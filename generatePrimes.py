import functions as fn
import obj
import random
import csv


def addPrimes(file):
    with open(file, 'r') as fp:
        pass


def write():
    with open('primenumbers.csv', 'w') as fp:
        file = csv.writer(fp)
        data = [x for x in range(100,999) if fn.isPrime(x)]
        for line in data:
            file.writerow([line])
    

def read():
    with open('primenumbers.csv', 'r') as fp:
        file = csv.reader(fp)
        for line in file:
            print(line)


def generatePrimes():
    # for i in range(10):
    #     print('{} is prime: {}'.format(i,fn.isPrime(i)))
    with open('primenumbers.csv', 'r') as fp:
        file = list(csv.reader(fp))
        p = int(file[random.randint(0,len(file))][0])
        q = int(file[random.randint(0,len(file))][0])

    wallet = obj.keyPair(p,q)
    print(wallet)

def test():
    print(fn.GCD(208,4))


if __name__ == '__main__':
    test()