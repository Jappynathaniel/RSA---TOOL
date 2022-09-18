def decryptor(cipher,pvtkey,modulo):
    from rsa_python import rsa
    return rsa.decrypt(cipher,pvtkey, modulo)