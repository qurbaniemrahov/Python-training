import os

file = open("senan.txt","w")  #w menasi write demekdir



os.getcwd()



#a - size append xarakterli elave etmeye komek edir
file = open("senan.txt","a",encoding="utf-8")
file.write("Qurbani\nElvin\nRustem")
file.close()
file = open("senan.txt","r")

for i in file:
    print(i)
file.close()    

file.close()

#Fayllari avtomatik baglayan funksiya




    





