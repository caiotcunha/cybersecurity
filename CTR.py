from Crypto.Cipher import AES

def CTR_AES_encrypt(iv,c,key,plainText):
    
    # Initialize the AES cipher
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Split the plaintext into blocks
    blocks = [plainText[i:i+16] for i in range(0, len(plainText), 16)]
    
    #Initialize the ciphertext
    ciphertext = b""
    
    ivC = iv + c
    
    # Decrypt each block
    for block in blocks:
        counterEncrypted = cipher.encrypt(ivC)
        # size of counter = plaintext block size
        counterEncrypted = counterEncrypted[:len(block)]
        ciphertext += bytes([counterEncrypted[i] ^ block[i] for i in range(len(block))])
        
        ivC = int.from_bytes(ivC, "big") + 1
        ivC = int.to_bytes(ivC,16,"big")
    
    ciphertext = iv + c + ciphertext
    
    return ciphertext

def CTR_AES_decrypt(ciphertext, key):
    #IV
    iv = ciphertext[:8]
    
    #counter
    c = ciphertext[8:16]

    #cipher
    ciphertext = ciphertext[16:]
    
    # Initialize the AES cipher
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Split the ciphertext into blocks
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    
    #Initialize the plaintext
    plaintext = b""
    
    ivC = iv + c
    
    # Decrypt each block
    for block in blocks:
        counterEncrypted = cipher.encrypt(ivC)
        # size of counter = plaintext block size
        counterEncrypted = counterEncrypted[:len(block)]
        plaintext += bytes([counterEncrypted[i] ^ block[i] for i in range(len(block))])
        
        ivC = int.from_bytes(ivC, "big") + 1
        ivC = int.to_bytes(ivC,16,"big")
    
    return plaintext.decode('latin-1')