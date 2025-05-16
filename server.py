# server.py
import hmac
import hashlib

SECRET_KEY = b'supersecretkey'

def generate_mac(message: bytes) -> str:
    return hmac.new(SECRET_KEY, message, hashlib.sha256).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    expected_mac = generate_mac(message)
    return mac == expected_mac

def main():
    message = b"amount=100&to=alice"
    mac = generate_mac(message)

    print("=== Server Simulation (Using HMAC) ===")
    print(f"Original message: {message.decode()}")
    print(f"MAC: {mac}")

    print("\n--- Verifying legitimate message ---")
    if verify(message, mac):
        print("✅ MAC verified successfully. Message is authentic.\n")
    else:
        print("❌ MAC verification failed.\n")

    forged_message = b"amount=100&to=alice&admin=true"
    forged_mac = mac  

    print("--- Verifying forged message ---")
    if verify(forged_message, forged_mac):
        print("❌ MAC verified successfully (unexpected - ATTACK SUCCEEDED).")
    else:
        print("✅ MAC verification failed (as expected - ATTACK FAILED).")

if __name__ == "__main__":
    main()
