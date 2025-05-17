import hmac
import hashlib

SECRET_KEY = b'supersecretkey'

def generate_hmac(message: bytes) -> str:
    return hmac.new(SECRET_KEY, message, hashlib.md5).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    return hmac.compare_digest(generate_hmac(message), mac)

def main():
    message = b"amount=100&to=alice"
    mac = generate_hmac(message)
    print("=== Secure Server Simulation ===")
    print(f"Original message: {message.decode()}")
    print(f"HMAC: {mac}")

    print("\n--- Verifying message ---")
    if verify(message, mac):
        print("✅ Message is authentic and verified.")

if __name__ == "__main__":
    main()
