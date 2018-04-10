import os, struct
from Crypto.Cipher import AES

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = 'uploads/'+in_filename + '.enc'

    iv = '1234561234561234'
    encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    filesize = os.path.getsize(in_filename)
    
    with open(in_filename, 'rb') as infile:
        with open('uploads/'+out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))#packing sizefile biar jd bytes kecil
            outfile.write(iv.encode('utf-8'))#nulis iv biar bisa di decrypt

            while True:
                chunk = infile.read(chunksize)
                
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))#encrypt


          
#os.remove(FileName+".enc")
