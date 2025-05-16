# MAC Forgery Attack Demonstration and Mitigation

## Overview
This project demonstrates a **length extension attack** against a naive hash-based MAC implementation and shows the secure HMAC alternative.

## Files

### 1. Insecure Server (`server.py`)
```python
import hashlib

SECRET_KEY = b'supersecretkey'

def generate_mac(message: bytes) -> str:
    return hashlib.md5(SECRET_KEY + message).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    return mac == generate_mac(message)
```
### 2. Attacker (client.py)
```python
import hashpumpy
import server

def perform_attack():
    intercepted_message = b"amount=100&to=alice"
    intercepted_mac = server.generate_mac(intercepted_message)
    data_to_append = b"&admin=true"

    for key_length in range(8, 17):
        forged_mac, forged_message = hashpumpy.hashpump(
            intercepted_mac,
            intercepted_message.decode(),
            data_to_append.decode(),
            key_length
        )
        if server.verify(forged_message.encode(), forged_mac):
            print("✅ Attack successful!")
            return forged_message.encode(), forged_mac
```
### 3. Secure Server (secure_server.py)
```python
import hmac
import hashlib

SECRET_KEY = b'supersecretkey'

def generate_hmac(message: bytes) -> str:
    return hmac.new(SECRET_KEY, message, hashlib.sha256).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    return hmac.compare_digest(generate_hmac(message), mac)
```
### How to Run
### Install dependencies:

```bash
pip install hashpumpy
```
### Test the insecure implementation:

```bash
python server.py
python client.py  # Will show successful attack
```
### Test the secure implementation:

```bash
python secure_server.py
python client.py  # Will show failed attack
```
### Expected Outputs

=== Insecure Server ===
```bash
Original message: amount=100&to=alice
MAC: 614d28d808af46d3702fe35fae67267c
```
✅ Attack successful!
```bash
Forged message: b'amount=100&to=alice\x80...&admin=true'
```


=== Secure Server ===
```bash
Original message: amount=100&to=alice
HMAC: 9a83ddf5e5d49a9a...
```
❌ Attack failed (expected with HMAC)

### Technical Explanation
### Why the Attack Works
MD5 processes messages in blocks
Final MAC represents internal hash state
Attacker can continue hashing from this state

### Why HMAC Prevents It
Uses key mixing: hash(key ⊕ opad || hash(key ⊕ ipad || message))
Inner hash destroys length extension property   
Mathematically proven secure construction

### Team
Yehia Tarek
Sara Ahmed
Shadwa Ahmed

### Course
Data Integrity and Authentication
### Submission Date
May 16, 2023
