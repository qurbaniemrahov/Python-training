from email.errors import StartBoundaryNotFoundDefect


class Developer():


    def __init__(self,ad,soyad,nomre,maas,diller):

        self.ad = ad
        self.soyad = soyad
        self.nomre = nomre
        self.maas = maas
        self.diller = diller

    def melumatlari_goster(self):
        print("""
        Proqramist haqqinda melumatlar
        
        Ad: {}
        
        Soyad: {}
        
        Nomre: {}
        
        Maas: {}
        
        Diller: {}
        
        
        
        
        """.format(self.ad,self.soyad,self.nomre,self.maas,self.diller))

    def dil_elavesi(self,yeni_dil):
        print("Dil elave olunur..")    
        self.diller.append(yeni_dil)

    def maas_artimi(self,artan_mebleg):
        print('Maas artirilir ...') 
        self.maas += artan_mebleg  


developer3 = Developer('Orxan','Ibrahimov',12345,1000,['Javascript','Python'])

developer4 = Developer('Gunel','Musayeva',1234567,4000,['Go','Javascript'])

developer4.melumatlari_goster()

developer4.maas_artimi(500)


print(developer4.maas)


#Inheritance bir clasin diger clasdan atributlari ve metodlari miras alir

class Isci():
    def __init__(self,ad,maas,sobe):
        print("Isci sinfinin init funksiyasi")
        self.ad = ad
        self.maas = maas
        self.sobe = sobe

    def melumatlari_goster(self):
        print("Isci sinfinin melumatlari...")

        print("Ad: {} \nMaas: {} \nSobe: {}\n".format(self.ad,self.maas,self.sobe)) 

    def sobe_deyisdir(self,yeni_sobe):
        print("Sobe deyisir ...")
        self.sobe = yeni_sobe

class Rehber(Isci):       # Isci sinfinden miras alir (inheritance) alir    
    pass   # Pass sozu bloku ertelemek ucundur 

rehber1 = Rehber('Qurbani',1000,'HR') #Rehber clasinin obyekti

print(rehber1.sobe)


