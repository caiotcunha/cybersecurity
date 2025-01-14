import CBC
import CTR

def main():
    
    print("Questão 1")
    key = bytes.fromhex("140b41b22a29beb4061bda66b6747e14")
    f = bytes.fromhex("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
    plaintext = CBC.CBC_AES_decrypt(f, key)
    print(plaintext)
    
    print("Questão 2")
    f = bytes.fromhex("5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253")
    plaintext = CBC.CBC_AES_decrypt(f, key)
    print(plaintext)
    
    print("Questão 3")
    key = bytes.fromhex("36f18357be4dbd77f050515c73fcf9f2")
    f = bytes.fromhex("69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329")
    plaintext = CTR.CTR_AES_decrypt(f, key)
    print(plaintext)
    
    print("Questão 4")
    f = bytes.fromhex("770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451")
    plaintext = CTR.CTR_AES_decrypt(f, key)
    print(plaintext)
    
    key = bytes.fromhex("140b41b22a29beb4061bda66b6747e14")
    plainText = b"Test CBC encryption"
    iv = b'L\xa0\x0f\xf4\xc8\x98\xd6\x1e\x1e\xdb\xf1\x80\x06\x18\xfb('
    f = CBC.CBC_AES_encrypt(plainText, iv,key)
    plaintext = CBC.CBC_AES_decrypt(f, key)
    print(plaintext)
    
    iv = b'i\xdd\xa8E\\}\xd4%'
    c = b'K\xf3S\xb7s0N\xec'
    key = bytes.fromhex("36f18357be4dbd77f050515c73fcf9f2")
    plaintext = b"Test CTR encryption"
    f = CTR.CTR_AES_encrypt(iv,c,key,plaintext)
    plaintext = CTR.CTR_AES_decrypt(f, key)
    print(plaintext)
    
    
    
    
if __name__ == "__main__":
    main()