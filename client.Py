# client.py
import hashpumpy
import server  
def perform_attack():
    intercepted_message = b"amount=100&to=alice"
    intercepted_mac = server.generate_mac(intercepted_message)
    data_to_append = b"&admin=true"

    for key_length in range(8, 17): 
        result = hashpumpy.hashpump(intercepted_mac, intercepted_message.decode(), data_to_append.decode(), key_length)
        forged_mac = result[0]
        forged_message = result[1].encode()

        if server.verify(forged_message, forged_mac):
            print("✅ Attack successful!")
            print("Forged message:", forged_message)
            print("Forged MAC:", forged_mac)
            return

    print("❌ Attack failed. Couldn't forge valid MAC.")

if __name__ == "__main__":
    perform_attack()
