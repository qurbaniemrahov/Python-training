#TCP/IP - Transmission Control Protocol - Internet Protocol
# email: pythonsmtp3@gmail.com
# login: pythonsmtp3@gmail.com
#smtp-server : smtp.gmail.com / smtp-relay.gmail.com
# Password: Baku2022
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart() # Mail strukturumuzu yaratmaga komek edir

mesaj["From"] = "pythontest3@gmail.com" # Email kimden gedecek
mesaj["To"] = "allahverdiulvi@gmail.com" # Kime gondereceyik
mesaj["Subject"] = "SMTP ile mail gondermek" # Mailin movzusu

#Mailin icerisi
yazi = """

Salam, Python ile email gonderirem.
Bu ise menim ikinci emailimdir!!!

Ulvi Allahverdiyev

"""
mesaj_icerisi = MIMEText(yazi,"plain") #Mailmizin icerisini bu sinifden yaradcagiq
mesaj.attach(mesaj_icerisi) # Mailimizin icerisini mail struktumuza elave edirik

try:
    mail = smtplib.SMTP("smtp.gmail.com",587) # SMTP obyektimizi yaradiriqi ve gmail smtp serverine-baglaniriq
    mail.ehlo() # SMTp serverine ozumuzu tanidiriq
    mail.starttls() #Adresimizin ve sifremizin xususi sifreleme metodu ucun vacibdir
    mail.login("pythonsmtp3","Baku2022") # SMTP serverine giris edirik, Oz mail adresinizi ve sifremizin yaziriq
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string()) # Mailimizi gonderirik
    print("E-mail ugurla gonderildi...")
    mail.close() #SMTP serverimizin baglantisini qiririq.
    
except:
    sys.stderr.write("E-mail gondermek ugursuz...") # Herhansi bir baglanti xetasi olanda veya mail gondermek zamani bu xetaniversin
    sys.stderr.flush()
print("E-mail ugurlar gonderildi...")
# https://pillow.readthedocs.io/en/stable/


