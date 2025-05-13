MAC FORGERY DEMO - HOW TO RUN
=============================

This project demonstrates how a naive MAC implementation using MD5 is vulnerable
to a length extension attack, and how to securely mitigate it using HMAC.

---------------------------------------------
🛠 REQUIREMENTS
---------------------------------------------
- Python 3.x
- No additional libraries needed (uses built-in `hashlib`, `hmac`, `struct`)

---------------------------------------------
📁 FILES INCLUDED
---------------------------------------------
1. server.py           # Naive MAC implementation (vulnerable)
2. client.py           # Simulates MAC forgery using padding
3. secure_server.py    # Secure implementation using HMAC

---------------------------------------------
▶️ HOW TO RUN
---------------------------------------------

1. Run the vulnerable server simulation:
   -------------------------------------
   $ python3 server.py

   You will see the MAC generated for a normal message,
   and a failed attempt to verify a forged message.

2. Run the simulated attack:
   --------------------------
   $ python3 client.py

   This simulates how an attacker would craft a forged message using MD5 padding
   and reuse the original MAC.

3. Run the secure server simulation:
   ---------------------------------
   $ python3 secure_server.py

   This uses HMAC (Hash-based Message Authentication Code).
   Forged messages will fail validation — showing the correct way to handle MACs.

---------------------------------------------
📝 NOTES
---------------------------------------------
- If you want to test other key lengths in `client.py`, edit the range in:
    for key_len in range(8, 17):
- Make sure all files are in the same directory before running them.

---------------------------------------------
✅ EXPECTED OUTPUT
---------------------------------------------
- server.py: Shows a successful MAC generation and a failed verification for forged message.
- client.py: Constructs a forged message and attempts to trick the server.
- secure_server.py: Rejects the forged message securely using HMAC.

---------------------------------------------
🔐 SECURITY LESSON
---------------------------------------------
Never use plain hash(secret + message) for authentication.
Use HMAC instead: hmac.new(key, message, hashlib.md5 or sha256).hexdigest()

