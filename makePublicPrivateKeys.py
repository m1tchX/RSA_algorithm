import os
import sys
import random
import cryptomath

def generateKey(keySize=1024):
    '''Генерирует парные ключи заданного размера модуля n (в битах).'''
    pq_size = keySize // 2

    # 1. Генерируем два больших простых числа p и q
    p = cryptomath.generateLargePrime(pq_size)
    q = cryptomath.generateLargePrime(pq_size)
    while p == q:
        q = cryptomath.generateLargePrime(pq_size)

    n = p * q
    phi = (p - 1) * (q - 1)

    # 2. Открытая экспонента e = 65537 (стандарт)
    e = 65537
    if cryptomath.gcd(e, phi) != 1:
        while True:
            e = random.randrange(3, phi, 2)
            if cryptomath.gcd(e, phi) == 1:
                break

    # 3. Вычисляем закрытую экспоненту d
    d = cryptomath.findModInverse(e, phi)

    publicKey = (n, e)
    privateKey = (n, d)

    print('Открытый ключ (n, e):', publicKey)
    print('Закрытый ключ (n, d):', privateKey)

    return publicKey, privateKey


def makeKeyFiles(name, keySize=1024):
    '''Создает файлы 'name_pubkey.txt' и 'name_privkey.txt' с записанными ключами.'''
    pub_filename = f'{name}_pubkey.txt'
    priv_filename = f'{name}_privkey.txt'

    if os.path.exists(pub_filename) or os.path.exists(priv_filename):
        sys.exit(f'ОШИБКА: Файл {pub_filename} или {priv_filename} уже существует!')

    publicKey, privateKey = generateKey(keySize)

    print(f'\nЗапись открытого ключа в файл {pub_filename}...')
    with open(pub_filename, 'w', encoding='utf-8') as file:
        file.write(f'{keySize},{publicKey[0]},{publicKey[1]}')

    print(f'Запись закрытого ключа в файл {priv_filename}...')
    with open(priv_filename, 'w', encoding='utf-8') as file:
        file.write(f'{keySize},{privateKey[0]},{privateKey[1]}')


def main():
    print('Создание файлов ключей RSA (размер модуля n = 1024 бит)...')
    makeKeyFiles('user', 1024)
    print('Файлы ключей успешно созданы.')


if __name__ == '__main__':
    main()