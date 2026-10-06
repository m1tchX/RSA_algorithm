import math
import cryptomath

def isPrimeTrialDiv(num):
    '''Проверка на простоту методом пробного деления (для небольших чисел).'''
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


rabinMiller = cryptomath.is_prime
generateLargePrime = cryptomath.generateLargePrime