#!/usr/bin/env python

print "hello"flynnk36@lg25-24:~ $ python
Python 2.7.12 (default, Jul 01 2016, 15:34:22) [GCC] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 2*3*6371
38226
>>> 3*6731**2
135919083
>>> 3*6371**2
121768923
>>> 575*24
13800
>>> 484400/575
842
>>> 384400-575*504
94600
>>> 932/138
6
>>> 932/139
6
>>> 2**32
4294967296
>>> 2**64
18446744073709551616L
>>> (a**b)**c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> a=1
>>> a
1
>>> a=2
>>> a=1
>>> b=2
>>> c=3
>>> (a**b)**c
1
>>> a**(b**c)
1
>>> a=2
>>> b=3
>>> c=3
>>> (a**b)**c
512
>>> a**(b**c)
134217728
>>> 2*3.14*6371
40009.880000000005
>>> 3.14*6371**2
127451472.74000001
>>> x=3
>>> y=4
>>> x
3
>>> y
4
>>> x*y
12
>>> x**2 + y**2
25
>>> radius=6371
>>> pi=3.14
>>> 2*pi*radius
40009.880000000005
>>> radius=696300
>>> 2*pi*radius
4372764.0
>>> goals=3
>>> points=1
>>> (2*goals)+(5*points)
11
>>> x=0
>>> x+1
1
>>> x+1
1
>>> x+1
1
>>> x=x+1
>>> 
>>> x=
  File "<stdin>", line 1
    x=
     ^
SyntaxError: invalid syntax
>>> x
1
>>> x=x+1
>>> x
2
>>> x=x+1
>>> x
3
>>> x=x+1%2
>>> x
4
>>> x=0
>>> x
0
>>> x=x+1%2
>>> x
1
>>> x=0
>>> x=x+1%1
>>> x
0
>>> x=x+1%2
>>> x
1
>>> x=x+1%2
>>> x
2
>>> x=x+1%2
>>> x
3
>>> x=x+1%3
>>> x
4
>>> x=0
>>> x=x+1%3
>>> s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
>>> x
1
>>> x=x+1%3
>>> x
2
>>> x=x+1%3
>>> x
3
>>> x=0
>>> x=(x+1)%2
>>> x
1
>>> x=(x+1)%2
>>> x
0
>>> control-d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'control' is not defined
>>> Control-d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Control' is not defined
>>> control_d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'control_d' is not defined
>>> 
flynnk36@lg25-24:~ $ cd
flynnk36@lg25-24:~ $ mkdir ca116
flynnk36@lg25-24:~ $ mkdir ca116/week-01
flynnk36@lg25-24:~ $ cd ca116/week-01
flynnk36@lg25-24:~/ca116/week-01 $ pwd
/users/ca1/flynnk36/ca116/week-01
flynnk36@lg25-24:~/ca116/week-01 $ gedit hello.py
python hello.py


