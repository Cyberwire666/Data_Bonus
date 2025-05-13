import struct

def md5_padding(msg_len: int):
    padding = b'\x80'
    padding += b'\x00' * ((56 - (msg_len + 1) % 64) % 64)
    padding += struct.pack('<Q', msg_len * 8)
    return padding

def perform_attack():
    original_message = b"amount=100&to=alice"
    original_mac = "614d28d808af46d3702fe35fae67267c"
    append_data = b"&admin=true"

    print("=== Simulated MAC Forgery ===")
    for key_len in range(8, 17):
        padding = md5_padding(len(original_message) + key_len)
        forged_message = original_message + padding + append_data

        print(f"\n[+] Trying key length = {key_len}")
        print("Forged message:", forged_message)
        print("Forged message (hex):", forged_message.hex())
        print("Use original MAC:", original_mac)
        break

if __name__ == "__main__":
    perform_attack()
