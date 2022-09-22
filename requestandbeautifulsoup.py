import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/" #saytimizin linki

response = requests.get(url)  #Web sayti cekirik

html_content = response.content  #Web saytin icerisin alir

soup = BeautifulSoup(html_content,"html.parser") #Web saytimizi parcalamaq ucun Beautiful soup obyektine atiriq menbeni!

# print(soup.prettify()) #Daha gozel goruntu elde etmek ucun pretify istifade edirik

# for i in soup.find_all("a"):
#     print(i.text)

a = float(input("Rating-i yazin: "))

basliqlar = soup.find_all("td",{"class":"titleColumn"})
ratinqler = soup.find_all("td",{"class","ratingColumn imdbRating"})

for basliq,rating in zip(basliqlar,ratinqler):
    basliq = basliq.text
    rating = rating.text

    basliq = basliq.strip()
    basliq = basliq.replace("\n","")


    rating = rating.strip()
    rating = rating.replace("\n","")

    if(float(rating)> a):
        print("Filmin adi: {} Filmin reytinqi: {}".format(basliq,rating))





