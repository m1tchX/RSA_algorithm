# Software Implementation and Testing of the RSA Asymmetric Encryption Algorithm

This project is a coursework focused on the study, software implementation, and performance testing of the **RSA** asymmetric encryption algorithm in Python.

---

## 📌 Implementation Features

- **Mathematical Core (`cryptomath.py`, `primeNum.py`):**
  - Euclidean algorithm for greatest common divisor ($\text{GCD}$).
  - Extended Euclidean algorithm for modular multiplicative inverse ($d \equiv e^{-1} \pmod{\phi(n)}$).
  - Probabilistic Miller-Rabin primality test for high-bit prime validation.
  - Generation of random prime numbers of specified bit length (up to 2048 bits per number).

- **Public Exponent Selection ($e = 65537$):**
  - The test module `RSA_testing.py` fixes $e = 65537$ ($2^{16} + 1$, the fourth Fermat number $F_4$) as the public exponent.
  - This is an industry standard in cryptography (X.509, PKCS#1, TLS/SSL) providing resilience against Manasse and low-exponent attacks, while optimizing encryption operations via binary exponentiation ($10000000000000001_2$ requires only 17 operations).

- **Key Generation (`makePublicPrivateKeys.py`):**
  - Automated generation of a key pair for a given bit length ($n = p \cdot q$).
  - Saving keys to text files (`*_pubkey.txt`, `*_privkey.txt`).

- **Console Demonstration (`RSA_simple.py`):**
  - A simple interactive script for straightforward encryption and decryption of user numbers $x$ given $p$ and $q$.

- **Benchmarking & Testing (`RSA_testing.py`):**
  - Measurement of encryption, decryption, and full-cycle execution times for various key lengths: **512, 1024, 2048, and 4096 bits**.

---

## 📁 Project Structure

```text
RSA_algorithm/
├── cryptomath.py            # Core mathematical functions (GCD, mod inverse, Miller-Rabin)
├── primeNum.py              # Auxiliary prime number generation module
├── makePublicPrivateKeys.py # Public/private key pair generation with file output
├── RSA_simple.py            # Interactive demonstration script
├── RSA_testing.py           # Load testing and performance benchmarking
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

---

## 🚀 Getting Started and Usage

The project requires only a **Python 3.x** interpreter (no external libraries needed).

### 1. Interactive RSA Demonstration
Run the script for manual entry of prime numbers and encryption of number $x$:
```bash
python RSA_simple.py
```

### 2. Key File Generation
The script will generate keys of the specified bit length and save them to `user_pubkey.txt` and `user_privkey.txt`:
```bash
python makePublicPrivateKeys.py
```

### 3. Running Performance Benchmarks
The script will run a series of tests for modulus $n$ sizes of 512, 1024, 2048, and 4096 bits and output average encryption/decryption times:
```bash
python RSA_testing.py
```

Example test output:
```text
Running tests (5 trials per key size)...
n Bits     | Avg. Encrypt (s)   | Avg. Decrypt (s)   | Avg. Cycle (s) 
---------------------------------------------------------------------------
512        | 0.000013           | 0.000455           | 0.000468       
1024       | 0.000033           | 0.002306           | 0.002340       
2048       | 0.000117           | 0.016834           | 0.016951       
4096       | 0.000419           | 0.119010           | 0.119428       
```
