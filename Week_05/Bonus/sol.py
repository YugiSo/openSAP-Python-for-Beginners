# Week 5 - Bonus Assignment


def isprime(num: int) -> bool:
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    else:    
        return True


def prime_list(num: int) -> list:
    return [] if (num < 2) else [i for i in range(2, num + 1) if isprime(i)]


num = int(input('Up to which number do you want all prime numbers: '))
print(prime_list(num))