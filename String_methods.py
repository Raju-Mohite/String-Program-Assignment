Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'hello world'
'hello world'
>>> capitalize('hello world')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    capitalize('hello world')
NameError: name 'capitalize' is not defined
>>> a= 'hello world'
>>> a
'hello world'
>>> a.capitalize()
'Hello world'
>>> a
'hello world'
>>> b = "HELLO WORLD"
>>> b.lower()
'hello world'
>>> a
'hello world'
>>> a.upper()
'HELLO WORLD'
>>> c = 'python'
>>> c
'python'
>>> c.center(10,*)
SyntaxError: invalid syntax
>>> c.center(10,'*')
'**python**'
>>> c.center(8,'*')
'*python*'
>>> c.center(9,'*')
'**python*'
>>> c.center(7,'*')
'*python'
>>> c.center(5,'*')
'python'
>>> c.center(3,'*')
'python'
>>> a
'hello world'
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.count()
TypeError: count() takes at least 1 argument (0 given)
>>> a.count('l')
3
>>> a.count('d')
1
>>> a.index('o')
4
>>> a.index('r')
8
>>> a.finr('or')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.finr('or')
AttributeError: 'str' object has no attribute 'finr'
>>> a.find('or')
7
>>> b = '31/01/2022'
>>> b
'31/01/2022'
>>> b.replace('/','-')
'31-01-2022'
>>> b.split('/')
['31', '01', '2022']
>>> d = 'abc123'
>>> d
'abc123'
>>> d.isalnum()
True
>>> d = '12345'
>>> d
'12345'
>>> d.isnum()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d.isnum()
AttributeError: 'str' object has no attribute 'isnum'
>>> d.isnumeric()
True
>>> a
'hello world'
>>> a.islower()
True
>>> b
'31/01/2022'
>>> c
'python'
>>> d
'12345'
>>> a= "HOLLO WORLD"
>>> a
>>> a='Hello world'
>>> a.upper()
'HOLLO WORLD'
>>> a.isupper()
True
>>> 


