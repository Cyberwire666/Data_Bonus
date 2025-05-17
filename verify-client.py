from server import verify

def test_forged():
    forged_message = b"amount=100&to=alice\x80..." 
    forged_mac = "..." 

    if verify(forged_message, forged_mac):
        print("✅ Attack Successful: Forged MAC accepted!")
    else:
        print("❌ Attack Failed: Forged MAC rejected.")

if __name__ == "__main__":
    test_forged()
