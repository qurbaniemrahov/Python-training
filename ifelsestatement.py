Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Mentiqi deyerler ve qarsilasdirma operatorlari
#Mentiqi baglayicilar ve opeartoru
#Serti veziyyetler if else bloku
#sertli veziyyetler -if elif else bloku


#Boolean
#Boolean
clear()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
 a = True
 
SyntaxError: unexpected indent
a
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a
NameError: name 'a' is not defined
KeyboardInterrupt


a = True
a
True
print(type(a))
<class 'bool'>
b = False
b
False
type(b)
<class 'bool'>
bool(5.5)
True
bool()-1
-1
bool(-1)
True
bool(0)
False
bool(" ")
True
2>1
True
1<5
True
1>5
False
type(1>5)
<class 'bool'>
type(none)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    type(none)
NameError: name 'none' is not defined. Did you mean: 'None'?
c = None
c

type(c)
<class 'NoneType'>
"Qurbani" == "Qurbani"
True
2 != 3
True
#Mentiqi baglayicilar ve operatoru
1<2
True
1<2 and "Qurbani" == "Qurbani"
True
1<2 and "Qurbani" == "Qurbanii"
False
- * - =
SyntaxError: invalid syntax
- * - = +
SyntaxError: invalid syntax
true and true
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    true and true
NameError: name 'true' is not defined. Did you mean: 'True'?
true>true
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    true>true
NameError: name 'true' is not defined. Did you mean: 'True'?
True and False
False
True and True
True
False and False
False
'
False and True
False
False>True
False
True == 0
False
True ==1
True
False ==0
True
1< 2 or "Qurbani" != "Eli"
True
1> 2 or "Qurbani" != "Eli"
True
True or True
True
True or False
True
False or False
False
True or False
True
True or True
True
not
SyntaxError: invalid syntax
#not operator yazdigimiz True deyerin inkar etmek ucundur
2 == 2
True
not 2 == 2
False
2 == 2 and not 3<2
True
not(2.14>3.49) or (2 != 2 and "Qurbani" == "Qurbani")
True
not True
False
not False
True
a = 5
b = 6
a=(a+b)*6/a+b=6
SyntaxError: cannot assign to expression
a
5
a=6*(a+b)/a+b
a
19.2
a=6(a+b)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a=6(a+b)
TypeError: 'int' object is not callable
a= a+b/a+b
a
25.5125
a=(a+b)/(a+b)
a
1.0
a = (a+b)/(a+b) *6
a
6.0
KeyboardInterrupt


a = 5
b=6

a = (a+b)/(a+b) *6
a
6.0
int(a)
6
b = (a+b)/(a+b) *5
b
5.0
int(b)
5
a = (a+b)/(a+b) *b
a
5.0
a = (a+b)/(a+b) *a
a
5.0
KeyboardInterrupt


a= 5
b = 6
a = (a+b)/(a+b) *b
a
6.0
b = (a+b)/(a+b) *a
b
6.0
b
6.0
a =
SyntaxError: invalid syntax

KeyboardInterrupt

a = 2
a
2
a = 2
if(a == 2):
    print(a)


2

if(a == 2):
    print(a)
print("Salam")
SyntaxError: invalid syntax
print("Salam")
Salam
#18 yas olub olmamasin kontrol etmek
age = int(input("Enter your age:"))
Enter your age:18
if (age < 18):
    print("your age is less than 18 tou dont enter this site")
else:
    print("welcome")

    
welcome
#reqem musbetdir ya menfi
digit = int(input("Enter input:"))
Enter input:5
if(digit<0):
    print("negative number")
else:
    print("pozitive number")

    
pozitive number

KeyboardInterrupt
digit
5

a = 12345
print(len(a))
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    print(len(a))
TypeError: object of type 'int' has no len()
print(a.len())
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    print(a.len())
AttributeError: 'int' object has no attribute 'len'
len(a)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    len(a)
TypeError: object of type 'int' has no len()
a = "12345"
print(len(a))
5
#Authentication
print("********\n Istifadeci Girisi\n********")
********
 Istifadeci Girisi
********
********
SyntaxError: invalid syntax

