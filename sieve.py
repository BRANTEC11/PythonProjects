import math
def sieve(y):
    n = y+1
    is_prime = []
    ii = 0
    i = 0
    while ii < n:
        if ii < 2:
            is_prime.append(False)
        else:
            is_prime.append(True)
        ii = ii + 1
    while i <= math.sqrt(y):
        
        if is_prime[i] == True:
            j = i*i
            while j <= y:
                is_prime[j] = False
                j = j + i 
        i = i+1
    is_true_prime = []

    
    for x in range(len(is_prime)):
        if is_prime[x] == True:
            is_true_prime.append(x)
    




            
    print("Number of primes found: " + str(len(is_true_prime)))
    print(is_true_prime)
