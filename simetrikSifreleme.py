# -*- coding: utf-8 -*-
import hashlib
from Crypto.Cipher import AES


def main():
    metin=''
    passwordkey=''
    # dosyadan sifrelenmek istenen metnin okunmasi
    file = open("s_girdi.txt", "r")
    for line in file:
        metin += line
    # dosyadan key in okunması
    file = open("key.txt", "r")
    for line in file:
        passwordkey += line.strip() + ""
    # Girilen metnin secilen blok boyutu için metin boyutunun kontrol edilmesi
    if (16 and (len(metin) % 16) == 0):
        aes_encrypt(metin,passwordkey)
    else:
        print "Girdi metninizin metin boyutu 16 nin kati degildir"
        print "Metin içindeki karakter boyutu: ", len(metin)

def aes_encrypt(metin,passwordkey):
    key = hashlib.sha256(passwordkey).digest()
    IV = 16 * '\x00'  # Initialization vector: discussed later
    mode = AES.MODE_CBC
    encryptor = AES.new(key, mode, IV=IV)
    ciphertext =encryptor.encrypt(metin)
    file = open("s_cikti.txt", "w")
    file.write(ciphertext)
    file.close()
    print ("Sifreli metininiz s_cikti.txt dosyasina yazdirilmistir.")

def aes_decrypt():
    sifreli =''
    cozumkey=''

    # dosyadan cozumkey in okunması
    file = open("cozum_key.txt", "r")
    for line in file:
        cozumkey += line.strip() + ""
    # dosyadan sifrelenmis metnin okunmasi
    file = open("s_cikti.txt", "r")
    for line in file:
        sifreli += line.strip() + ""

    ckey = hashlib.sha256(cozumkey).digest()
    IV = 16 * '\x00'
    mode = AES.MODE_CBC
    decryptor = AES.new(ckey, mode, IV=IV)
    plaintext =decryptor.decrypt(sifreli)
    print "Sifreli metnin cozumu: \n",plaintext
