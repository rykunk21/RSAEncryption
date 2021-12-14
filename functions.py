def isPrime(num):
    if num > 1:
    
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
    
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def GCD(a, b):
    while(b):
        a, b = b, a % b
    return a

def relativePrime(val1, *args):
    for val in args:
        if GCD(val1, val) != 1:
            return False
    return True
      
def bezout(phiN, e):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = e; old_r = phiN

    while r != 0:
        quotient = old_r//r # In Python, // operator performs integer or floored division
        # This is a pythonic way to swap numbers
        # See the same part in C++ implementation below to know more
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t

    if old_t < 0:
        return phiN + old_t
    else:
        return old_t






