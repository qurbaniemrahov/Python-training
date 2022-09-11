Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = {"saylar":{"bir":1,"iki":2}, "meyveler":{"gilas":"yaz"}}
a["saylar"]
{'bir': 1, 'iki': 2}
a["saylar"["bir"]]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a["saylar"["bir"]]
TypeError: string indices must be integers
a["saylar"[0]]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a["saylar"[0]]
KeyError: 's'
a
{'saylar': {'bir': 1, 'iki': 2}, 'meyveler': {'gilas': 'yaz'}}
a["saylar"]["bir"]
1
a["meyveler"]
{'gilas': 'yaz'}
a["meyveler"]["gilas"]
'yaz'
a["meyveler"]["gilas"] = "armud'
SyntaxError: unterminated string literal (detected at line 1)
a["meyveler"]["gilas"] = "armud"
a
{'saylar': {'bir': 1, 'iki': 2}, 'meyveler': {'gilas': 'armud'}}
#dictionary methods
new_dictionary = {"bir":1,"iki":2,"uc":2}
new_dictionary.values
<built-in method values of dict object at 0x00000195B10732C0>
new_dictionary.values()
dict_values([1, 2, 2])
dict_values([1, 2, 2])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dict_values([1, 2, 2])
NameError: name 'dict_values' is not defined
new_dictionary.keys()
dict_keys(['bir', 'iki', 'uc'])
new_dictionary.items()
dict_items([('bir', 1), ('iki', 2), ('uc', 2)])
dict_items["bir"]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict_items["bir"]
NameError: name 'dict_items' is not defined
dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
my_dict = {"Emrahov":"Qurbani"}
my_dict.contains()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    my_dict.contains()
AttributeError: 'dict' object has no attribute 'contains'
my_dict.contains("Emrahov")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    my_dict.contains("Emrahov")
AttributeError: 'dict' object has no attribute 'contains'
