import tkinter 
from tkinter import *
from tkinter import font
from datetime import date
import time
import math
import cmath
import datetime
import statistics
from statistics import *
from tkinter import ttk
from tooltip import *
import calendar
from tkinter import messagebox




#---------------main window -------------

root=Tk()
root.title("Scientific Calculator")
root.geometry("630x580")
root.iconbitmap("img.ico")
root.configure(bg="#1e3d59")
root.resizable(False,False)

#---------------Font--------------
f=font.Font(family='LCDMono2',size=20,weight='bold')
ff1=font.Font(family='Century',size=25,weight='bold')
f1=font.Font(family='Calibri (Body)',size=20,weight='bold')
f2=font.Font(family='Arial italic',size=8,weight='normal')
font.families()

#----------------------------------design purpose label--------------------
dl=Label(root,text='',bg='#30475e').grid(row=0,column=0)

#---------------------------------calculator name------------------------
name=Label(root,font=f1,text='PDA',fg='#ff6e40',bg='#1e3d59')
name.place(x=20,y=15)

small=Label(root,font=f2,text='Scientific Calculator',bg='#1e3d59',fg='#e8e8e8')
small.place(x=45,y=45)

#----------------------Weekday--------------
now=datetime.datetime.now()
now=now.strftime("%A ,")
week=Label(root,text=now,font=('Arial',16),bg='#1e3d59',fg='#f5f0e1')
week.place(x=200,y=30)


#---------------------Date-------------------

today=date.today()
today=today.strftime("%dth %b,%Y")
date_label=Label(root,text=today,font=('Arial',16),bg='#1e3d59',fg='#f5f0e1')
date_label.place(x=290,y=30)


#-------------------Time---------------------
def my_watch():
    x=time.strftime("%H:%M:%S")
    clock.config(text=x)
    clock.after(200,my_watch)

clock=Label(root,font=f,bg='#1e3d59',fg='#19d3da')
clock.place(x=480,y=30)
my_watch()

#------------------START CALCULATOR JOURNEY------
text_input=StringVar()
enter=Entry(root,bd=10,width="29",insertwidth=4,font=ff1,bg='#cdc9c3',text=text_input)
enter.place(x=31,y=100)

#------------Start Button----------------------

#----------------LEFT SIDE--------------
squaret=Button(root,text='√Sqrt',font=("Arial",12,"bold"),bg="#aed6dc",padx="3",fg="black",command=lambda : sq())
squaret.place(x=30,y=200)
CreateToolTip(squaret,"Enter a value\nfind root of a value\nfor example: √4=2")
def sq():
    try:
        s=text_input.get()
        if '-' in s:
            messagebox.showerror("Error",'Cannot be determined!')
        elif '.' in s:
            s=float(s)
            s=math.sqrt(s)
            s=str(s)
            text_input.set(s)
        else:
            s=int(s)
            s=math.sqrt(s)
            s=str(s)
            text_input.set(s)
    except:
        messagebox.showerror("Error","Envalid")

#power
power=Button(root,text='Pow',bg='#aed6dc',fg='black',font=("Arial",12,"bold"),padx="7",command=lambda : num('^'))
power.place(x=100,y=200)
CreateToolTip(power,"Find x to the power y\nFor example: 2^3=8")
def calpow(s):
    try:
        a=s.split('^')
        a=[int(i) for i in a ]
        a,b=a
        c=math.pow(a,b)
        text_input.set(c)
    except:
        messagebox.showerror("Error","Enter value as 2^3 and click enter button.")

#log
loog=Button(root,text='Log',bg='#aed6dc',fg='black',font=("Arial",12,"bold"),padx="7",command=lambda : logg())
loog.place(x=170,y=200)
CreateToolTip(loog,"Given value then , and base.\nEnter log button.\nFor example:3,10=0.477....")
def logg():
    try:
        s=text_input.get()
        if '-' in s:
            messagebox.showerror("Error","Cann't be determined")
        elif '.' in s:
            messagebox.showerror("Error","Cann't be determined")
        else:
            a=s.split(',')
            a=[int(i) for i in a ]
            a,b=a
            text_input.set(str(math.log(a,b)))
    except:
        messagebox.showerror("Error","Enter value and base: value:2, base=10")  


#-------------------,--------------
coma=Button(root,text=',',padx="16",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : num(','))
coma.place(x=240,y=200)
CreateToolTip(coma,"Use for comma. ,")



