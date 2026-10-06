import cryptomath

def main():
    print("=== Демонстрация работы алгоритма RSA ===")

    p = int(input('Введите первое простое число p: '))
    q = int(input('Введите второе простое число q: '))

    if not (cryptomath.is_prime(p) and cryptomath.is_prime(q)):
        print("ПРЕДУПРЕЖДЕНИЕ: одно или оба из введенных чисел не являются простыми!")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Используем e = 65537, либо фоллбэк для очень маленьких p и q
    e = 65537
    if cryptomath.gcd(e, phi) != 1:
        e = 3
        while cryptomath.gcd(e, phi) != 1 and e < phi:
            e += 2

    d = cryptomath.findModInverse(e, phi)

    print(f'\nВычисленный модуль n = p * q: {n}')
    print(f'Функция Эйлера phi(n): {phi}')
    print(f'Открытый ключ  (n, e): ({n}, {e})')
    print(f'Закрытый ключ (n, d): ({n}, {d})')

    x = int(input(f'\nВведите число x для шифрования (0 <= x < {n}): '))
    if x >= n or x < 0:
        print(f"ОШИБКА: число x должно удовлетворять условию 0 <= x < n ({n})!")
        return

    # Шифрование: c = x^e mod n
    encrypted_x = pow(x, e, n)
    print(f'Зашифрованное сообщение (c): {encrypted_x}')

    # Расшифрование: m = c^d mod n
    decrypted_x = pow(encrypted_x, d, n)
    print(f'Расшифрованное сообщение (m): {decrypted_x}')

    if x == decrypted_x:
        print("УСПЕХ: расшифрованное сообщение совпадает с исходным!")
    else:
        print("ОШИБКА: расшифрованное сообщение не совпадает с исходным!")


if __name__ == '__main__':
    main()