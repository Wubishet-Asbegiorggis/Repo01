import math
import time
import datetime
import calendar
import array
import sys
import abc
from functools import partial
from tkinter import *
from tkinter import messagebox
'''
# l0=[36,'python single string',"python double string"]
# l1=[36,'python single string',"python double string"]
# d0={1:"Name", 2:'ID No',3:"Nationality"}
# d1={1:"Name", 2:'ID No',3:"Nationality"}
# s0={ "Name","ID No","Age","Department","Salary"}
# s1={ "Name","ID No","Age","Department","Salary"}
# t0=(16,'Weekend Programming',"Programming with Python ")
# t1=(16,'Weekend Programming',"Programming with Python ")
# print(l0==l1)
# print(l0 is l1)
# print(d0==d1)
# print(d0 is d1)
# print(s0==s1)
# print(s0 is s1)
# print(t0==t1)
# print(t0 is t1)
#
# a=5712
# b=0
# q=a/b
# try:
#     q=a/b
#     print(q)
#     print("\n\t Devision by zero error occured !")
# except: #ZeroDivisionError
#     print("\n\t A number cannot be devided by Zero(0) !")
#     print("\t Error tye : Arithmetic Error !")
#
# finally:
#     print("\t Python Finally Block !")
# print("\t Quotient q equals : ",)
# assert b!=0," Division by Zero Error !"
# print(a/b)
#
# def funw_r():
#     v0=5.7587475
#     return v0
# def funw_nor():
#     v1=7.52367493864
# print("Functional output for function with return keyword : ",funw_r())
# print("Functional output for function with no return keyword : ",funw_nor())
#
# x=5.76458
# y=7.576435
# del x
# print("\t The value on y is :",y)
# Str0={1:"Name",2:"Age",3:"Salary",4:"Department",5:"Address"}
# print(Str0)
# del Str0[2]
# print(Str0)
#
# str1='String' \
#      ' literal ' \
#      ' with ' \
#      ' multiple' \
#      ' lines'
# str2="String" \
#      " literal" \
#      " with" \
#      " multiple" \
#      " lines"
# str3="'String" \
#      " literal" \
#      " with" \
#      " multiple" \
#      " lines"
# print(str1)
# print(str2)
# print(str3)
#
# u=0b111010
# v=0o1435
# w=0x23473264d
# x=2356476435.7635
# y=635.3754e2
# z=7.0+16.0j
# d=100.3746578765
# print(d,",",u,",",v,",",w,",",x,",",y,",",z,",",z.imag,",",z.real)
#
# x=(1==True)
# y=(False==5)
# z=(7==True)
# a=True+16
# b=False+16
# print("\t x :",x)
# print("\t y :",y)
# print("\t z :",z)
# print("\t a =",a)
# print("\t b =",b)
#
# Dct={'Name':" Yohannes",'Age':20,"Address":" Washington DC","SSN":' UGR/0593846/13'}
# print(Dct)
# print(Dct["SSN"])
# Dct["Age"]=22
# print(Dct["Address"])
# print(Dct["Age"])
#
# tp0=(365,'Tuple Element',"Tuple element with double quotes ")
# print(tp0[2])
#
# s0={"Scientist","Yohannes","Haileselassie"}
# print(s0)
#
# str0="Alemayehu","Bekele","Zeleke"
# print(str0[1])
#
# x=15
# y=4
# fd=x//y
# print(fd)
#
# 'Python comment with single quote string'
# "Python comment with double quote string"
# """Python comment with three triple quotes string"""
# def Sum():
#     '\t Python function to return the sum of two floating numbers'
#     a=342354.7654
#     b=43546.5423435
#     sum=a+b
#     return sum
# print("\t Sum equals :",Sum())
# print(Sum.__doc__)
#
# num=float(input("\n\t Enter the numerator : "))
# denom=float(input("\n\t Enter the denominator : "))
# qt=num/denom
# if(qt>=1 or qt<=-1):
#     print("\n\t The Fraction is a non-proper fraction !")
# else:
#     print("\n\t The fraction is a proper fraction !")
#
# i0=float(input("\n\t Enter the first number :"))
# i1=float(input("\t Enter the second number :"))
# i2=float(input("\t Enter the third number :"))
# if (i0>i1 and i0>i2):
#     if (i1>i2):
#         print("\t The first number is the largest number !")
#         print("\t The second number is the middle sized number !")
#         print("\t The third number is the smallest number !")
#     else:
#         print("\t The first number is the largest number !")
#         print("\t The third number is the middle sized number !")
#         print("\t The second number is the smallest number !")
# if(i0<i1 and i2<i1):
#         if(i2<i0):
#             print("\t The second number is the largest number !")
#             print("\t The first number is the middle sized number !")
#             print("\t The third number is the smallest number !")
#         else:
#             print("\t The second number is the largest number !")
#             print("\t The third number is the middle sized number !")
#             print("\t The first number is the smallest number !")
# if(i0<i2 and i1<i2):
#     if(i0<i1):
#         print("\t The third number is the largest number !")
#         print("\t The second number is the middle sized number !")
#         print("\t The first number is the smallest number !")
#     else:
#         print("\t The third number is the largest number !")
#         print("\t The first number is the middle sized number !")
#         print("\t The sceond number is the smallest number !")
#
# mark=float(input("\n\t Input the scored mark :"))
# if mark>=90 and mark<=100:
#     print("\t The grade for the scored mark is : A+")
# elif mark>=83 and mark<90:
#     print("\t The grade for the scored mark is : A")
# elif mark>=80 and mark<83:
#     print("\t The grade for the scored mark is : A-")
# elif mark>=75 and mark<80:
#     print("\t The grade for the scored mark is : B+")
# elif mark>=68 and mark<75:
#     print("\t The grade for the scored mark is : B")
# elif mark>=65 and mark<68:
#     print("\t The grade for the scored mark is : B-")
# elif mark>=60 and mark<65:
#     print("\t The grade for the scored mark is : C+")
# elif mark>=50 and mark<60:
#     print("\t The grade for the scored mark is : C")
# elif mark>=40 and mark<50:
#     print("\t The grade for the scored mark is : D")
# elif mark>=30 and mark<40:
#     print("\t The grade for the scored mark is : Fx")
# else:
#     print("\t Sorry, you failed the course. You should add the course again !")
#
# tup=[2,3,6,4,5,8,7,9,1,10]
# sqrd=[]
# for i in tup:
#     sqr=i**2
#     sqrd.append(sqr)
#
# print("\t Elements of the squared tuple are :",sqrd)
#
# str1="Summer Programming with Python !"
# for e in str1:
#     if e=="m":
#         print("\t Maximum achievement !")
#     else:
#         print("\t",e)
#
# tuple1 = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)
#
# # Initiating the loop
# for value in tuple_:
#     if value % 2 == 0:
#         print(value," is an even number")
#     # giving an else statement
#     else:
#      print(value," is an odd number")
#
# print(range(15))
# print(list(range(15)))
# print(list(range(5,16)))
# print(list(range(5,30,5)))
#
# str1="Python ","range","function","in","combination ","with ","len()","function !"
# for st in range(len(str1)):
#     print(str1[st].upper())
#
# i=0
# while i<5:
#     print("Python While loop !")
#     i+=1
#
# for ltr in "Test for Python Continue statement !":
#     if ltr== "o" or ltr == "p" or ltr == "t" or ltr=="e":
#          continue
#     else:
#      print('Current Letter is:',ltr)
#
# tuple2 = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)
# sum=0
# for i in  tuple2:
#     sum=sum+i**2
# print("\n\t The Sum of the squared elements is :",sum)
#
# import random
# numbers = [ ]
# for val in range(0, 11):
#     numbers.append(random.randint( 0, 11 ) )
# print(numbers)
#
# name1="Alemayehu"
# name2="Yohannes"
# Dict={"Abenezer":89, "Yohannes":96 , "Tewodros":85}
# def stMark(stName):
#     for name in Dict:
#      if name==stName:
#             print(f"\t The scored mark of {stName} is :",Dict[stName])
#             break
#     else:
#             print(f"\t There is no student named {stName} in the list !")
# stMark("Alemayehu")
#
# array=[21, 27,34,456,427,675,971,655,571,64571,793,69697]
# def primeCheck(num):
#     cond=0
#     factor=2
#     while factor<=num/2:
#         if num%factor==0:
#             cond=1
#             break
#         factor+=1
#     if cond==0:
#         print("\t",f"{num} is a prime number")
#     else:
#         print("\t",f"{num} is not a prime number")
# for n in array:
#     primeCheck(n)
#
# tup1=[5,7,2,3,9,7,6,8,1]
# sqrd=[]
# while tup1:
#     sqrd.append(tup1.pop()**2)
# print(sqrd)
#
# num1 = 9
# num2 = 14
# maximum_value = 4
# counter = 0
# while (counter < num1 or counter < num2) and not counter >= maximum_value: # grouping multiple conditions
#     print(f"Number of iterations: {counter}")
#     counter +=1
#
# tup4=[28,21,36,1000,19,999999998,8,6,4,9,-18, -1650, -1.000,2,5,3,1,10,16,28]
# sort=sorted(tup4)
# print(sort)
#
# n=1
# while 1:
#     i=1
#     while i<=10:
#        prod=n*i
#        print("\t",f"{n} ","x",f" {i}"," = "f"{prod}")
#        i+=1
#     opt=input("\t Do you want to continue printing the table ? If No press n, If Yes press any key !")
#     if opt=="n":
#         print("\t Progress terminated !")
#         break
#     else:
#         n+=1
#
# str0='\n\t Jo Biden said, "Welcome the new hero of our world !"'
# str2="\t Donald Trump said,'USA will prevail forever !'"
# str3="\t Thomas Jefferson said,\"Little patience overweights gallons of arrogance !\""
# print(str0)
# print(str1)
# print(str2)
#
# list0 = [1, 2, 3, 4, 5, 6]
# print(list0)
# del list0[3]
# print(list0)

list0 = [" \t John", "\t David", "\t James", "\t Jonathan"]
print("\n\tThe original elements:-")
for i in list0:
    print(i)
print("\n\tAfter removing one element:-")
list0.remove("\t David")
for i in list0:
    print(i)

str = "Johnson"
s = list(str)
print(type(s))
print(s)

l0 =[]
#Number of elements will be entered by the user
n = int(input("\n\t Enter the number of elements in the list :"))
# for loop to take the input
for i in range(0,n):
    # The input is taken from the user and added to the list as the item
    l0.append(input(f"\t Enter element {i+1}: "))
print("\n\t Elements of the list are:-")
# traversal loop to print the list items
for i in l0:
    print(i, end = "  ")

print("\n")
l1=[1,3,7,4,5,2,10]
l2=[7,12,15,9,10,2]
k=0
for i in l1:
    for j in l2:
        if i==j:
            k+=1
            print(f"\t Common element {k}: ",j)

tuple_ = ("Python", "Tuple", "Ordered", "Collection")

print(tuple_[0])
print(tuple_[1])
# trying to access element index more than the length of a tuple
try:
    print(tuple_[5])
except Exception as e:
    print(e)
# trying to access elements through the index of floating data type
try:
    print(tuple_[1.0])
except Exception as e:
    print(e)

# Creating a nested tuple
nested_tuple = ("Tuple", [4, 6, 2, 6], (6, 2, 6, 7))

# Accessing the index of a nested tuple
print(nested_tuple[0][3])
print(nested_tuple[1][1])

def function(num1, num2):
    print("num1 is: ", num1)
    print("num2 is: ", num2)

# Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30
print("Passing out of order arguments")
function(30, 20)

# Calling function and passing only one argument
print("Passing only one argument")
try:
    function(30)
except Exception as e:
    print(e)

def fun0(*args):
#    res=[]
    for i in args:
#       res.append(args)
     return args
print(fun0("Abebayehu",'Bekele','Ephrem','Gebeyehu','Tewodros','Yohannes','Haileselassie'))
print(fun0(1,3,5,7,9,2,4,6,8,10,16,19,21,25,27,28,30,36,"Multiple arguments"))

print(format(12,"b"))

# opens p0.py file of the current directory
f = open("p0.py")
print("\n\t File opened !")

print(complex(5))
print(complex(5,7))

class Student:
    id = 101
    name = "Pranshu"
    email = "pranshu@abc.com"
# Declaring function
    def getinfo(self):
        print(self.id, self.name, self.email)
s = Student()
s.getinfo()

print(divmod(17,5))


print(list(enumerate([1,2,3])))

   def filterdata(x):

        for i in x:
        if i>5:
            print(i)
# Calling function
result = (1,2,6,16,21,25)
# Displaying result
print(filterdata(result))

l1={5,3,7,9,943,34,0,-1,-7,567,-46575,545,456,34,3453,932348576748}
print(sorted(l1))

class A:
    a=5
    b=7
    sum=a+b
    print("\n\t The Sum is : ",sum)

print(set(zip([1,2,3,4,5,6,7,8,9,10],["One","Two","Three","Four","Five","Six","Seven","Eight","Nine", "Ten"])

print("\n\t The Square root of 81 is:",math.sqrt(81))
from math import *
print("\t The Square root of 36 is:",sqrt(36))

import sys
print(sys.path)

print("\n\t Functions in math header file:",dir(math))

n=5
def funinc():
    m=65/n
    print(m)
    print(n)
funinc()
print(n)
num=6
def funinc1():
    global num
    num+=2
    print(num)
funinc1()
print(num)

n=7
try:
    print(m=n/0)
except Exception as e:
    print(e)

list=[3,5,7,1]
if len(list)<5:
    raise Exception(f"\n\t The length of the list should have been greater than or equal to 5, but is: {len(list)}")

print(time.time())  #The time since 12 pm, jan 1, 1970.
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(datetime.datetime.now())
print(datetime.datetime(2022,9,17,1,17,36,90000))
print(calendar.month(2022,9))
print(calendar.prcal(2022))

arr=array.array("f",[5,7,2,3,1,9,4,7,8,16,21,28])
print(arr[10])
arr1=array.array("f",[4,54,75,8,97,56,57])
print(arr1[6])
arr2=array.array("i",[])
arr2=arr+arr1
print(arr2)

print(type(sys.argv))
for i in sys.argv:
    print(i)

class cl0:
    def _init_(self,name,ssn,department):
        self.name
        self.ssn
        self.department
    def display(arg):
        print("Name:%s\n SSN:%i\n Department:%s",arg.name,arg.ssn,arg.department)
object=cl0("TEWODROS",12131621252836,"COMPUTER_SCIENCE")
object.display()

n="GEORGE WASHINGTON"
ssn=12131621252836
dep="COMPUTER SCIENCE"
print("Name: %s\n ID: %i\n Department: %s" %( n,ssn,dep))

class cl1:
    def _init_(self):
        print("\n\t First Constructor !")
    def _init_(self):
        print("\n\t Second Constructor !")
    def disp(ob):
        print("\n\t First function !")
    def disp(ob):
        print("\n\t Second function !")
obj=cl1()
print(obj._init_())
obj.disp()

class abscl(abc.ABC):
    def polygon(arg):
        pass
class triang(abscl):
    def polygon(arg): # Method Overriding and Abstraction in python.
        print("\n\t Triangle has 3 sides.")
class sqr(abscl):
    def polygon(arg):
        print("\n\t Square has 4 sides.")
class pentag(abscl):
    def polygon(arg):
        print("\n\t Pentagon has 5 sides.")
class hexag(abscl):
    def polygon(arg):
        print("\n\t Hexagon has 6 sides.")
class circ(abscl):
    def polygon(arg):
        print("\n\t Circle has an infinite number of sides.")
Ob=abscl()   # Since abstracts can't be instantiated, objects for abstract classes cannot be created !
Ob.polygon
Ot=triang()  # Since abstracts can't be instantiated, objects for abstract classes cannot be created !
Ot.polygon
Os=sqr()     # Since abstracts can't be instantiated, objects for abstract classes cannot be created !
Os.polygon
Op=pentag()  # Since abstracts can't be instantiated, objects for abstract classes cannot be created !
Op.polygon
Oh=hexag()   # Since abstracts can't be instantiated, objects for abstract classes cannot be created !
Oh.polygon
Oc=circ()    # Since abstracts can't be instantiated, objects for abstract classes cannot be created !
Oc.polygon

Appw=Tk()
Appw.mainloop()

Wobj=Tk()                                                
GreenButton=Button(Wobj,text="Green",fg="green")         # ---> python tkinter Button() widget.
GreenButton.pack(side="top")                             # Function of tkinter pack() method --> Geometric pack
YellowButton=Button(Wobj,text="Black",fg="black")
YellowButton.pack(side="left")
BlueButton=Button(Wobj,text="Blue",fg="blue")
BlueButton.pack(side="right")
RedButton=Button(Wobj,text="Red",fg="red")
RedButton.pack(side="bottom")
Wobj.mainloop()

Obj=Tk()  # Function of grid() method --> Geometric grid
name=Label(Obj,text="Name",fg="green").grid(row=0,column=0)
password=Label(Obj,text="Password",fg="green").grid(row=1,column=0)
e1=Entry(Obj).grid(row=0,column=1)                            
e2=Entry(Obj).grid(row=1,column=1)
submit=Button(Obj,text="Submit",fg="red").grid(row=5,column=0)
Obj.mainloop()

Ob=Tk()
Ob.geometry("500x500") 
name=Label(Ob,text="Name",fg="green").place(x=80,y=90)  # ---> python tkinter Label() widget.
e1=Entry(Ob).place(x=140,y=90)
email=Label(Ob,text="Email",fg="green").place(x=80,y=130)
e2=Entry(Ob).place(x=140,y=130)
password=Label(Ob,text="Password",fg="green").place(x=80,y=180)
e3=Entry(Ob).place(x=140,y=180)
sumbit=Button(Ob,text="Submit",fg="red").place(x=100,y=250)
Ob.mainloop()

bto=Tk()                        #Position of default  pack() method -->Geometric pack
bto.geometry("300x300")
btn=Button(bto,text="BUTTON",fg="red")
btn.pack()
bto.mainloop()

ob0=Tk()
ob0.geometry("500x500")
def fun0():
    messagebox.showinfo("Hello !","NORTH Button Clicked !")
b0=Button(ob0,text="NORTH",command=fun0,fg="green",bg="pink",padx=0,pady=0)  
b0.pack(side=TOP)
def fun1():
    messagebox.showinfo("Hi !","SOUTH Button Clicked !")
b1=Button(ob0,text="SOUTH",command=fun1,fg="blue",bg="pink",padx=0,pady=0)
b1.pack(side=BOTTOM)
def fun2():
    messagebox.showinfo("Alert !","WEST Button Clicked !")
b2=Button(ob0,text="WEST",command=fun2,fg="black",bg="pink",padx=0,pady=0)
b2.pack(side=LEFT)
def fun3():
    messagebox.showinfo("Notice !","EAST Button Clicked !")
b3=Button(ob0,text="EAST",command=fun3,fg="red",bg="pink",padx=0,pady=0)
b3.pack(side=RIGHT)
def fun4():
    messagebox.showinfo("Warning !","CENTER Button Clicked !")
b4=Button(ob0,text="CENTRE",command=fun4,fg="green",bg="pink").place(x=612,y=305)
ob0.mainloop()

Cvobj=Tk()
Cvobj.geometry("500x500")
c=Canvas(Cvobj,bg="pink",height=200)             # ---> python tkinter Canvas() widget.
c.pack()
Cvobj.mainloop()

co=Tk()
co.geometry=("500x500")
c=Canvas(co,bg="pink",height=200,width=200)
arc=c.create_arc((10,15,150,200),start=0,extent=150,fill="green") # --> Different shapes can be created by altering the values of start and extent.
c.pack()
co.mainloop()

cho=Tk()
cho.geometry("500x500")
                                               # ---> python tkinter Checkbutton() widget.
chb=Label(cho,text="Select among the following programming languages ",fg="green",bg="white",height=3)
chb0=Checkbutton(cho,text="C",fg="green",bg="pink",height=5,width=5)
chb1=Checkbutton(cho,text="C++",fg="green",bg="yellow",height=5,width=5)
chb2=Checkbutton(cho,text="Java",fg="green",bg="pink",height=5,width=5)
chb3=Checkbutton(cho,text="Python",fg="green",bg="yellow",height=5,width=5)
bt=Button(cho,text="SUBMIT",fg="red",bg="white",height=6,width=10)
chb.pack()
chb0.pack()
chb1.pack()
chb2.pack()
chb3.pack()
bt.pack()
cho.mainloop()

frmo=Tk()
frmo.geometry("500x500")   
frame=Frame(frmo).pack()          # ---> python tkinter Frame() widget.
frmo.mainloop()

frmob=Tk()
frame=Frame().pack()
frmob.geometry("500x500")
bt0=Button(frame,text="SPRING",fg="green",bg="yellow").pack(side=TOP)
bt1=Button(frmob,text="AUTUMN",fg="black",bg="orange").pack(side=LEFT)
bt2=Button(frame,text="SUMMER",fg="blue",bg="pink").pack(side=BOTTOM)
bt3=Button(frmob,text="WINTER",fg="black",bg="white").pack(side=RIGHT)
bt4=Button(frmob,text="SEASONS OF THE YEAR",fg="green",cursor="circle",font="15").place(x=590,y=315)
frmob.mainloop()

lbo=Tk()
lbl=Label(lbo,text="List of Favourite Countries ")
lb=Listbox(lbo)                                   # ---> python tkinter Listbox() widget.
lb.insert(1,"Ethiopia")
lb.insert(2,"USA")
lb.insert(3,"India")
lb.insert(4,"Britain")
lb.insert(5,"Israel")
lb.insert(6,"Russia")
lb.insert(7,"Canada")
lbtn=Button(lbo,text="Delete",fg="green",bg="pink",command=lambda argument=lb:argument.delete(ANCHOR))
lbl.pack()
lb.pack()
lbtn.pack()

def funsm(lblsm, n1, n2): # ---> Simple Calculator using python Button(),Label(),partial(),config(),title() and Entry() methods and widgets.
    num1=(n1.get())
    num2=(n2.get())
    ressm=float (num1) + float (num2)
    lblsm.config(text=" Sum = %f" % ressm, fg="blue", bg="white")
def fundf(lbldf, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    resdf = float (num1) - float (num2)
    lbldf.config(text=" Difference = %f" % resdf,fg="blue",bg="white")
def funpr(lblpr, n1, n2):
        num1 = (n1.get())
        num2 = (n2.get())
        respr = float (num1) * float (num2)
        lblpr.config(text=" Product = %f" % respr,fg="blue",bg="white")
def funqt(lbldv, n1, n2):
        num1 = (n1.get())
        num2 = (n2.get())
        resdv = float (num1) / float (num2)
        lbldv.config(text=" Quotient = %f" % resdv, fg="blue", bg="white")
def funrem(remvar, n1, n2):
    num1=(n1.get())
    num2=(n2.get())
    resrem=float (num1) % float (num2)
    remvar.config(text="Remainder = %f"%resrem,fg="blue",bg="white")
calo=Tk()
calo.geometry("500x500")
calo.title("       SIMPLE CALCULATOR : ~")
number1=StringVar()
number2=StringVar()
labelNum1=Label(calo,text="Enter the first number ",fg='black',bg="white").place(x=10,y=50)
labelNum2=Label(calo,text="Enter the second number",fg="black",bg="white").place(x=10,y=90)
resultPosition=Label(calo)
resultPosition.place(x=80,y=180)
entryNum1=Entry(calo,textvariable=number1).place(x=150,y=50)      # ---> python tkinter Entry() widget.
entryNum2=Entry(calo,textvariable=number2).place(x=150,y=90)
probsm=partial(funsm,resultPosition,number1,number2)
probdf=partial(fundf,resultPosition,number1,number2)              # python functool's partial() method.
probpr=partial(funpr,resultPosition,number1,number2)
probdv=partial(funqt,resultPosition,number1,number2)
probrem=partial(funrem,resultPosition,number1,number2)
btnCal=Label(calo,text="Choose Operator",fg="green",bg="white").place(x=10,y=130)
btnSum=Button(calo,text="+",fg="blue",bg="white",command=probsm).place(x=120,y=130)
btnDiff=Button(calo,text="-",fg="blue",bg="white",command=probdf).place(x=150,y=130)
btnProd=Button(calo,text="x",fg="blue",bg="white",command=probpr).place(x=180,y=130)
btnDiv=Button(calo,text="/",fg="blue",bg="white",command=probdv).place(x=210,y=130)
btnrem=Button(calo,text="%",fg="blue",bg="white",command=probrem).place(x=240,y=130)
calo.mainloop()

mnbto=Tk()
mnbto.geometry("500x500")
mnbtv=Menubutton(mnbto,text="Favourite Languages")  #--> relief = FLAT by default.
mnbtv.grid() 
#mnbtv.menu=Menu(mmnbtv)                     # python Menubutton() widget.       
#mnbtv["menu"]=mnbtv.menu
#mnbtv.menu.add_command(label="English")
#mnbtv.menu.add_radiobutton(label="Amharic")
#mmnbtv.menu.add_cascade(label="Hindi")
mnbtv.pack()
mnbto.mainloop()

mno=Tk()
mno.geometry("500x500")
def menufun():
    print("Hello !")
menv=Menu(mno)
menv.add_cascade(label="Print->Hello !",command=menufun)
menv.add_command(label="Quit",command=mno.quit)
mno.config(menu=menv)
mno.mainloop()

mo=Tk()
mo.geometry("500x500")
mnv=Menu(mo)                        # python tkinter Menu() widget.
fx=Menu(mnv,tearoff=0)                         
fx.add_command(label="Desktop")
fx.add_command(label="Documents")
fx.add_command(label="Downloads")
fx.add_command(label="Music")
fx.add_command(label="Pictures")
fx.add_command(label="Videos")
fx.add_command(label="Windows(C:)")
fx.add_command(label="New Volume(D:)")
fx.add_command(label="Network")
fx.add_cascade(label="Linux")
fx.add_command(label="Dropbox")
fx.add_command(label="OneDrive - personal")
fx.add_separator()
fx.add_command(label="Exit",command=mo.quit)
mnv.add_cascade(label="File Explorer",menu=fx)
pc=Menu(fx,tearoff=0)
pc.add_command(label="Desktop")
pc.add_command(label="Documents")
pc.add_command(label="Downloads")
pc.add_command(label="Music")
pc.add_command(label="Pictures")
pc.add_command(label="Videos")
pc.add_command(label="Windows(C:)")
pc.add_command(label="New Volume(D:)")
pc.add_command(label="Network")
pc.add_separator()
pc.add_cascade(label="Exit",command=pc.quit)
mnv.add_cascade(label="This PC",menu=pc)
fl=Menu(pc,tearoff=0)
fl.add_command(label="New")
fl.add_command(label="Open")
fl.add_command(label="Save")
fl.add_command(label="Save as ...")
fl.add_command(label="Close")
fl.add_separator()
fl.add_command(label="Exit",command=fl.quit)
mnv.add_cascade(label="File",menu=fl)
ed=Menu(mo,tearoff=0)
ed.add_command(label="Undo")
ed.add_separator()
ed.add_command(label="Cut")
ed.add_command(label="Copy")
ed.add_command(label="Paste")
ed.add_command(label="Delete")
ed.add_command(label="Select All")
ed.add_separator()
ed.add_command(label="Exit",command=ed.quit)
mnv.add_cascade(label="Edit",menu=ed)
hp=Menu(mnv,tearoff=0)
hp.add_command(label="About")
hp.add_separator()
hp.add_command(label="Exit", command=hp.quit)
mnv.add_cascade(label="Help",menu=hp)   # add_Cascade() method is used to create a menu taking a another menu as its argument, unlike add_command() nethod.
mo.config(menu=mnv)
mo.mainloop()

msgob=Tk()
msgob.geometry("500x500")      # python tkinter Message() widget.
msgv=Message(msgob,text="Welcome to Python tkinter's Message() widget !")
msgv.pack()
msgob.mainloop()

def rdfun():
    pstlbl.config(text="You Selected Option : "+str(rdv.get()),fg="green",bg="yellow")
rdob=Tk()
rdob.geometry("500x500")     # python tkinter Radiobutton() widget.
rdv=StringVar()
rdlbl=Label(text="Among the following select your favourite programming language",fg="green",bg="yellow")
rd1=Radiobutton(rdob,text="C",fg="green",bg="white",variable=rdv,value=1,command=rdfun)
rd2=Radiobutton(rdob,text="C++",fg="green",bg="white",variable=rdv,value=2,command=rdfun)
rd3=Radiobutton(rdob,text="Java",fg="green",bg="white",variable=rdv,value=3,command=rdfun)
rd4=Radiobutton(rdob,text="Python",fg="green",bg="white",variable=rdv,value=4,command=rdfun)
rd5=Radiobutton(rdob,text="C#",fg="green",bg="white",variable=rdv,value=5,command=rdfun)
rd6=Radiobutton(rdob,text="JavaScript",fg="green",bg="white",variable=rdv,value=6,command=rdfun)
pstlbl=Label(rdob)
rdlbl.pack()
rd1.pack(anchor=W)
rd2.pack(anchor=W)
rd3.pack(anchor=W)
rd4.pack(anchor=W)
rd5.pack(anchor=W)
rd6.pack(anchor=W)
pstlbl.pack()
rdob.mainloop()

def sclfun():                               # python tkinter Scale() widget.
    sclpst.config(text="Scale = "+str(sclv.get()),fg="green",bg="white")
sclob=Tk()
sclob.geometry("500x500")              
sclv=DoubleVar()
sc1=Scale(sclob,fg="black",bg="white",variable=sclv,from_=0,to=1000000,orient=HORIZONTAL)
scbtn=Button(sclob,text="VALUE",fg="green",bg="yellow",command=sclfun)
sclpst=Label(sclob)
sc1.pack(anchor=CENTER)
scbtn.pack(anchor=CENTER)
sclpst.pack()
sclob.mainloop()

scbro=Tk()
scbro.geometry("500x500")
scbrv=Scrollbar(scbro)                # python tkinter Scrollbar() widget.
scbrv.pack(side=RIGHT,fill=Y)
scrls=Listbox(scbro,yscrollcommand=scbrv.set,height=30,width=30)
for i in range(100):
    scrls.insert(END,"Number  "+str(i+1))
scrls.pack(side=LEFT)
#scbro.config(command=scrls.yview)
scbro.mainloop()

txtob=Tk()
txtob.geometry("500x500")              # python tkinter Text() widget.
txtv=Text(txtob)
txtv.insert(INSERT,"<-------> Name ")
txtv.insert(END,"<-------> Salary <-------> ")
txtv.pack()
txtv.tag_add("Write Here","1.0","1.4")
txtv.tag_add("Click Here","1.8","1.13")
txtv.tag_config("Write here",background="white",foreground="black")
txtv.tag_config("Click here",foreground="green",background="white")
txtob.mainloop()

def tplfun():
    tplv=Toplevel(tplob)                # python tkinter Toplevel() widget.
    tplob.mainloop()
tplob=Tk()
tplob.geometry("500x500")
tpbtn=Button(tplob,text="Open",command=tplfun)
tpbtn.pack()
tplob.mainloop()

spob=Tk()                              
spob.geometry("500x500")                # python tkinter Spinbox() widget.
spv=Spinbox(spob,from_=0,to=25,fg="black",bg="yellow")
spv.pack()
spob.mainloop()

def pwfun():
    num1=int(e1.get())
    num2=int(e2.get())
    lfdt=str(num1+num2)
    lf.insert(1,lfdt)
pwob=Tk()
pwob.geometry("500x500")                # python tkinter PanedWindow() widget.
pw1=PanedWindow(pwob)                 
pw1.pack()
lf=Entry(pwob)
pw1.add(lf)
pw2=PanedWindow(pwob,orient=VERTICAL)
pw1.add(pw2)
e1=Entry(pwob,fg="black",bg="white")
e2=Entry(pwob,fg="black",bg="white")
pw2.add(e1)
pw2.add(e2)
pwbtn=Button(pwob,text="ADD",command=pwfun,fg="green",bg="white")
pw2.add(pwbtn)
pwob.mainloop()

lblfmob=Tk()                             # python tkinter LabelFrame() widget.
lblfmob.geometry("500x500")
lblfmv1=LabelFrame(lblfmob,text=" LOW LEVEL PROGRAMMING LANGUAGES ")
lblfmv1.pack(fill=Y,expand="yes")
lbfmlb1=Label(lblfmv1,text=" Comment Section for low level programming languages")
lbfmlb1.pack(side=LEFT)
lblfmv2=LabelFrame(lblfmob,text=" HIGH LEVEL PROGRAMMING LANGUAGES ")
lblfmv2.pack(fill=Y,expand="yes")
lbfmlb2=Label(lblfmv2,text=" Comment section for high level programming languages ")
lbfmlb2.pack(side=LEFT)
lblfmob.mainloop()

                            # python's Messagebox Widget with different methodss.
msgbxshwinfo=Tk()
msgbxshwinfo.geometry("500x500")
messagebox.showinfo("             1.  NOTICE"," You are programming with showinfo() messagebox widget.")
msgbxshwinfo.mainloop()

msgbxshwarn=Tk()
msgbxshwarn.geometry("500x500")
messagebox.showwarning("          2.  WARNING ","Battery is running low !")
msgbxshwarn.mainloop()

msgbxsherr=Tk()
msgbxsherr.geometry("500x500")
messagebox.showerror("            3.  ERROR","Error encounterred with showerror() method !")
msgbxsherr.mainloop()

msgbxaskqt=Tk()
msgbxaskqt.geometry("500x500")
messagebox.askquestion("          4.  CONFIRM ","Do you have the commitmemt to continue as a programmer ?")
msgbxaskqt.mainloop()

msgbxaskokcanc=Tk()
msgbxaskokcanc.geometry("500x500")
messagebox.askokcancel("           5.  OK/CANCEL ","Loading python programming with askokcancel() method ! ")
msgbxaskokcanc.mainloop()

msgbxaskyn=Tk()
msgbxaskyn.geometry("500x500")
messagebox.askyesno("            6.  YES/NO","Do you need to continue with python askyesno() method ?")
msgbxaskyn,mainloop()

msgbxretrcanc=Tk()
msgbxretrcanc.geometry("500x500")
messagebox.askretrycancel("      7.   RETRY/CANCEL","Do you need to Retry progrommimg with python Tkinter ?")
msgbxretrcanc.mainloop()
'''
