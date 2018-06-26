# -*- coding: utf-8 -*-
# Karmasiklastirmada Rail fence algoritmasini kullandim.
# Cit uzunlugunu 3 sectim.Normalde yukaridan asagiya dogru yazilir.
# Burada zigzag deseninde olusturucaz

def main():
    # dosyadan okuyup dosyaya yazma islemi
    with open("girdi.txt", "r") as fileRead:
        with open("cikti.txt", "a") as fileWrite:
            for line in fileRead.readlines():
                fileWrite.write(rail_fence(line)+"\n")
    print('\n')
    print ("Karmasik metinleriniz cikti.txt dosyasina yazdirilmistir.")

def rail_fence(cleartext):
    #cleartext giris.txt den gelen satirlardir

    key = 3  # Rail fence icin key(cit'i)i 3 belirledik degistirilebilir.
    encrypt_hali=""
    # gelen cleartextin boyutu(lenght) kadar stun ve key kadar satir matrisi olustuturur
    matris = [["" for x in range(len(cleartext))] for i in range(key)]
    increment = 1
    satir = 0
    stun = 0

    cleartext = cleartext.replace('\n','')  #Dosyadan okudugumda sondaki \n ifadeside geliyor onu ortadan kaldirmak için yapildi

    for i in cleartext:
        if satir + increment < 0 or satir + increment >= len(matris):
            increment = increment * -1
        matris[satir][stun] = i
        satir += increment
        stun += 1

    for list in matris:
        encrypt_hali += "".join(list)
    return encrypt_hali

#rail fence çözümleyen metod
def rail_fence_decipher(ciphertext):
    key=3
    decrypt_hali = ""

    matris = [["" for x in range(len(ciphertext))] for y in range(key)]
    idx = 0
    increment = 1

    for secilenSatir in range(0, len(matris)):
        satir = 0
        for stun in range(0, len(matris[satir])):
            if satir + increment < 0 or satir + increment >= len(matris):
                increment = increment * -1
            if satir == secilenSatir:
                matris[satir][stun] += ciphertext[idx]
                idx += 1
            satir += increment
    # matrisin transpozunu aldiktan sonra bizim cozumumuz matrisin satirlari olucaktir
    matris = transpoz_al(matris)
    for list in matris:
        decrypt_hali += "".join(list)
    return decrypt_hali


# Matrisin transzpozunu alma metodu
def transpoz_al(matris):
    sonuc = [[0 for y in range(len(matris))] for x in range(len(matris[0]))]
    for i in range(len(matris)):
        for j in range(len(matris[0])):
            sonuc[j][i] = matris[i][j]
    return sonuc
