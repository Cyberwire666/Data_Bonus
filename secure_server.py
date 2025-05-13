import hashlib, hmac

SECRET_KEY = b'supersecretkey'

def generate_mac(message: bytes) -> str:
    return hmac.new(SECRET_KEY, message, hashlib.md5).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    return hmac.compare_digest(generate_mac(message), mac)

def main():
    message = b"amount=100&to=alice"
    mac = generate_mac(message)

    print("=== Secure Server ===")
    print(f"Original message: {message.decode()}")
    print(f"MAC: {mac}")

    forged_message = b"amount=100&to=alice&admin=true"
    forged_mac = mac

    print("\n--- Verifying forged message ---")
    if verify(forged_message, forged_mac):
        print("MAC verified (unexpected).")
    else:
        print("MAC verification failed ✅ (secure).")

if __name__ == "__main__":
    main()
