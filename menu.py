# -*- coding: utf-8 -*-
import os #Ekran temizlemek için import ettik
from sys import platform
import simetrikSifreleme
import karmasiklastir
import adim_hash
# Erdem Gençoğlu
# 12253030
# Kriptoloji Ödevi 1 (Menu tasarlanması)

def main_menu():  #Ana menu
    print 13 * "-", "ANA MENU", 13 * "-"
    print "1. Proje 2"
    print "2. Proje 3"
    print "3. Proje 4"
    print "4. Menu 4"
    print "5. Cikis"
    print 36 * "-"
    loop = True
    while loop:
        try:
            choice = input("Seciminizi yapiniz [1-5]: ")
            if choice == 1:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                sub_menu1()
                loop = False
            elif choice == 2:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                sub_menu2()
                loop = False
            elif choice == 3:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                sub_menu3()
                loop = False
            elif choice == 4:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                print "Ileri seviye kriptoloji"
                print "icerik...\n....\n...\n"
                secim(main_menu)
                loop=False
            elif choice == 5:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                loop = False
            else:
                raw_input("Yanlis deger girdiniz tekrar girmek icin [enter] a basiniz..")
        except:
            print ("Lutfen karekter girmeyiniz!")

def sub_menu1():  #1. alt menu
    print 5 * "-", "Proje-2 algoritmalari", 5 * "-"
    print "1. Karmasiklastirma"
    print "2. Dagilim"
    print "3. Once karistir sonra dagilim uygula"
    print "4. Once dagilim uygula sonra karistir"
    print "5. Ana menuye don"
    print 37 * "-"
    sub_loop = True
    while (sub_loop):
        try:
            choice = input("Seciminizi yapiniz [1-5]: ")
            if choice == 1:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                print "Rail fence ile karmasiklastirma"
                karmasiklastir.main()#proje-2 nin ilk secenegi
                secim(sub_menu1)
                sub_loop=False

            elif choice == 2:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                print ""
                secim(sub_menu1)
                sub_loop = False

            elif choice == 3:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                print ""
                secim(sub_menu1)
                sub_loop = False

            elif choice==4:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                print ""
                secim(sub_menu1)
                sub_loop = False
            elif choice == 5:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                main_menu()
                return
            else:
                raw_input("Yanlis deger girdiniz tekrar girmek icin [enter] a basiniz..")
        except:
            print ("Lutfen karekter girmeyiniz!")

def sub_menu2():
    print 5 * "-", "Sifre cozumleme", 6 * "-"
    print "1. Simetrik Sifreleme"
    print "2. Simetrik Sifreli metnin Cozumu"
    print "3. Ana menuye don"
    print 28 * "-"
    sub_loop = True
    while (sub_loop):
        try:
            choice = input("Seciminizi yapiniz [1-3]: ")
            if choice == 1:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                print "Aes ile simetrik Sifreleme"
                simetrikSifreleme.main()
                secim(sub_menu2)
                sub_loop=False
            elif choice == 2:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                print "Sifrenin Cozumu"
                simetrikSifreleme.aes_decrypt()
                secim(sub_menu2)
                sub_loop = False
            elif choice == 3:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                main_menu()
                return
            else:
                raw_input("Yanlis deger girdiniz tekrar girmek icin [enter] a basiniz..")
        except:
            print ("Lutfen karekter girmeyiniz!")

def sub_menu3():
    print 9 * "-", "Hash ve butunluk", 8 * "-"
    print "1. Adim-1"
    print "2. Adim-2"
    print "3. Ana menuye don"
    print 36 * "-"
    sub_loop = True
    while (sub_loop):
        try:
            choice = input("Seciminizi yapiniz [1-3]: ")
            if choice == 1:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                print "girdi.txt hashlanip sifrelendi cikti.txt kontrol ediniz."
                adim_hash.girdiyi_sifrele()
                secim(sub_menu3)
                sub_loop=False
            elif choice == 2:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                print "Sonuclar"
                adim_hash.ciktiyi_coz()
                secim(sub_menu3)
                sub_loop = False
            elif choice == 3:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                main_menu()
                return
            else:
                raw_input("Yanlis deger girdiniz tekrar girmek icin [enter] a basiniz..")
        except:
            print ("Lutfen karekter girmeyiniz!")

def secim(menu):
    while(1):
        try:
            giris = input("Bir onceki menu icin [1] e basiniz:")
            if giris == 1:
                if platform == "linux" or platform == "linux2":
                    os.system("clear")
                elif platform == "win32":
                    os.system("cls")
                menu()
                break
            else:
                raw_input("Yanlis deger girdiniz tekrar girmek icin [enter] a basiniz..")
        except:
            print ("Lutfen karekter girmeyiniz!")
main_menu()