#!/usr/bin/env python
print "hello"

keoghk22@lg25-47:~ $ python
Python 2.7.12 (default, Jul 01 2016, 15:34:22) [GCC] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 * 3 * 6371
38226
>>> 3 * 6371 * 6371
121768923
>>> 
>>> # task 2
... 
>>> d = 384400
>>> speed = 575km/hr
  File "<stdin>", line 1
    speed = 575km/hr
                ^
SyntaxError: invalid syntax
>>> 
>>> s = 575
>>> 
>>> 24 * s
13800
>>> d / 13800
27
>>> 13800 * 21
289800
>>> d - 289800
94600
>>> 94600 / 24
3941
>>> 
>>> #task 3 
... 
>>> 
>>> 
>>> 
>>> 931 / 2 
465
>>> 931 / 3
310
>>> 931%3
1
>>> # 2nd persn is chosen
... 
>>> #task 4
... 
>>> #part 1 above
... 
>>> 931%4
3
>>> 931%5
1
>>> 
>>> 
>>> # task 5 
... 
>>> 2 ** 32
4294967296
>>> 
>>> 2 ** 64
18446744073709551616L
>>> 
>>> (2 ** 2 ) ** 2
16
>>> 2 **( 2 ** 2)
16
>>> 2 **( 3 ** 4)
2417851639229258349412352L
>>> 
>>> 
>>> # task 7
... 
>>> r = 6371
>>> x = 3.14
>>> 
>>> 2 * x * r
40009.880000000005
>>> 
>>> x * r ** 2
127451472.74000001
>>> (x * r ** 2)/ 2
63725736.370000005
>>> 
>>> 
>>> 
>>> 
>>> x = 3
>>> y = 4
>>> x * y
12
>>> x **2 + y**2
25
>>> 
>>> r = 6371
>>> pi = 3.14 
>>> 
>>> 2 * pi * r
40009.880000000005
>>> 
>>> goals = 3
>>> points = 1
>>> 
>>> 5 * goals + 4 * points 
19
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x = 0
>>> x = 0 + 1
>>> 
KeyboardInterrupt
>>> x = 0
>>> x + 1
1
>>> x
0
>>> x +1 
1
>>> x = x +1 
>>> x + 1
2
>>> x + 0 
1
>>> 
>>> x = 0
>>> (x + 1)%x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> 
>>> (x + 1)% x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> x = x + 1
>>> (x + x)% x
0
>>> (x + x)% x
0
>>> x + 1 
2
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x = 0
>>> x%2
0
>>> x%2
0
>>> 2 % x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x = 0 
>>> 
>>> x + 1
1
>>> x%1
0
>>> 
>>> 
>>> 
>>> x%1
0
>>> x= o 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'o' is not defined
>>> x = 0
>>> x%3(x + 2) + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> 
keoghk22@lg25-47:~ $ cd
keoghk22@lg25-47:~ $ mkdir ca116
keoghk22@lg25-47:~ $ cd mkdir ca116
bash: cd: mkdir: No such file or directory
keoghk22@lg25-47:~ $ cd
keoghk22@lg25-47:~ $ mkdir ca116
mkdir: cannot create directory ‘ca116’: File exists
keoghk22@lg25-47:~ $ cd ca116
keoghk22@lg25-47:~/ca116 $ mkdir ca116/week-01
mkdir: cannot create directory ‘ca116/week-01’: No such file or directory
keoghk22@lg25-47:~/ca116 $ ~
bash: /users/ca1/keoghk22: Is a directory
keoghk22@lg25-47:~/ca116 $ cd
keoghk22@lg25-47:~ $ cd ca116
keoghk22@lg25-47:~/ca116 $ mkdir ca116/week-01
mkdir: cannot create directory ‘ca116/week-01’: No such file or directory
keoghk22@lg25-47:~/ca116 $ cd
keoghk22@lg25-47:~ $ mkdir ca116/week-01
keoghk22@lg25-47:~ $ cd ca116/week-01
keoghk22@lg25-47:~/ca116/week-01 $ pwd
/users/ca1/keoghk22/ca116/week-01
keoghk22@lg25-47:~/ca116/week-01 $ gedit hello.py &
[1] 3982
keoghk22@lg25-47:~/ca116/week-01 $ python hello.py

