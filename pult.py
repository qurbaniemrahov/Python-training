import random
import time


class Pult():

    def __init__(self, tv_status="Off", tv_sesi=0, kanal_list=['AZTV'], kanal='AZTV'):
        self.tv_status = tv_status
        self.tv_sesi = tv_sesi
        self.kanal_list = kanal_list
        self.kanal = kanal

    def tv_qos(self):
        if (self.tv_status == 'Off'):
            print('Tv onsuzda aciqdir...')

        else:
            print('Tv acilir')
            self.tv_status == 'On'

    def tv_off(self):
        if (self.tv_status == 'Off'):
            print('Tv onsuzda sonuludur')

        else:
            print('Tv sonur...')
            self.tv_status = 'Off'

    def ses_deyis(self):
        while True:
            cavap = input(
                "Sesi azalt: '<' \n Sesi artir: '>'\nCixis ucun: q-ya bas")

            if (cavap == "<"):
                if (self.tv_sesi != 0):
                    self.tv_sesi -= 1

            elif (cavap == ">"):
                if (self.tv_sesi != 21):
                    self.tv_sesi += 1

                    print("Ses:", self.tv_sesi)
            else:
                print("Ses deyismedi:", self.tv_sesi)
                break

    def kanal_elave(self, kanal_adi):
        print('Kanal elave olunur...')
        time.sleep(1)
        self.kanal_list.append(kanal_adi)
        print('Kanal elave olundu...')

    def tesadufi_kanal(self):
        tesadufi = random.randint(0, len(self.kanal_list)-1)
        self.kanal = self.kanal_list[tesadufi]
        print("Cari kanal:", self.kanal)

    def __len__(self):
        return len(self.kanal_list)

    def __str__(self):
        return "Tv Veziyyeti: {}\nTv sesi: {}n\Kanal listi: {}\nCari Kanal: {}\n".format(self.tv_status, self.tv_sesi, self.kanal_list, self.kanal)

pult = Pult()


print("""
Televizor Proqrami:

1.Tv qos
2.Tv sondur
3.Ses tenzimeleri
4.Kanal elave et
5.Kanal sayini goster
6.Tesadufi kanala kec
7.Televizor melumatlari




""")

while True:
    emeliyyat = input("Emeliyyat secin:")

    if(emeliyyat == "q"):
        print("Proqramdan cixildi")
        break

    elif(emeliyyat == "1"):
        pult.tv_qos()    
    elif(emeliyyat == "2"):
        pult.tv_off()
    elif(emeliyyat == "3"):
        pult.ses_deyis() 
    elif(emeliyyat == "4"):
        kanal_adlari = input("Kanal adlarini ',' ile ayiraraq yazin.")   

        kanal_siyahisi = kanal_adlari.split(",")    

        for elave in kanal_siyahisi:
            pult.kanal_elave(elave)

    elif(emeliyyat == "5"):
        print("Kanal sayi:",len(pult))  

    elif(emeliyyat == "6"):
        pult.tesadufi_kanal()

    elif(emeliyyat == "7"):
        print(pult)    

       

    else:
        print("Duzgun emeliyyat secin:")              