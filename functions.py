def isPrime(num):
    if num > 1:
    
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
    
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
        else:
            return True
    
    else:
        return False

def GCD(a, b):
    # Euclids algorithm

    b, a = sorted([a,b])
    if a % b == 0:
        return b

    minterms = [(a // b)]
    minterm = minterms[0] 
    remainder = a - (minterm * b)
    while a % remainder != 0:
        a = b
        b = remainder
        minterm = a // b
        remainder = a - (minterm * b)
        minterms.append(minterm)

    class pair:
        minterms = minterms
        remainder = remainder

        def __repr__(self):
            return "remainder: {}\nminterms {}".format(self.remainder, self.minterms)

        def __str__(self):
            return "remainder: {}\nminterms {}".format(self.remainder, self.minterms)
        
    return pair()


    







