import sqlite3
import time

class Kitab():

    def __init__(self,ad,yazici,nesriyyat,tip,say):
        self.ad = ad
        self.yazici = yazici
        self.nesriyyat = nesriyyat
        self.tip = tip
        self.say = say

    def __str__(self):
        return "Kitab adi : {}\nYazici: {}\nNesriyyat: {}\nTip: {}\nSay: {}\n".format(
            self.ad,
            self.yazici,
            self.nesriyyat,
            self.tip,
            self.say
        )  

class Kitabxana():
    def __init__(self):

        self.baglanti_yarat()

def baglanti_yarat(self):
    self.baglanti = sqlite3.connect("kitabxana3.db")
    self.cursor = self.baglanti.cursor()
    sorgu = "create table if not exists kitablar(ad TEXT, yazici TEXT, nesriyyat TEXT, tip TEXT, say INT)"    
    self.cursor.execute     

