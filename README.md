# Pysqlitecrypto-RSA

Pysqlitecrypto-RSA is a Python package that provides functionalities for RSA key generation, encryption, and decryption using SQLite storage.

## Installation

To install Pysqlitecrypto-RSA, you can use pip:

```bash
pip install Pysqlitecrypto-RSA
```

Make sure you have Python 3.x installed.

## Usage

You can use Pysqlitecrypto-RSA in your Python projects by importing the necessary functions:

```python
from pysqlitecrypto_rsa import generate_keys, encrypt_message, decrypt_message

# Generate RSA keys with a specified key size
generate_keys(1024)

# Encrypt a message
encrypted_message = encrypt_message("Your message here")

# Decrypt the encrypted message
decrypted_message = decrypt_message(encrypted_message)
```

### Note:
- The `generate_keys` function requires the key size to be passed as an argument. For example, `generate_keys(1024)` generates RSA keys with a key size of 1024 bits.

## License

Pysqlitecrypto-RSA is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
