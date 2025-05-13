# client.py
import hashlib
import struct

# Helper to generate MD5 padding
def md5_padding(msg_len: int):
    padding = b'\x80'  # 0x80 = 10000000 (bit 1 followed by zeros)
    padding += b'\x00' * ((56 - (msg_len + 1) % 64) % 64)
    padding += struct.pack('<Q', msg_len * 8)  # 64-bit little-endian
    return padding

def perform_attack():
    # Intercepted values
    original_message = b"amount=100&to=alice"
    original_mac = "614d28d808af46d3702fe35fae67267c"  # taken from vulnerable server
    append_data = b"&admin=true"

    print("=== Length Extension Attack (Simulated) ===")

    for key_len in range(8, 17):  # reasonable guess: 8–16 bytes
        # Step 1: Generate padding as the hash function would do
        padding = md5_padding(len(original_message) + key_len)

        # Step 2: Forge message
        forged_message = original_message + padding + append_data

        print(f"\n[+] Trying with key length = {key_len}")
        print(f"Forged message (raw): {forged_message}")
        print(f"Forged message (hex): {forged_message.hex()}")

        print(f"Use the original MAC: {original_mac}")
        print("Send forged message + original MAC to the vulnerable server.")

        # Stop after one example (you can loop through all)
        break

if __name__ == "__main__":
    perform_attack()