#e to the power x
ex=Button(root,text='e^x',padx="10",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : e())
ex.place(x=30,y=260)
CreateToolTip(ex,"Enter a value.\nFind e to the power x")
def e():
    try:
        s=text_input.get()
        if '.' in s:
            s=float(s)
        else:
            s=int(s)
        s=math.exp(s)
        global operator
        operator=''
        text_input.set(str(s))
    except:
        messagebox.showerror("Error","Envalid")

#-----------------------e--------------
fe=Button(root,text='e',padx="20",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : ie())
fe.place(x=100,y=260)
CreateToolTip(fe,"e=2.71------")
def ie():
    num(math.e)

#---------------factorial------------
fact=Button(root,text='X!',padx="14",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : f(text_input.get()))
fact.place(x=170,y=260)
CreateToolTip(fact,"Enter a number.\nThen,Enter X! button.")
def f(a):
    try:
        if '.' in a:
            messagebox.showinfo("Error","Factorial Cann't be determined float and negative values!") 
        elif '-' in a:
            messagebox.showinfo("Error","Factorial Cann't determined float and negative value!") 
        else:
            s=math.factorial(int(a))
            text_input.set(str(s))
    except:
        messagebox.showerror("Error","Envalid")


#----------------pi----------------
pai=Button(root,text='PI',padx="10",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : pie())
pai.place(x=240,y=260)
CreateToolTip(pai,"3.1416..........")
def pie():
    num(math.pi)


#--------------------sin--------------
sine=Button(root,text='Sin',padx="10",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : sinn())
sine.place(x=30,y=320)
CreateToolTip(sine,"Enter a value. \n click sin button")
def sinn():
    try:
        s=text_input.get()
        if '.' in s:
            s=float(s)
        else:
            s=int(s)
        s=math.sin(math.radians(s))
        s=str(s)
        text_input.set(s)
    except:
        messagebox.showerror("Error","Envalid")

#-------cos-----------
cosine=Button(root,text='Cos',padx="10",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : coss())
cosine.place(x=100,y=320)
CreateToolTip(cosine,"Enter a value. \n click cos button")
def coss():
    try:
        s=text_input.get()
        if '.' in s:
            s=float(s)
        else:
            s=int(s)
        s=math.cos(math.radians(s))
        s=str(s)
        text_input.set(s)
    except:
        messagebox.showerror("Error","Envalid")


#--------------tan------------
tangent=Button(root,text='tan',padx="10",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : tann())
tangent.place(x=170,y=320)
CreateToolTip(tangent,"Enter a value. \n click tan button")
def tann():
    try:
        s=text_input.get()
        if '.' in s:
            s=float(s)
        else:
            s=int(s)
    
        s=math.tan(math.radians(s))
        s=str(s)
        text_input.set(s)
    except:
        messagebox.showerror("Error","Envalid")

#******----lcm------------
lcmm=Button(root,text='Lcm',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda: lc())
lcmm.place(x=240,y=320)
CreateToolTip(lcmm,"Enter two values:2,3. \n Click lcm button.\nAns:6")
def lc():
    try:
        s=text_input.get()
        a=s.split(',')

        a=[int(i) for i in a]
        a,b=a
        a=abs(a)
        b=abs(b)
        l=a*b//math.gcd(a,b)
        text_input.set(str(l))
    except:
        messagebox.showerror("Error","Envalid")

#---------SEC--------
sec=Button(root,text='Sec',padx="10",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : sc())
sec.place(x=30,y=380)
def sc():
    try:
        s=text_input.get()
        if '.' in s:
            s=float(s)
        else:
            s=int(s)
    
        s=1/(math.cos(math.radians(s)))
        s=str(s)
        text_input.set(s)
    except:
        messagebox.showerror("Error","Envalid")




#----------cosec-------
cosec=Button(root,text='Cosec',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : cosc())
cosec.place(x=100,y=380)
def cosc():
    try:
        s=text_input.get()
        if '.' in s:
            s=float(s)
        else:
            s=int(s)
    
        s=1/(math.sin(math.radians(s)))
        s=str(s)
        text_input.set(s)
    except:
        messagebox.showerror("Error","Envalid")




