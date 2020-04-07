from timeit import default_timer as timer
test=1000000

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def is_prime(n):
    #if n <=1: return False
    #if n <=3: return True
    #elif n%2 ==0 or n%3 == 0: return False
    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) ==0: return False
        i = i + 6
    return True

def primes_to_old(n):
    div_vals = [x for x in range(3,int(n**.5)+1,2) if is_prime(x)]
    scope = range(3,n,2)
    return [2] + [i for i in scope if not 0 in [i%y for y in div_vals if y != i]]

def primes_to(n):
    return [2,3]+[x for x in range(3,n,2) if is_prime(x) and x%3 != 0]



start = timer()
print(primes_to(test))
end = timer()
print (end - start)


start = timer()
print (sieve_for_primes_to(test))
end = timer()
print (end - start)

