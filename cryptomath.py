import random

def gcd(a, b):
    '''Возвращает НОД, используя алгоритм Евклида.'''
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    '''Возвращает x — обратный по модулю m элемент к a (a * x ≡ 1 mod m).'''
    if gcd(a, m) != 1:
        return None  # Обратного элемента не существует

    # Вычисление с помощью расширенного алгоритма Евклида:
    u1, u2, u3 = a, 1, 0
    v1, v2, v3 = m, 0, 1
    while v1 != 0:
        q = u1 // v1
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u2 % m


def is_prime(n, k=40):
    '''Тест Миллера-Рабина на простоту.'''
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Разложение n - 1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generateLargePrime(keySize):
    '''Генерирует случайное простое число заданной битности.'''
    while True:
        num = random.getrandbits(keySize)
        # Устанавливаем старший бит (чтобы число было нужной длины)
        # и младший бит (чтобы число было нечетным)
        num |= (1 << (keySize - 1)) | 1
        if is_prime(num):
            return num