#-----------cot--------
cot=Button(root,text='Cot',padx="10",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : caught())
cot.place(x=170,y=380)
def caught():
    try:
        s=text_input.get()
        if '.' in s:
            s=float(s)
        else:
            s=int(s)
    
        s=1/(math.tan(math.radians(s)))
        s=str(s)
        text_input.set(s)
    except:
        messagebox.showerror("Error","Envalid")

#gcd between two numbers
gcdd=Button(root,text='Gcd',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : hcf())
gcdd.place(x=240,y=380)
CreateToolTip(gcdd,"Enter two values.: 12,6 \n click gcd button.\nAns:6")
def hcf():
    try:
        s=text_input.get()
        a=s.split(',')

        a=[int(i) for i in a]
        a,b=a
        a=abs(a)
        b=abs(b)
        g=math.gcd(a,b)
        text_input.set(str(g))
    except:
        messagebox.showerror("Error","Envalid")


#----asin-----
arsin=Button(root,text='sin^-1',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : acsin())
arsin.place(x=30,y=440)
CreateToolTip(arsin,"Enter a value. \n click arcsin button")
def acsin():
    try:
        s=text_input.get()
        if '.' in s:
            s=float(s)
        else:
            s=int(s)
        if s>= -1 and s <= 1:
            s=math.degrees(math.asin(s))
            s=str(s)
            text_input.set(s)
        else:
            messagebox.showinfo("Information","Enter value between -1 to 1.")
    except:
        messagebox.showerror("Error","Envalid")



#-----acos------
arcos=Button(root,text='cos^-1',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : accos())
arcos.place(x=100,y=440)
CreateToolTip(arcos,"Enter a value. \n click arcCos button")
def accos():
    try:
        s=text_input.get()
        if '.' in s:
            s=float(s)
        else:
            s=int(s)
        if s>= -1 and s <= 1:
            s=math.acos(s)
            s=math.degrees(s)
            s=str(s)
            text_input.set(s)
        else:
            messagebox.showinfo("Information","Enter value between -1 to 1.")
    except:
        messagebox.showerror("Error","Envalid")




#------atan------
artan=Button(root,text='tan^-1',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : actan())
artan.place(x=170,y=440)
CreateToolTip(artan,"Enter a value.\n click arctan button")   
def actan():
    try:
        s=text_input.get()
        if '.' in s:
            s=float(s)
        else:
            s=int(s)
        if s>=-1 and s<=1:
            s=math.atan(s)
            s=math.degrees(s)
            s=str(s)
            text_input.set(s)
        else:
            messagebox.showinfo("Information","Enter value between -1 to 1.")
    except:
        messagebox.showerror("Error","Envalid")


#----------------radians-------------------
r=Button(root,text='RAD',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : ra())
r.place(x=240,y=440)
CreateToolTip(r,"Find value in radian")
def ra():
    try:
        s=text_input.get()
    
        if '.' in s:
            a=float(s)
        else:
            a=int(s)
        
        
        k=math.radians(a)
        text_input.set(str(k))
    except:
        messagebox.showerror("Error","Envalid")

#---------------------Quadratic Equation-------
qe=Button(root,padx="10",text='ax^2+bx+c=0',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),height=2,command=lambda : equation())
qe.place(x=30,y=500)
CreateToolTip(qe,"ax2 + bx + c = 0, where\na, b and c are real numbers and \na ≠ 0")
def equation():
    try:
        s=text_input.get()
        a,b,c=s.split(',')
        a=int(a)
        b=int(b)
        c=int(c)
        d=(b**2)-(4*a*c)
        root1=(-b+cmath.sqrt(d))/(2*a)
        root2=(-b-cmath.sqrt(d))/(2*a) #class complex

        text_input.set(f"root1={root1} and root2={root2}")
    except:
        messagebox.showerror("Error","Envalid")



