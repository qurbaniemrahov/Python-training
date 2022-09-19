
try:
    a = int("dbskbksdbhbshskbdhksbsdk763763716171")
    print("Proqram buradadir ...")
except:
    print("Xeta bas verdi")
    print("Proqram basa catdi")    


try:
    a = int(input("Reqem 1:"))
    b = int(input("Reqem 2:"))   
    print(a/b)
except:
    print("Zehmet olmasa inputlari dogru yazin")

finally:
    print("Mutleq sekilde islemeli olan kod buradir")    


def ters_cevir(s):
    if(type(s) != str):
        raise ("Zehmet olmasa duzgun input yazin")    
    else:
        return s[::-1]   

       



