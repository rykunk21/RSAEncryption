import functions as fn
import obj
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
    wallet = obj.User()
    print(wallet)

def test():
    print(fn.relativePrime(13,26,6))


if __name__ == '__main__':
    test()