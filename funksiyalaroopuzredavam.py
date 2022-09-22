#  listim = [1,2,3,4,5]
#  iterator = iter(listim)  #for kimi tekrarliyir
#  while True:
#      try:
#          print(next(iterator))
#      except StopIteration:
#          break    

# class TV():
#     def __init__(self,kanal_list):
#         self.kanal_list = kanal_list
      
#         self.kanal_nomre = -1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.kanal_nomre += 1

#         if(self.kanal_nomre < len(self.kanal_list)):
#             return self.kanal_list[self.kanal_momre]   

#         else:
#             self.kanal_nomre = -1
#             raise StopIteration

# tv = TV(["AZTv,ITV,Space,ITV,ATV"])    #Obyektimizi yaradiriq       

# iterator = iter(tv)
# print(next(tv))

# for i in tv:
#     print(i)


#Generatorlar

def al():
    for i in range(1,6):
        yield i ** 2

generator = al()     

print(generator)