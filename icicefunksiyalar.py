#Ic ice funksiyalar

#args and kwargs (keywordarguments)

def funksiya(*args):
    print(args)
    for i in args:
        print(i)

funksiya(1,2,3,4)

def funk(ad,*args):
    print("Ad:",ad)
    for i in args:
        print(i)

funk("Qurbani",1,2,3,4,5)        

# **kwargs

def funk1(**kwargs):
    print(kwargs)

funk1(ad = "Qurbani", soyad = "Emrahov", nomrem = 12345)

def funk2(**kwargs):
    for i,j in kwargs.items():
        print("Argumentin ad:",i, "Argumentin deyeri:",j)

        
def funksiya(*args,**kwargs):
    for i in args:
        print("Argumentler:",i)

    print("-------------------")
    for i,j in kwargs.items():
        print("Argumentin adi:",i,"Argumentin deyeri:",j)  

funksiya(1,2,3,4,5,6,7,ad = "Qurbani", soyad = "Emrahov", nomre = 123455) 

def funksiya1():
    def funksiya2():
        print("Hello from 2 function")
    print("Hello from bigger function")      
    funksiya2()  
      
#Funksiyalari geri dondermek ve arqument olaraq dondermek

def funksiya(emeliyyat):

    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def vurma(*args):
        vur = 1
        for i in args:
            vur *= i
        return vur

    if emeliyyat == "toplama":
        return toplama
    else:
        return vurma

test = funksiya("toplama")
print(test(1,2,3,4)) 

test1 = funksiya("vurma")
print(test1(5,4))


#Funksiyalari arqument olaraq gondere bilirik...

def toplama(a,b):
    return a +b 

def vurma(a,b):
    return a * b

def cixma(a,b):
    return a -b 

def bolme(a,b):
    return a/b  

def ana_funksiya(func1,func2,func3,func4,emeliyyat):
    if(emeliyyat == "topla"):
        print(func1(3,4))
    elif(emeliyyat == "vurma"):
        print(func2(10,3))
    elif(emeliyyat == "cixma"):
        print(func3(20,5)) 
    elif(emeliyyat == "bolme"):
        print(func4(10,4))  
    else:
        print("Duzgun emeliyyat secin")                       



