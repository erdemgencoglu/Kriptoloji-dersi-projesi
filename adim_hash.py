# -*- coding: utf-8 -*-
from aead import AEAD

sifreleyici = AEAD(AEAD.generate_key())

# 100 defa hashleme metedu
def getHash(key):
    hashli_metin = ""
    for x in range(0,100):
        hashli_metin = hash(key)
    return hashli_metin

# girdi.txt dosyasinin ve key.txt dosyalarinin okunmasi ve haslenip cikti.txt icine yazilmasi
def girdiyi_sifrele():
    with open("girdi.txt", "r") as fileReadInput:
        with open("key.txt", "r") as fileReadKey:
            with open("cikti.txt", "a") as fileWriteOutput:
                key = fileReadKey.readline().strip()
                for line in fileReadInput.readlines():
                    fileWriteOutput.write(sifreleyici.encrypt(line.strip(), key) +"||" + str(hash(line.strip())) +"||" + str(getHash(key))+"\n")
                    with open("cikti.txt", "w") as fileReadd:
                        print ""
# cikti.txt nin icindeki veriler okunup ayristirildiktan sonra butunluk testinin yapilmasi
def ciktiyi_coz():
    with open("cikti.txt", "r") as fileReadOutput:
        with open("key.txt", "r") as fileReadKey:
            with open("girdi.txt", "r") as fileReadInput:
                with open("girdi.txt", "a") as fileWriteInput:
                    key = fileReadKey.readline().strip()
                    for line in fileReadOutput.readlines():
                        duzenle = line.strip()
                        cipherText = duzenle.split("||")[0]#Sifreli metnin alinmasi
                        hashText = int(duzenle.split("||")[1])#hashlenmis metnin alinmasi
                        hashKey = duzenle.split("||")[2]#hashlenmis keyin alinmasi
                        girdi_bilgi = fileReadInput.readline().strip()#girdi.txt deki icerik
                        hashli_girdi_bilgi = hash(girdi_bilgi)#girdi.txt nin hashlenmis hali
                        orjinal_key = str(getHash(key))#keyimizin ilk hali
                        if hashli_girdi_bilgi == hashText:
                            if hashKey == orjinal_key:
                                print "Hashler uyuştu butunluk bozulmadi"
                                fileWriteInput.write(sifreleyici.decrypt(cipherText ,key) + "\n")
                            else:
                                print "Keyler uyuşmadı."
                        else:
                            print "Hash'li veriler uyuşmadı."
                        with open("girdi.txt", "w") as fileReadd:
                            print ""