#-------------------------measures of length------------------
msl=Button(root,text='Unit of length',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),height=2,command=lambda : measure())
msl.place(x=170,y=500)
CreateToolTip(msl,"Find meter,centimeter,millimeter")
def measure():
    txt=StringVar()
    txtc=StringVar()
    n=Toplevel()
    n.title("Measures of length")
    n.iconbitmap("img.ico")
    n.geometry('380x600')
    n.resizable(False,False)
    m=Label(n,text='M:').place(x=80,y=20)
    e=Entry(n,text=txt).place(x=100,y=20)

    cm=Label(n,text='CM:').place(x=70,y=70)
    ce=Entry(n,text=txtc).place(x=100,y=70)

    btn=Button(n,text="M <=> CM",font=("Arial",12,"bold"),command=lambda : convert())
    btn.place(x=100,y=130)

    def convert():
        
        if txt.get()!='':
            s=txt.get()
            if '.' in s:
                s=float(s)
            else:
                s=int(s)
            s=100*s
            s=str(s)
            txtc.set(s)
        elif txtc.get()!='':
            s=txtc.get()
            if '.' in s:
                s=float(s)
            else:
                s=int(s)
            s=s/100
            s=str(s)
            txt.set(s)

    #-----------------m to mm----------
    txtm=StringVar()
    txtmm=StringVar()


    m1=Label(n,text='M:').place(x=80,y=200)
    e1=Entry(n,text=txtm).place(x=100,y=200)

    mm=Label(n,text='MM:').place(x=70,y=250)
    me=Entry(n,text=txtmm).place(x=100,y=250)

    btn1=Button(n,text="M <=> mm",font=("Arial",12,"bold"),command=lambda : convertm())
    btn1.place(x=100,y=300)

    def convertm():
        if txtm.get()!='':
            s=txtm.get()
            if '.' in s:
                s=float(s)
            else:
                s=int(s)
            s=1000*s
            s=str(s)
            txtmm.set(s)
        elif txtmm.get()!='':
            s=txtmm.get()
            if '.' in s:
                s=float(s)
            else:
                s=int(s)
            s=s/1000
            s=str(s)
            txtm.set(s)

    #-----------------cm to mm----------
    txtcm=StringVar()
    tmm=StringVar()


    cm1=Label(n,text='CM:').place(x=70,y=370)
    cme=Entry(n,text=txtcm).place(x=100,y=370)

    mm1=Label(n,text='MM:').place(x=70,y=410)
    me1=Entry(n,text=tmm).place(x=100,y=410)

    btn2=Button(n,text="CM <=> mm",font=("Arial",12,"bold"),command=lambda : convertcm())
    btn2.place(x=100,y=460)

    def convertcm():
        if txtcm.get()!='':
            s=txtcm.get()
            if '.' in s:
                s=float(s)
            else:
                s=int(s)
            s=10*s
            s=str(s)
            tmm.set(s)
        elif tmm.get()!='':
            s=tmm.get()
            if '.' in s:
                s=float(s)
            else:
                s=int(s)
            s=s/10
            s=str(s)
            txtcm.set(s)

    btn3=Button(n,text="Exit",font=("Arial",12,'bold'),command=n.destroy).place(x=130,y=520)






#-----------------MIDDLE------------------
#*****************bracket (**************
fb=Button(root,text='(',padx="15",bg='#ff9a8d',fg='black',font=("Arial",12,"bold"),command=lambda: num('('))
fb.place(x=310,y=200)





