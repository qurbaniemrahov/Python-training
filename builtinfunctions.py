#Advance level of string


#upper () and lower ()
print("python".upper())

#replace() 

# "Javascript".replace("Python")

#split () stringi parcalara ayirir

# name  = "Qurbani"

# print(name.split(""))
# print(name)

#strip(), lstrip(), rstrip()
#strip(x) -Stringin basinda ve sonunda olan x deyerini silir
#lstrip() -Stringin sadece basinda olan x deyerini silir

print("    Python       ".strip())

#join()

listim = ['21','02','2000']
print('/'.join(listim))

#count verilen deyerin nece defe kecdiyin gosterir


#find() ve rfind()

a = "masin".find("a")
print(a)

#set-ler datatype-dir bir deyerde sadece bi defe deyer tutan veri tipidir



listim = [1,2,3,4,5]

x = set(listim)

print(x)

x = {'Python','Php','Js'}

for i in x:
    print(i)


#set method add()




x = set()
print(dir(x))