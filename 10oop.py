from email.errors import StartBoundaryNotFoundDefect
from multiprocessing import AuthenticationError
from unicodedata import name

listim = [1,2,3,4,5]

class Developer():

    def __init__(self, ad, soyad, nomre, maas, diller):

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
        
        
        
        
        """.format(self.ad, self.soyad, self.nomre, self.maas, self.diller))

    def dil_elavesi(self, yeni_dil):
        print("Dil elave olunur..")
        self.diller.append(yeni_dil)

    def maas_artimi(self, artan_mebleg):
        print('Maas artirilir ...')
        self.maas += artan_mebleg


developer3 = Developer('Orxan', 'Ibrahimov', 12345,
                       1000, ['Javascript', 'Python'])

developer4 = Developer('Gunel', 'Musayeva', 1234567,
                       4000, ['Go', 'Javascript'])

developer4.melumatlari_goster()

developer4.maas_artimi(500)


print(developer4.maas)


# Inheritance bir clasin diger clasdan atributlari ve metodlari miras alir

class Isci():
    def __init__(self, ad, maas, sobe):
        print("Isci sinfinin init funksiyasi")
        self.ad = ad
        self.maas = maas
        self.sobe = sobe

    def melumatlari_goster(self):
        print("Isci sinfinin melumatlari...")

        print("Ad: {} \nMaas: {} \nSobe: {}\n".format(
            self.ad, self.maas, self.sobe))

    def sobe_deyisdir(self, yeni_sobe):
        print("Sobe deyisir ...")
        self.sobe = yeni_sobe


class Rehber(Isci):       # Isci sinfinden miras alir (inheritance) alir
    pass   # Pass sozu bloku ertelemek ucundur


rehber1 = Rehber('Qurbani', 1000, 'HR')  # Rehber clasinin obyekti

print(dir(rehber1))


class Rehber(Isci):
    def maas_artir(self, artan_mebleg):
        print('Maasa artim gelir..')
        self.maas += artan_mebleg


rehber2 = Rehber('Nicat', 500, 'Enginiering')

rehber2.maas_artir(400)

# Overriding(Legv etme)


class Isci():
    def __init__(self, ad, maas, sobe):
        print("Isci sinfinin init funksiyasi")
        self.ad = ad
        self.maas = maas
        self.sobe = sobe

    def melumatlari_goster(self):
        print("Isci sinfinin melumatlari...")

        print("Ad: {} \nMaas: {} \nSobe: {}\n".format(
            self.ad, self.maas, self.sobe))

    def sobe_deyisdir(self, yeni_sobe):
        print("Sobe deyisir ...")
        self.sobe = yeni_sobe


class Rehber(Isci):
    # Mesuliyyet dasidigi komandadaki iscilerin sayi
    def __init__(self, ad, maas, sobe, isci_sayi):
        print('Rehber sinfinin init funksiyasi')
        self.ad = ad
        self.maas = maas
        self.sobe = sobe
        self.isci_sayi = isci_sayi

    def maas_artir(self, artan_mebleg):
        print('Maas artirilir...')

        self.maas += artan_mebleg


# Rehber sinfinin init funksiyasi override olunur
a = Rehber('Cimi', 1000, 'It', 1)


# Super keywordu(acar sozu)
class Isci():
    def __init__(self, ad, maas, sobe):
        print("Isci sinfinin init funksiyasi")
        self.ad = ad
        self.maas = maas
        self.sobe = sobe

    def melumatlari_goster(self):
        print("Isci sinfinin melumatlari...")

        print("Ad: {} \nMaas: {} \nSobe: {}\n".format(
            self.ad, self.maas, self.sobe))

    def sobe_deyisdir(self, yeni_sobe):
        print("Sobe deyisir ...")
        self.sobe = yeni_sobe


class Rehber(Isci):
    # Mesuliyyet dasidigi komandadaki iscilerin sayi
    def __init__(self, ad, maas, sobe, isci_sayi):

        # 3 eded ozellik isci funksiyasini init funksiyasi ile evez edirik
        super(). __init__(ad, maas, sobe)

        print('Rehber sinfinin init funksiyasi')

        # ekstra ozellik (attribute) da ozumuz elave edirik.
        self.isci_sayi = isci_sayi

    def melumatlari_goster(self):
        print('Rehber sinfinin melumatlari')

        print("Ad: {} \nMaas: {} \nSobe: {}\n Mesuliyyet dasidigi isci sayi {}\n".format(
            self.ad, self.maas, self.sobe, self.isci_sayi))


    def maas_artir(self, artan_mebleg):
        print('Maas artirilir...')

        self.maas += artan_mebleg

c = Rehber('Adil Qedirov',1000,'Hr',4)
print(c)

class Kitab():
    pass

kitab1 = Kitab() # __init__ metodu cagirilacaq

class Kitab():
    def __init__(self, name, author, page_content, novu):
        print("Kitab sinfinin init funksiyasi")
        self.name = name
        self.author = author
        self.page_content = page_content
        self.novu = novu

    def __str__(self):
        #return istifade etmek sertdir
        return "Name: {}  \nAuthor {}  \nPage count  \nType of Book {}\n".format(self.name,self.author,self.page_content,self.novu)  

    def __len__(self):

        return self.page_content   

    def __del__(self):

        print('Kitab silinir')       

kitab1 = Kitab('Code Da Vinchi','-------',800,'Science')

print(kitab1)
print(len(kitab1))


#Del metodu

