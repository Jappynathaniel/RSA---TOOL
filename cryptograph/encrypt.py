from rsa_python import rsa
import decrypt.decrypt as dec
import sys 
key_pair = rsa.generate_key_pair(1024)
message = sys.argv[1]
cipher = rsa.encrypt(message, key_pair["public"], key_pair["modulus"]) #The message to be encoded along with the public key.
decry = dec.decryptor(cipher, key_pair["private"], key_pair["modulus"]) #Private key is used to decode the message.
print("cypher",cipher)

print("\nprivate",key_pair["private"])
print("\nmodulus",key_pair["modulus"])
