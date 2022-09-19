from functools import reduce

#map funksiyasi
#iterate olunan data tipler mutable ve immutable 

def double(x):
    return x* 2
map(double,[1,2,3,4,5,6,7])

print(list(map(double,[1,2,3,4,5,6,7]))) 


print(list(map(lambda x: x ** 2,[1,2,3,4,5])))

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [9,10,11,12,13,14]

map(lambda x,y : x * y,list1,list2)

print(list(map(lambda x,y : x * y,list1,list2)))

#reduce funksiyasidir built in functiondur (yeni icerisinde python olan funksiyalar)

reduce(lambda x,y : x + y,[12,18,20,10])

print(reduce(lambda x,y : x + y,[12,18,20,10]))

def maximum(x,y):
    if(x>y):
        return x
    else:
        return y    
reduce(maximum,[-2,1,100,35,32]) 
print(reduce(maximum,[-2,1,100,35,32]) )  

#filter funksiyasi
list(filter(lambda x: x % 2 == 0,[1,2,3,4,5,6,7,8]))

print(list(filter(lambda x: x % 2 == 0,[1,2,3,4,5,6,7,8])))

#zip funksiyasi
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10,11]

i = 0
netice = list()

while(i<len(list1) and i<len(list2)):
    netice.append(list1[i],list2[i])
    i+=1
print(netice)

zip(list1,list2)

print(list(zip(list1,list2)))

#enumerate()  nomreleme

listim = ["Alma","Armud","Banan"]
print(list(enumerate(listim)))

#All and Any function
list4 = [1,2,3,4,5]
list5 = [1,2,3,4,5]

print(all(list4))
print(any(list5))




