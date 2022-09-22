#Dekoratlor kod tekrarinin qarsisini almaq ucun yaradilib

import time

def zaman_hesabla(funksiya):
    def wrapper(reqemler):

        baslama_saati = time.time()
        netice = funksiya(reqemler)
        bitme_saati = time.time()
        print(funksiya.__name__ + " " + + str(bitme_saati-baslama_saati)+ "saniye cekdi.")

        return netice

    return wrapper 
    
@zaman_hesabla
def hesabla(reqemler):
    netice = []
    for i in reqemler:
        netice.append(i**2)
    return netice        
