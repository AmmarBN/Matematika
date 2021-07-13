import os,sys,time,requests

x = "AmmarBN"
y = "subscribe"

def login():
          user = raw_input("Masukkan Username : ")
          pasw = raw_input("Masukkan Password : ")
          if user ==x and pasw ==y:
              print "Acces granted"
              time.sleep(2)
          else:
              print "Acces danied"
              time.sleep(2)
              os.system("python2 login.py")
if __name__ == "__main__":
       login()

os.system("clear")
banner = """
<--------------------------------------------------------------->
Author : Ammar_SP
YT     : https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ
Github :git clone https://github.com/AmmarBN
<---------------------------------------------------------------->
"""

print (banner)
print ("==================================")
print "(1) pertambahan"
print "(2) pengurangan"
print "(3) perkalian"
print "(4) pembagian"
print ("==================================")
pilih = input("Masukkan Pilihan Anda : ")
if pilih == 1:
	print
	angka_1 = input("Masukkan Angka Pertama : ")
	angka_2 = input("Masukkan Angka Kedua : ")
	total = angka_1 + angka_2
	print"Hasil Pertambahan",total

if pilih == 2:
	print
	angka_1 = input("Masukkan Angka Pertama : ")
        angka_2 = input("Masukkan Angka Kedua : ")
	total = angka_1 - angka_2
	print"Hasil Pengurangan",total

if pilih == 3:
	print
	angka_1 = input("Masukkan Angka Pertama : ")
	angka_2 = input("Masukkan Angka Kedua : ")
	total = angka_1 * angka_2
	print"Hasil Perkalian",total
if pilih == 4:
        print
        angka_1 = input("Masukkan Angka Pertama : ")
        angka_2 = input("Masukkan Angka Kedua : ")
        total = angka_1 - angka_2
	print"Hasil Pembagian",total
									
