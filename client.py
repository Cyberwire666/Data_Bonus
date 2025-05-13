# client.py
import hashpumpy
from server import verify

def perform_attack():
    intercepted_message = b"amount=100&to=alice"
    intercepted_mac = "614d28d808af46d3702fe35fae67267c"
    data_to_append = b"&admin=true"

    # Try multiple key lengths (assume between 8 and 20)
    for key_length in range(8, 21):
        new_mac, new_message = hashpumpy.hashpump(intercepted_mac, intercepted_message.decode(), data_to_append.decode(), key_length)
        forged_message = new_message.encode()
        forged_mac = new_mac

        if verify(forged_message, forged_mac):
            print("SUCCESS: Server accepted the forged message!")
            print("Forged message:", forged_message)
            print("Forged MAC:", forged_mac)
            return

    print("Attack failed. Try increasing key length range.")

if __name__ == "__main__":
    perform_attack()
