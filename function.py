
from pickle import TRUE
from tkinter import FALSE

#here are some function of python
a=-23
print(abs(a))
b=[TRUE,TRUE]
c=[FALSE,FALSE,TRUE]
print(all(b))
print(all(c))
print(ascii("my name is nitin"))
print(ascii('d'))
print(bool(1)) #it does not matches with false criteria
print(bool(0))
x=('apple','banana','cherry')
y=enumerate(x)
for i in y:
    print(i)
print(format(0.5,'%'))#function format formats the value ,it convert the 0.5 to 50%
print(format(45,'b'))# it convert 45 to binary

