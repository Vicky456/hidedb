import base64
from cryptography.fernet import Fernet


def encrypt(key,plainText):
    enc=[]
    for i in range(len(plainText)):
        key_c=key[i%len(key)]
        enc_c=chr((ord(plainText[i])+ord(key_c))%256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decrypt(key,cyperText):
    dec=[]
    enc=base64.urlsafe_b64decode(cyperText).decode()
    for i in range(len(enc)):
        key_c=key[i%len(key)]
        dec_c=chr((256+ord(enc[i])-ord(key_c))%256)
        dec.append(dec_c)
    return "".join(dec)




key = Fernet.generate_key() #this is your "password"
print(key)
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(b"Hello stackoverflow!")
print(encoded_text)
decoded_text = cipher_suite.decrypt(encoded_text)
print(decoded_text)