#---------------------------Age---------------------------------------
age=Button(root,text='AGE',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : agecal())
age.place(x=310,y=260)
CreateToolTip(age,"Calculate your age")
def agecal():
    newindow=Toplevel()
    newindow.title("Age calculator")
    newindow.iconbitmap("img.ico")
    newindow.geometry('500x500')
    newindow.resizable(False,False)

    #-------------headline---------------
    bhead=Label(newindow,fg='green',text="Age Calculator",font=("Tahoma",20,'bold')).place(x=150,y=10)

    #---------------birthdate------------
    birthd=StringVar()
    birthm=StringVar()
    birthy=StringVar()
    #-----------------------------------
    bdate=Label(newindow,text='Birth date:',font=('Arial',10)).place(x=14,y=90)
    dcombo=ttk.Combobox(newindow,textvariable=birthd,width=15)
    dcombo.place(x=90,y=90)
    a=[]
    for i in range(1,32):
        a.append(i)
    
    dcombo.config(values=a)

    bm=Label(newindow,text='Birth Month:',font=('Arial',10)).place(x=14,y=120)
    mcombo=ttk.Combobox(newindow,textvariable=birthm,width=15)
    mcombo.place(x=90,y=120)
    a=[]
    for i in range(1,13):
        a.append(i)
    
    mcombo.config(values=a)

    by=Label(newindow,text='Birth Year:',font=('Arial',10)).place(x=14,y=170)
    ycombo=ttk.Combobox(newindow,textvariable=birthy,width=15)
    ycombo.place(x=90,y=170)
    a=[]
    for i in range(1900,(date.today().year)+1):
        a.append(i)
    ycombo.config(values=a)

    btn=Button(newindow,text="Calculate",font=("Arial",10),command=lambda : agecalculator())
    btn.place(x=90,y=220)
    txt=StringVar()
    showl=Label(newindow,textvariable=txt,font=('Tahoma',20),fg='green')
    showl.place(x=80,y=300)

    btn2=Button(newindow,text='Exit',font=('Arial italic',10),command=newindow.destroy)
    btn2.place(x=200,y=220)
    
    def agecalculator():
        dtoday=date.today().day
        mtoday=date.today().month
        ytoday=date.today().year
        day=int(birthd.get())
        month=int(birthm.get())
        year=int(birthy.get())
        dd=mm=yy=0
        if dtoday<day:
            dtoday+=30
            dd=dtoday-day
            month+=1
            if mtoday<month:
                mtoday+=12
                mm=mtoday-month
                year+=1
                yy=ytoday-year
            else:
                mm=mtoday-month
                yy=ytoday-year
        else:
            dd=dtoday-day
            if mtoday<month:
                mtoday+=12
                mm=mtoday-month
                year+=1
                yy=ytoday-year
            else:
                mm=mtoday-month
                yy=ytoday-year
        showl.config(text=txt.set(f"{yy} years,{mm} months,{dd+1} days"))


#------------------PRIME----------------------
prime=Button(root,text='PRIME',bg="#aed6dc",fg="black",font=("Arial",9,"bold"),pady="5",command=lambda: fprime())
prime.place(x=310,y=320)
CreateToolTip(prime,"Check number is prime or not")
def fprime():
    try:
        s=text_input.get()
        s=int(s)
        if s>1:
            for i in range(2,s):
                if(s%i)==0:
                    messagebox.showinfo("Prime",'Not a prime number.')
                    break
            else:
                messagebox.showinfo("Prime",'Prime number.')
        else:
            messagebox.showinfo("Prime",'Not a prime number')
    except:
        messagebox.showerror("Error","Envalid")


#---------------------------leap--------------------------------------
leapy=Button(root,text='Leap',bg="#aed6dc",fg="black",font=("Arial",11,"bold"),command=lambda: leap())
leapy.place(x=310,y=380)
CreateToolTip(leapy,"Find leap year")
def leap():
    try:
        year=text_input.get()
        year=int(year)
        if year%4==0:
            if year%100!=0:
                messagebox.showinfo("Leap Year","Leap year.")
            elif year%100==0:
                if year%400!=0:
                    messagebox.showinfo("Leap Year","Not leap year.")
                else:
                    messagebox.showinfo("Leap Year","Leap year.")
        else:
            messagebox.showinfo("Leap Year","Not leap year.")
    except:
        messagebox.showerror("Error","Envalid")

# Degrees
de=Button(root,text='DEG',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : d())
de.place(x=310,y=440)
CreateToolTip(de,"Find value in degree")
def d():
    try:
        s=text_input.get()
    
        if '.' in s:
            a=float(s)
        else:
            a=int(s)
        
        
        k=math.degrees(a)
        text_input.set(str(k))
    except:
        messagebox.showerror("Error","Envalid")
        


