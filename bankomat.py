#Atm proqrami

print("**********\nAtm sistemine xos gemisiniz!\n**********")

print("""
Emeliiyatlar:

1. Balans Yoxlama
2. Balans Artirma
3. Pul cekme

Proqramdan cixmaq ucun "q" herfine basin




""")

balans = 1000 #balnsdaki mebleg

while True:
    emeliyyat = input("Emeliiyat secin: ")

    if (emeliyyat == "q"):
        print("yene sizi gozleyirik ugurlar olsun")
        break
    elif (emeliyyat == "1"):
        print("balansiniz {} - azn-dir".format(balans))
    elif (emeliyyat == "2"):
        mebleg = int(input("Artirmaq istediyiniz meblegi yazin: "))
        balans += mebleg
    elif (emeliyyat == "3"):
        mebleg = int(input("Cekmek istediyiniz meblegi secin"))
        
        if (balans-mebleg <0):
            print("Bu qeder pul ceke bilmersiz")
            print("Balansiniz {} - azndir".format(balans))
            continue

        balans-=mebleg
    else:
         print("Zehmet olmasa duzgun bir emeliyyat secin")
           



        
        

