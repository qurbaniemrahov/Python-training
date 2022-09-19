import sqlite3 #sqlite daxil edirik sisteme

con = sqlite3.connect("kitabxana.db") #kitabxanaya baglaniriq connection

cursor = con.cursor() #cursor adli deyisnler bazasi ustunde emeliyyat etmek ucun istifade edeceyimiz aletdir

def stol_yarat():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitablar(Ad TEXT, Yazici TEXT,Nesriyyat TEXT,sehife_sayi INT )")
    con.commit() #sorgunun verilenler bazasi uzerinde kecerli olmasi ucun commit mecburdur
stol_yarat()

def melumat_elavesi(ad,yazici,nesriyyat,sehife_sayi):
    cursor.execute("INSERT INTO kitablar VALUES(?,?,?,?)",(ad,yazici,nesriyyat,sehife_sayi))
    con.commit()

ad = input("Ad:  ")
yazici = input("Yazici:  ")
nesriyyat = input("Yayin evi:  ")
sehife_sayi = int(input("Sehife sayi:  "))
melumat_elavesi(ad,yazici,nesriyyat,sehife_sayi)

def verilenleri_cek():
    cursor.execute("select * from kitablar")
    data = cursor.fetchall() #verilenler bazasindaki melumatlari cekmek ucun fetcall istifade edirik
    print("Kitablar stolunun melumatlari...")
    for i in data:
        print(i)
    #con commite ehtiyyac yoxdur cunki her hansi bir update etmedik   

def verilenleri_cek2():    
    cursor.execute("select ad,yazici from kitablar")
    data = cursor.fetchall()
    for i in data:
        print(i)


def verilenleri_cek3():
    cursor.execute("select * from nesriyyat = ?",(nesriyyat))
    data  = cursor.fetchall()
    print("Kitablar stolunun melumatlari")
    for i in data:
        print(i)

def verilenleri_yenile(nesriyyat):
    cursor.execute("update kitablar set Nesriyyat = ? where Nesriyyat = ?",("Usa",nesriyyat))
    con.commit()


verilenleri_yenile()
con.close()

#Create table kitablar (Ad TEXT, Yazici TEXT,Nesriyyat TEXT,sehife_sayi INT )
#CREATE TABLE IF NOT EXISTS kitablar(Ad TEXT, Yazici TEXT,Nesriyyat TEXT,sehife_sayi INT )

#datalarin elave olunmasi ucun numuneler

#INSERT INTO kitablar VALUES('code da vinchi','Bilmirem','Baku',1977)

#Sql sorgusu ile data cekmek
#select * from kitablar
#select ad,yazici from kitablar
#select * from kitablar where nesriyyat = 'baku'
#update kitablar set nesriyyat = "Baku" where Nesriyyat = "Gence Media"


