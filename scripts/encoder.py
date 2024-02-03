import os
import sys

DECIMANS = 18

def generate_random_bytes(size: int):
    return os.urandom(size)

def encrypt(pool: str, amount: float, key: bytes) -> bytes:
    amount_int = int(amount * (10 ** DECIMANS))
    amount_size = sys.getsizeof(amount_int) - 24
    amount_bytes = amount_int.to_bytes(amount_size, byteorder="big", signed=False)
    pool_bytes = bytes.fromhex(pool[2:])
    
    result = bytearray()
    for i in range(20):
        result.append(key[i] ^ pool_bytes[i])
    for i in range(amount_size):
        result.append(key[i + 20] ^ amount_bytes[i])
    return bytes(result) + key[:len(pool_bytes) + amount_size]

def decrypt(data: bytes) -> tuple[str, float]:
    key_len = len(data) // 2
    
    address_int = 0
    for i in range(20):
        address_int = (address_int << 8) + (data[i] ^ data[i + key_len])
    address = f"0x{address_int:x}"

    amount_int = 0
    for i in range(20, key_len):
        amount_int = (amount_int << 8) + (data[i] ^ data[i + key_len])
    amount = (amount_int / (10 ** DECIMANS))

    return address, amount

def generate_random_input(pool: str, amount: float):
    key = generate_random_bytes(52)
    return f"0x{encrypt(pool, amount, key).hex()}"
