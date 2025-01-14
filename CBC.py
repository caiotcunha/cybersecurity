from Crypto.Cipher import AES

def pad (blocks, lastBlock, blockSize = 16):
    n = (blockSize - len(lastBlock))
    if n == 0:
        newBlock = bytes([blockSize] * blockSize)
        blocks.append(newBlock)
    else:
        padding = bytes([n] * n)
        newBlock = lastBlock + padding
        blocks[-1] = newBlock

    return blocks

def unpad (plainText):
    n = plainText[-1] 
    return plainText[:-n]

def CBC_AES_encrypt(plainText, iv,key):
    
    # Split the ciphertext into blocks
    blocks = [plainText[i:i+16] for i in range(0, len(plainText), 16)]
    
    blocks = pad(blocks,blocks[-1])
        
    # Initialize the AES cipher
    cipher = AES.new(key, AES.MODE_ECB)
    
    prev = iv
    
    cipherText = b""
    
    # encrypt each block
    for block in blocks:
        blockCipherText = cipher.encrypt(bytes([block[i] ^ prev[i] for i in range(16)]))
        prev = blockCipherText
        cipherText += blockCipherText
    
    cipherText = iv + cipherText
    
    
    return cipherText
    
def CBC_AES_decrypt(ciphertext, key):
    
    # Split the ciphertext into blocks
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    
    # Initialize the AES cipher
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Initialize the IV
    prev = blocks[0]
    
    # Initialize the plaintext
    plaintext = b""
    
    # Decrypt each block
    for block in blocks[1:]:
        decrypted = cipher.decrypt(block)
        plaintext += bytes([decrypted[i] ^ prev[i] for i in range(16)])
        prev = block
    
    plaintext = unpad(plaintext)
    
    return plaintext.decode('latin-1')