#--------------------------weekday-------------------------------------
weakd=Button(root,text='Weekday',padx="10",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),height=2,command=lambda: week())
weakd.place(x=310,y=500)
CreateToolTip(weakd,"Find weekday from date/month/year")
def week():
    weakwindow=Toplevel()
    weakwindow.title("Weekday find")
    weakwindow.iconbitmap("img.ico")
    weakwindow.geometry("500x500")
    weakwindow.resizable(False,False)
    #----------------------headline

    weakl=Label(weakwindow,text="Weekday find",fg='green',font=('Arial',14))
    weakl.place(x=200,y=20)
    year=StringVar()
    month=StringVar()
    day=StringVar()
    #----------------year label

    yl=Label(weakwindow,text='Year:',font=('Arial',10,'bold'))
    yl.place(x=10,y=90)
    ye=ttk.Combobox(weakwindow,textvariable=year)
    a=[i for i in range((date.today().year),0,-1)]
    ye.configure(values=a)
    ye.place(x=80,y=90)

    #------------------month
    ml=Label(weakwindow,text='Month:',font=('Arial',10,'bold'))
    ml.place(x=10,y=120)
    me=ttk.Combobox(weakwindow,textvariable=month)
    a=[i for i in range(1,13)]
    me.configure(values=a)
    me.place(x=80,y=120)
    # #----------------day
    dl=Label(weakwindow,text='Day:',font=('Arial',10,'bold'))
    dl.place(x=10,y=150)
    de=ttk.Combobox(weakwindow,textvariable=day)
    a=[i for i in range(1,32)]
    de.configure(values=a)
    de.place(x=80,y=150)

    #-----------------find and exit--------------
    find=Button(weakwindow,text='Find',font=("Tahoma",10),command=lambda : weekfind())
    find.place(x=80,y=200)
    ber=Button(weakwindow,text="Exit",font=('Tahoma',10),command=weakwindow.destroy)
    ber.place(x=130,y=200)

    fweak=StringVar()


    findweak=Label(weakwindow,textvariable=fweak,fg='green',font=("Arial",20,'bold'))
    findweak.place(x=150,y=300)

    def weekfind():
        def findday(k):
            day,month,year=k.split(' ')
            day=int(day)
            month=int(month)
            year=int(year)
            days=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATARDAY','SUNDAY']
            dn=calendar.weekday(year,month,day)
            return(days[dn])
        
        y=year.get()
        m=month.get()
        d=day.get()
        k=str(d)+' '+str(m)+' '+str(y)
        
        fweak.set(findday(k))


#*************bracket )****************
lb=Button(root,text=')',padx="15",bg='#ff9a8d',fg='black',font=("Arial",12,"bold"),command=lambda: num(')'))
lb.place(x=370,y=200)


#7
seven=Button(root,text='7',bg="#aed6dc",fg="black",padx="11",font=("Arial",12,"bold"),command=lambda: num(7))
seven.place(x=370,y=260)

#4
four=Button(root,text='4',bg="#aed6dc",fg="black",padx="11",font=("Arial",12,"bold"),command=lambda: num(4))
four.place(x=370,y=320)

#1
one=Button(root,text='1',bg="#aed6dc",fg="black",padx="11",font=("Arial",12,"bold"),command=lambda: num(1))
one.place(x=370,y=380)

#0
zero=Button(root,text='0',bg="#aed6dc",fg="black",padx="11",font=("Arial",12,"bold"),command=lambda: num(0))
zero.place(x=370,y=440)






#-------------------------measures of central tandency----------------
mct=Button(root,text='Statistics',padx="12",bg="#aed6dc",fg="black",font=("Arial",12,"bold"),height=2,command=lambda : measurect())
mct.place(x=430,y=500)
CreateToolTip(mct,"Statistics module of python.\nFind mean,median and mode")
def measurect():
    nibo=StringVar()
    window=Toplevel()
    window.title("Statistics")
    window.iconbitmap("img.ico")
    window.geometry('400x400')
    window.resizable(False,False)
    nibol=Label(window,text='Values:',fg="green",font=('Arial',12)).place(x=20,y=30)
    niboe=Entry(window,text=nibo,font=('Tahoma',14)).place(x=100,y=30)

    btn=Button(window,text='Calculate',font=('Arial',10,'bold'),command=lambda : calculate()).place(x=20,y=80)
    tmean=StringVar()
    tmode=StringVar()
    tmedian=StringVar()
    tmean.set('Mean = 0')
    tmedian.set('Median = 0')
    tmode.set('Mode = 0')
    mean=Label(window,textvariable=tmean,fg="green",font=('Tahoma',10,'bold')).place(x=100,y=140)
    median=Label(window,textvariable=tmedian,fg="green",font=('Tahoma',10,'bold')).place(x=100,y=170)
    mood=Label(window,textvariable=tmode,fg="green",font=('Tahoma',10,'bold')).place(x=100,y=200)

    btn2=Button(window,text="Exit",font=('Arial italic',10),command=window.destroy).place(x=300,y=80)

    def calculate():
        s=nibo.get()
        a=s.split(',')
        if '.' in s:
            a=[float(i) for i in a]
            tmean.set(f"Mean = {statistics.fmean(a)}")
            
        else:
            a=[int(i) for i in a]
            tmean.set(f"Mean = {statistics.mean(a)}")

        tmedian.set(f"Median = {statistics.median(a)}")
        tmode.set(f"Mode = {statistics.multimode(a)}")


#------clear------
dlt=Button(root,text='CLR',bg='#ff9a8d',fg='black',font=("Arial",12,"bold"),command=lambda : faka())
dlt.place(x=430,y=200)
def faka():
    global operator
    operator=''
    text_input.set(operator)

#8
eight=Button(root,text='8',bg="#aed6dc",fg="black",padx="12",font=("Arial",12,"bold"),command=lambda: num(8))
eight.place(x=430,y=260)

#5
five=Button(root,text='5',bg="#aed6dc",fg="black",padx="12",font=("Arial",12,"bold"),command=lambda: num(5))
five.place(x=430,y=320)

#2
two=Button(root,text='2',bg="#aed6dc",fg="black",padx="12",font=("Arial",12,"bold"),command=lambda: num(2))
two.place(x=430,y=380)

#.
dot=Button(root,text='.',bg="#aed6dc",fg="black",padx="14",font=("Arial",12,"bold"),command=lambda: num('.'))
dot.place(x=430,y=440)

#--------Exit---------
ac=Button(root,text='EXIT',bg='#ff9a8d',fg='black',font=("Arial",12,"bold"),command=lambda : acexit())
ac.place(x=490,y=200)
CreateToolTip(ac,"Off app")
def acexit():
    root.quit()

#9
nine=Button(root,text='9',bg="#aed6dc",fg="black",padx="13",font=("Arial",12,"bold"),command=lambda: num(9))
nine.place(x=490,y=260)

#6
six=Button(root,text='6',bg="#aed6dc",fg="black",padx="13",font=("Arial",12,"bold"),command=lambda: num(6))
six.place(x=490,y=320)

#3
three=Button(root,text='3',bg="#aed6dc",fg="black",padx="13",font=("Arial",12,"bold"),command=lambda: num(3))
three.place(x=490,y=380)

#10^x
ten=Button(root,text='10^x',bg="#aed6dc",fg="black",font=("Arial",12,"bold"),command=lambda : num('e'))
ten.place(x=490,y=440)
CreateToolTip(ten,"Use for 10 to the power x.\n1e-3=1*10^-3")




#---------------------------------------------RIGHT SIDE-------------------------
#---------percentage---------

percentage=Button(root,text='%',bg="#edc988",fg="black",font=("Arial",12,"bold"),padx="7",command=lambda: percent())
percentage.place(x=560,y=200)
CreateToolTip(percentage,"Find percentage.")

def percent():
    s=text_input.get()
    try:
        if '.' in s:
            s=float(s)
            s=s/100
            text_input.set(str(s))
        else:
            s=int(s)
            s=s/100
            text_input.set(str(s))
    except:
        messagebox.showerror('Error','Error')


#-------/------
vag=Button(root,text='/',bg="#edc988",fg="black",padx="12",font=("Arial",12,"bold"),command=lambda: num('/'))
vag.place(x=560,y=260)

#-----------------x/----------
gun=Button(root,text='x',bg="#edc988",fg="black",padx="10",font=("Arial",12,"bold"),command=lambda: num('*'))
gun.place(x=560,y=320)

#-----------(+-)-----------
minus=Button(root,text='-',bg="#edc988",fg="black",padx="12",font=("Arial",12,"bold"),command=lambda: num('-'))
minus.place(x=560,y=380)

plus=Button(root,text='+',bg="#edc988",fg="black",padx="10",font=("Arial",12,"bold"),command=lambda: num('+'))
plus.place(x=560,y=440)


#------------equal-------------
equal=Button(root,text='=',bg="#edc988",fg="black",padx="11",font=("Arial",12,"bold"),height=2,command=lambda : calculation())
equal.place(x=560,y=500)

#------------------------------calculation-----------------------------------
operator=''
def num(numbers):
    global operator
    operator=text_input.get()
    operator+=str(numbers)
    text_input.set(operator)

def calculation(): 
    s=text_input.get()
    try:
        if 'e' in s:
            text_input.set(eval(s))
        elif '^'in s:
            calpow(s)
        else:
            text_input.set(eval(s))
            global operator
            operator=text_input.get()
    except:
        messagebox.showerror('Error','Empty')
    

#---------------main loop-----------------

root.mainloop()