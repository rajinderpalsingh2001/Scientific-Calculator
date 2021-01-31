#waheguru
from math import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

import threading
from time import sleep

class calc:
    def factorial(self):
        try:
            e=int(eval(self.txtfield.get()))
            if(e==0):
                self.resultset.set("0")
            else:
                fact=1
                for i in range(1,e+1):
                    fact=fact*i
                self.resultset.set(str(fact))
        except:
            self.resultset.set("INVALID EXPRESSION")

    def factors(self):
        try:
            e=int(eval(self.txtfield.get()))
            x=[]
            for i in range(2,e+1):
                j=True
                while j==True:
                    if(e%i)==0:
                        x.append(i)
                        e=e/i
                    else:
                        j=False
            self.resultset.set(x)
        except:
            self.resultset.set("INVALID EXPRESSION")

    def trigno(self,num,pos):
        if(self.ans2.get()==1):
            self.btnsin["text"]="asin()"
            self.btncos["text"]="acos()"
            self.btntan["text"]="atan()"
            self.btncosec["text"]="acosec()"
            self.btnsec["text"]="asec()"
            self.btncot["text"]="acot()"
            if(self.ans.get()==1):
                self.sinvalue="degrees(asin("
                self.cosvalue="degrees(acos("
                self.tanvalue="degrees(atan("
                self.cosecavlue="1/degrees(asin("
                self.secavlue="1/degrees(acos("
                self.cotvalue="1/degrees(atan("
            else:
                self.sinvalue = "radians(asin("
                self.cosvalue = "radians(acos("
                self.tanvalue = "radians(atan("
                self.cosecavlue = "1/radians(asin("
                self.secavlue = "1/radians(acos("
                self.cotvalue = "1/radians(atan("
        else:
            self.btnsin["text"] = "sin()"
            self.btncos["text"] = "cos()"
            self.btntan["text"] = "tan()"
            self.btncosec["text"] ="cosec()"
            self.btnsec["text"] = "sec()"
            self.btncot["text"] = "cot()"
            if (self.ans.get() == 1):
                self.sinvalue = 'sin('
                self.cosvalue = 'cos('
                self.tanvalue = 'tan('
                self.cosecavlue = '1/sin('
                self.secavlue = '1/cos('
                self.cotvalue = '1/tan('
            else:
                self.sinvalue = 'sin(radians('
                self.cosvalue = 'cos(radians('
                self.tanvalue = 'tan(radians('
                self.cosecavlue = '1/sin(radians('
                self.secavlue = '1/cos(radians('
                self.cotvalue = '1/tan(radians('
        self.txtfield.insert(pos,num)

    def log(self):
        self.press("log10(",'end')

    def ansbtn(self):
        self.txtfield.delete(0,'end')
        self.txtfield.insert('end',self.resultset.get())
        self.resultset.set("")

    def enable(self):
        pass


    def advexpo(self):
        try:
            x = []
            for i in self.txtfield.get():
                x.append(i)
            if (self.txtfield.get() == ""):
                num = "exp("
                self.press(num, 'end')
            elif ((x[len(x)-1]=="+") or (x[len(x)-1]=="-") or (x[len(x)-1]=="*") or (x[len(x)-1]=="/")):
                num="exp("
                self.press(num,'end')
            else:
                num='*exp('
                self.press(num,'end')
        except:
            pass

    def percentage(self):
        self.click=True
        n=eval(self.txtfield.get())
        return n/100


    def backclear(self):
        self.txtfield.delete(len(self.txtfield.get())-1)
        self.expression=""

    def clear(self):
        self.txtfield.delete(0,"end")
        self.expression=""

    def chkrightbracket(self):
        if ((self.txtfield.get().find("log10(") ==0) and self.txtfield.get()[len(self.txtfield.get()) - 1] != ")"):
            try:
                self.press(")", 'end')
            except:
                pass

        if ((self.txtfield.get().find("exp(") ==0) and self.txtfield.get()[len(self.txtfield.get()) - 1] != ")"):
            try:
                self.press(")", 'end')
            except:
                pass

        try:
            if ((self.txtfield.get().find("sin(radians(") == 0 or self.txtfield.get().find("sin(radians(") == 1 or self.txtfield.get().find("sin(radians(") == 2 or self.txtfield.get().find("sin(radians(") == 3 or self.txtfield.get().find("sin(radians(") == 4 or self.txtfield.get().find("sin(radians(") == 5 or self.txtfield.get().find("sin(radians(") == 6 or self.txtfield.get().find("sin(radians(") == 7 or self.txtfield.get().find("sin(radians(") == 8 or self.txtfield.get().find("sin(radians(") == 9 or self.txtfield.get().find("sin(radians(") == 10 or self.txtfield.get().find("sin(radians(") == 11 or self.txtfield.get().find("sin(radians(") == 12 or self.txtfield.get().find("sin(radians(") == 13 or self.txtfield.get().find("sin(radians(") == 14 or self.txtfield.get().find("sin(radians(") == 15
            or self.txtfield.get().find("cos(radians(") == 0 or self.txtfield.get().find("cos(radians(") == 1 or self.txtfield.get().find("cos(radians(") == 2 or self.txtfield.get().find("cos(radians(") == 3 or self.txtfield.get().find("cos(radians(") == 4 or self.txtfield.get().find("cos(radians(") == 5 or self.txtfield.get().find("cos(radians(") == 6 or self.txtfield.get().find("cos(radians(") == 7 or self.txtfield.get().find("cos(radians(") == 8 or self.txtfield.get().find("cos(radians(") == 9 or self.txtfield.get().find("cos(radians(") == 10 or self.txtfield.get().find("cos(radians(") == 11 or self.txtfield.get().find("cos(radians(") == 12 or self.txtfield.get().find("cos(radians(") == 13 or self.txtfield.get().find("cos(radians(") == 14 or self.txtfield.get().find("cos(radians(") == 15
            or self.txtfield.get().find("tan(radians(") == 0 or self.txtfield.get().find("tan(radians(") == 1 or self.txtfield.get().find("tan(radians(") == 2 or self.txtfield.get().find("tan(radians(") == 3 or self.txtfield.get().find("tan(radians(") == 4 or self.txtfield.get().find("tan(radians(") == 5 or self.txtfield.get().find("tan(radians(") == 6 or self.txtfield.get().find("tan(radians(") == 7 or self.txtfield.get().find("tan(radians(") == 8 or self.txtfield.get().find("tan(radians(") ==  9 or self.txtfield.get().find("tan(radians(") == 10 or self.txtfield.get().find("tan(radians(") == 11 or self.txtfield.get().find("tan(radians(") == 12 or self.txtfield.get().find("tan(radians(") == 13 or self.txtfield.get().find("tan(radians(") == 14 or self.txtfield.get().find("tan(radians(") == 15
            or self.txtfield.get().find("1/sin(radians(") == 0 or self.txtfield.get().find("1/sin(radians(") ==1 or self.txtfield.get().find("1/sin(radians(") ==2 or self.txtfield.get().find("1/sin(radians(") ==3 or self.txtfield.get().find("1/sin(radians(") ==4 or self.txtfield.get().find("1/sin(radians(") ==5 or self.txtfield.get().find("1/sin(radians(") ==6 or self.txtfield.get().find("1/sin(radians(") ==7 or self.txtfield.get().find("1/sin(radians(") ==8 or self.txtfield.get().find("1/sin(radians(") ==9 or self.txtfield.get().find("1/sin(radians(") ==10 or self.txtfield.get().find("1/sin(radians(") ==11 or self.txtfield.get().find("1/sin(radians(") ==12 or self.txtfield.get().find("1/sin(radians(") ==13 or self.txtfield.get().find("1/sin(radians(") ==14 or self.txtfield.get().find("1/sin(radians(") ==15
            or self.txtfield.get().find("1/cos(radians(")==0 or self.txtfield.get().find("1/cos(radians(")==1 or self.txtfield.get().find("1/cos(radians(")==2 or self.txtfield.get().find("1/cos(radians(")==3 or self.txtfield.get().find("1/cos(radians(")==4 or self.txtfield.get().find("1/cos(radians(")==5 or self.txtfield.get().find("1/cos(radians(")==6 or self.txtfield.get().find("1/cos(radians(")==7 or self.txtfield.get().find("1/cos(radians(")== 8 or self.txtfield.get().find("1/cos(radians(")==9 or self.txtfield.get().find("1/cos(radians(")==10 or self.txtfield.get().find("1/cos(radians(")==11 or self.txtfield.get().find("1/cos(radians(")==12 or self.txtfield.get().find("1/cos(radians(")==13 or self.txtfield.get().find("1/cos(radians(")==14 or self.txtfield.get().find("1/cos(radians(")==15
            or self.txtfield.get().find("1/tan(radians(") == 0 or self.txtfield.get().find("1/tan(radians(") ==1 or self.txtfield.get().find("1/tan(radians(") ==2 or self.txtfield.get().find("1/tan(radians(") ==3 or self.txtfield.get().find("1/tan(radians(") ==4 or self.txtfield.get().find("1/tan(radians(") ==5 or self.txtfield.get().find("1/tan(radians(") ==6 or self.txtfield.get().find("1/tan(radians(") ==7 or self.txtfield.get().find("1/tan(radians(") ==8 or self.txtfield.get().find("1/tan(radians(") ==9 or self.txtfield.get().find("1/tan(radians(") ==10 or self.txtfield.get().find("1/tan(radians(") ==11 or self.txtfield.get().find("1/tan(radians(") ==12 or self.txtfield.get().find("1/tan(radians(") ==13 or self.txtfield.get().find("1/tan(radians(") ==14 or self.txtfield.get().find("1/tan(radians(") ==15
                 or self.txtfield.get().find("radians(asin(") == 0 or self.txtfield.get().find(
                        "radians(asin(") == 1 or self.txtfield.get().find(
                        "radians(asin(") == 2 or self.txtfield.get().find(
                        "radians(asin(") == 3 or self.txtfield.get().find(
                        "radians(asin(") == 4 or self.txtfield.get().find(
                        "radians(asin(") == 5 or self.txtfield.get().find(
                        "radians(asin(") == 6 or self.txtfield.get().find(
                        "radians(asin(") == 7 or self.txtfield.get().find(
                        "radians(asin(") == 8 or self.txtfield.get().find(
                        "radians(asin(") == 9 or self.txtfield.get().find(
                        "radians(asin(") == 10 or self.txtfield.get().find(
                        "radians(asin(") == 11 or self.txtfield.get().find(
                        "radians(asin(") == 12 or self.txtfield.get().find(
                        "radians(asin(") == 13 or self.txtfield.get().find(
                        "radians(asin(") == 14 or self.txtfield.get().find("radians(asin(") == 15
                 or self.txtfield.get().find("radians(acos(") == 0 or self.txtfield.get().find(
                        "radians(acos(") == 1 or self.txtfield.get().find(
                        "radians(acos(") == 2 or self.txtfield.get().find(
                        "radians(acos(") == 3 or self.txtfield.get().find(
                        "radians(acos(") == 4 or self.txtfield.get().find(
                        "radians(acos(") == 5 or self.txtfield.get().find(
                        "radians(acos(") == 6 or self.txtfield.get().find(
                        "radians(acos(") == 7 or self.txtfield.get().find(
                        "radians(acos(") == 8 or self.txtfield.get().find(
                        "radians(acos(") == 9 or self.txtfield.get().find(
                        "radians(acos(") == 10 or self.txtfield.get().find(
                        "radians(acos(") == 11 or self.txtfield.get().find(
                        "radians(acos(") == 12 or self.txtfield.get().find(
                        "radians(acos(") == 13 or self.txtfield.get().find(
                        "radians(acos(") == 14 or self.txtfield.get().find("radians(acos(") == 15
                 or self.txtfield.get().find("radians(atan(") == 0 or self.txtfield.get().find(
                        "radians(atan(") == 1 or self.txtfield.get().find(
                        "radians(atan(") == 2 or self.txtfield.get().find(
                        "radians(atan(") == 3 or self.txtfield.get().find(
                        "radians(atan(") == 4 or self.txtfield.get().find(
                        "radians(atan(") == 5 or self.txtfield.get().find(
                        "radians(atan(") == 6 or self.txtfield.get().find(
                        "radians(atan(") == 7 or self.txtfield.get().find(
                        "radians(atan(") == 8 or self.txtfield.get().find(
                        "radians(atan(") == 9 or self.txtfield.get().find(
                        "radians(atan(") == 10 or self.txtfield.get().find(
                        "radians(atan(") == 11 or self.txtfield.get().find(
                        "radians(atan(") == 12 or self.txtfield.get().find(
                        "radians(atan(") == 13 or self.txtfield.get().find(
                        "radians(atan(") == 14 or self.txtfield.get().find("radians(atan(") == 15
                 or self.txtfield.get().find("1/radians(asin(") == 0 or self.txtfield.get().find(
                        "1/radians(asin(") == 1 or self.txtfield.get().find(
                        "1/radians(asin(") == 2 or self.txtfield.get().find(
                        "1/radians(asin(") == 3 or self.txtfield.get().find(
                        "1/radians(asin(") == 4 or self.txtfield.get().find(
                        "1/radians(asin(") == 5 or self.txtfield.get().find(
                        "1/radians(asin(") == 6 or self.txtfield.get().find(
                        "1/radians(asin(") == 7 or self.txtfield.get().find(
                        "1/radians(asin(") == 8 or self.txtfield.get().find(
                        "1/radians(asin(") == 9 or self.txtfield.get().find(
                        "1/radians(asin(") == 10 or self.txtfield.get().find(
                        "1/radians(asin(") == 11 or self.txtfield.get().find(
                        "1/radians(asin(") == 12 or self.txtfield.get().find(
                        "1/radians(asin(") == 13 or self.txtfield.get().find(
                        "1/radians(asin(") == 14 or self.txtfield.get().find("1/radians(asin(") == 15
                 or self.txtfield.get().find("1/radians(acos(") == 0 or self.txtfield.get().find(
                        "1/radians(acos(") == 1 or self.txtfield.get().find(
                        "1/radians(acos(") == 2 or self.txtfield.get().find(
                        "1/radians(acos(") == 3 or self.txtfield.get().find(
                        "1/radians(acos(") == 4 or self.txtfield.get().find(
                        "1/radians(acos(") == 5 or self.txtfield.get().find(
                        "1/radians(acos(") == 6 or self.txtfield.get().find(
                        "1/radians(acos(") == 7 or self.txtfield.get().find(
                        "1/radians(acos(") == 8 or self.txtfield.get().find(
                        "1/radians(acos(") == 9 or self.txtfield.get().find(
                        "1/radians(acos(") == 10 or self.txtfield.get().find(
                        "1/radians(acos(") == 11 or self.txtfield.get().find(
                        "1/radians(acos(") == 12 or self.txtfield.get().find(
                        "1/radians(acos(") == 13 or self.txtfield.get().find(
                        "1/radians(acos(") == 14 or self.txtfield.get().find("1/radians(acos(") == 15
                 or self.txtfield.get().find("1/radians(atan(") == 0 or self.txtfield.get().find(
                        "1/radians(atan(") == 1 or self.txtfield.get().find(
                        "1/radians(atan(") == 2 or self.txtfield.get().find(
                        "1/radians(atan(") == 3 or self.txtfield.get().find(
                        "1/radians(atan(") == 4 or self.txtfield.get().find(
                        "1/radians(atan(") == 5 or self.txtfield.get().find(
                        "1/radians(atan(") == 6 or self.txtfield.get().find(
                        "1/radians(atan(") == 7 or self.txtfield.get().find(
                        "1/radians(atan(") == 8 or self.txtfield.get().find(
                        "1/radians(atan(") == 9 or self.txtfield.get().find(
                        "1/radians(atan(") == 10 or self.txtfield.get().find(
                        "1/radians(atan(") == 11 or self.txtfield.get().find(
                        "1/radians(atan(") == 12 or self.txtfield.get().find(
                        "1/radians(atan(") == 13 or self.txtfield.get().find(
                        "1/radians(atan(") == 14 or self.txtfield.get().find("1/radians(atan(") == 15
                 or self.txtfield.get().find("degrees(asin(") == 0 or self.txtfield.get().find(
                        "degrees(asin(") == 1 or self.txtfield.get().find(
                        "degrees(asin(") == 2 or self.txtfield.get().find(
                        "degrees(asin(") == 3 or self.txtfield.get().find(
                        "degrees(asin(") == 4 or self.txtfield.get().find(
                        "degrees(asin(") == 5 or self.txtfield.get().find(
                        "degrees(asin(") == 6 or self.txtfield.get().find(
                        "degrees(asin(") == 7 or self.txtfield.get().find(
                        "degrees(asin(") == 8 or self.txtfield.get().find(
                        "degrees(asin(") == 9 or self.txtfield.get().find(
                        "degrees(asin(") == 10 or self.txtfield.get().find(
                        "degrees(asin(") == 11 or self.txtfield.get().find(
                        "degrees(asin(") == 12 or self.txtfield.get().find(
                        "degrees(asin(") == 13 or self.txtfield.get().find(
                        "degrees(asin(") == 14 or self.txtfield.get().find("degrees(asin(") == 15
                 or self.txtfield.get().find("degrees(acos(") == 0 or self.txtfield.get().find(
                        "degrees(acos(") == 1 or self.txtfield.get().find(
                        "degrees(acos(") == 2 or self.txtfield.get().find(
                        "degrees(acos(") == 3 or self.txtfield.get().find(
                        "degrees(acos(") == 4 or self.txtfield.get().find(
                        "degrees(acos(") == 5 or self.txtfield.get().find(
                        "degrees(acos(") == 6 or self.txtfield.get().find(
                        "degrees(acos(") == 7 or self.txtfield.get().find(
                        "degrees(acos(") == 8 or self.txtfield.get().find(
                        "degrees(acos(") == 9 or self.txtfield.get().find(
                        "degrees(acos(") == 10 or self.txtfield.get().find(
                        "degrees(acos(") == 11 or self.txtfield.get().find(
                        "degrees(acos(") == 12 or self.txtfield.get().find(
                        "degrees(acos(") == 13 or self.txtfield.get().find(
                        "degrees(acos(") == 14 or self.txtfield.get().find("degrees(acos(") == 15
                 or self.txtfield.get().find("degrees(atan(") == 0 or self.txtfield.get().find(
                        "degrees(atan(") == 1 or self.txtfield.get().find(
                        "degrees(atan(") == 2 or self.txtfield.get().find(
                        "degrees(atan(") == 3 or self.txtfield.get().find(
                        "degrees(atan(") == 4 or self.txtfield.get().find(
                        "degrees(atan(") == 5 or self.txtfield.get().find(
                        "degrees(atan(") == 6 or self.txtfield.get().find(
                        "degrees(atan(") == 7 or self.txtfield.get().find(
                        "degrees(atan(") == 8 or self.txtfield.get().find(
                        "degrees(atan(") == 9 or self.txtfield.get().find(
                        "degrees(atan(") == 10 or self.txtfield.get().find(
                        "degrees(atan(") == 11 or self.txtfield.get().find(
                        "degrees(atan(") == 12 or self.txtfield.get().find(
                        "degrees(atan(") == 13 or self.txtfield.get().find(
                        "degrees(atan(") == 14 or self.txtfield.get().find("degrees(atan(") == 15
                 or self.txtfield.get().find("1/degrees(asin(") == 0 or self.txtfield.get().find(
                        "1/degrees(asin(") == 1 or self.txtfield.get().find(
                        "1/degrees(asin(") == 2 or self.txtfield.get().find(
                        "1/degrees(asin(") == 3 or self.txtfield.get().find(
                        "1/degrees(asin(") == 4 or self.txtfield.get().find(
                        "1/degrees(asin(") == 5 or self.txtfield.get().find(
                        "1/degrees(asin(") == 6 or self.txtfield.get().find(
                        "1/degrees(asin(") == 7 or self.txtfield.get().find(
                        "1/degrees(asin(") == 8 or self.txtfield.get().find(
                        "1/degrees(asin(") == 9 or self.txtfield.get().find(
                        "1/degrees(asin(") == 10 or self.txtfield.get().find(
                        "1/degrees(asin(") == 11 or self.txtfield.get().find(
                        "1/degrees(asin(") == 12 or self.txtfield.get().find(
                        "1/degrees(asin(") == 13 or self.txtfield.get().find(
                        "1/degrees(asin(") == 14 or self.txtfield.get().find("1/degrees(asin(") == 15
                 or self.txtfield.get().find("1/degrees(acos(") == 0 or self.txtfield.get().find(
                        "1/degrees(acos(") == 1 or self.txtfield.get().find(
                        "1/degrees(acos(") == 2 or self.txtfield.get().find(
                        "1/degrees(acos(") == 3 or self.txtfield.get().find(
                        "1/degrees(acos(") == 4 or self.txtfield.get().find(
                        "1/degrees(acos(") == 5 or self.txtfield.get().find(
                        "1/degrees(acos(") == 6 or self.txtfield.get().find(
                        "1/degrees(acos(") == 7 or self.txtfield.get().find(
                        "1/degrees(acos(") == 8 or self.txtfield.get().find(
                        "1/degrees(acos(") == 9 or self.txtfield.get().find(
                        "1/degrees(acos(") == 10 or self.txtfield.get().find(
                        "1/degrees(acos(") == 11 or self.txtfield.get().find(
                        "1/degrees(acos(") == 12 or self.txtfield.get().find(
                        "1/degrees(acos(") == 13 or self.txtfield.get().find(
                        "1/degrees(acos(") == 14 or self.txtfield.get().find("1/degrees(acos(") == 15
                 or self.txtfield.get().find("1/degrees(atan(") == 0 or self.txtfield.get().find(
                        "1/degrees(atan(") == 1 or self.txtfield.get().find(
                        "1/degrees(atan(") == 2 or self.txtfield.get().find(
                        "1/degrees(atan(") == 3 or self.txtfield.get().find(
                        "1/degrees(atan(") == 4 or self.txtfield.get().find(
                        "1/degrees(atan(") == 5 or self.txtfield.get().find(
                        "1/degrees(atan(") == 6 or self.txtfield.get().find(
                        "1/degrees(atan(") == 7 or self.txtfield.get().find(
                        "1/degrees(atan(") == 8 or self.txtfield.get().find(
                        "1/degrees(atan(") == 9 or self.txtfield.get().find(
                        "1/degrees(atan(") == 10 or self.txtfield.get().find(
                        "1/degrees(atan(") == 11 or self.txtfield.get().find(
                        "1/degrees(atan(") == 12 or self.txtfield.get().find(
                        "1/degrees(atan(") == 13 or self.txtfield.get().find(
                        "1/degrees(atan(") == 14 or self.txtfield.get().find("1/degrees(atan(") == 15
            )and self.txtfield.get()[len(self.txtfield.get()) - 1] != ")"):
                self.press("))",self.posi)
            elif ((self.txtfield.get().find("sin(") == 0 or self.txtfield.get().find("sin(") == 1 or self.txtfield.get().find("sin(") == 2 or self.txtfield.get().find("sin(") == 3 or self.txtfield.get().find("sin(") == 4 or self.txtfield.get().find("sin(") == 5 or self.txtfield.get().find("sin(") == 6 or self.txtfield.get().find("sin(") == 7 or self.txtfield.get().find("sin(") == 8 or self.txtfield.get().find("sin(") == 9 or self.txtfield.get().find("sin(") == 10 or self.txtfield.get().find("sin(") == 11 or self.txtfield.get().find("sin(") == 12 or self.txtfield.get().find("sin(") == 13 or self.txtfield.get().find("sin(") == 14 or self.txtfield.get().find("sin(") == 15
            or self.txtfield.get().find("cos") == 0 or self.txtfield.get().find("cos(") == 1 or self.txtfield.get().find("cos(") == 2 or self.txtfield.get().find("cos(") == 3 or self.txtfield.get().find("cos(") == 4 or self.txtfield.get().find("cos(") == 5 or self.txtfield.get().find("cos(") == 6 or self.txtfield.get().find("cos(") == 7 or self.txtfield.get().find("cos(") == 8 or self.txtfield.get().find("cos(") == 9 or self.txtfield.get().find("cos(") == 10 or self.txtfield.get().find("cos(") == 11 or self.txtfield.get().find("cos(") == 12 or self.txtfield.get().find("cos(") == 13 or self.txtfield.get().find("cos(") == 14 or self.txtfield.get().find("cos(") == 15
            or self.txtfield.get().find("tan") == 0 or self.txtfield.get().find("tan(") == 1 or self.txtfield.get().find("tan(") == 2 or self.txtfield.get().find("tan(") == 3 or self.txtfield.get().find("tan(") == 4 or self.txtfield.get().find("tan(") == 5 or self.txtfield.get().find("tan(") == 6 or self.txtfield.get().find("tan(") == 7 or self.txtfield.get().find("tan(") == 8 or self.txtfield.get().find("tan(") ==  9 or self.txtfield.get().find("tan(") == 10 or self.txtfield.get().find("tan(") == 11 or self.txtfield.get().find("tan(") == 12 or self.txtfield.get().find("tan(") == 13 or self.txtfield.get().find("tan(") == 14 or self.txtfield.get().find("tan(") == 15
            or self.txtfield.get().find("1/sin(") == 0 or self.txtfield.get().find("1/sin(") ==1 or self.txtfield.get().find("1/sin(") ==2 or self.txtfield.get().find("1/sin(") ==3 or self.txtfield.get().find("1/sin(") ==4 or self.txtfield.get().find("1/sin(") ==5 or self.txtfield.get().find("1/sin(") ==6 or self.txtfield.get().find("1/sin(") ==7 or self.txtfield.get().find("1/sin(") ==8 or self.txtfield.get().find("1/sin(") ==9 or self.txtfield.get().find("1/sin(") ==10 or self.txtfield.get().find("1/sin(") ==11 or self.txtfield.get().find("1/sin(") ==12 or self.txtfield.get().find("1/sin(") ==13 or self.txtfield.get().find("1/sin(") ==14 or self.txtfield.get().find("1/sin(") ==15
            or self.txtfield.get().find("1/cos(")==0 or self.txtfield.get().find("1/cos(")==1 or self.txtfield.get().find("1/cos(")==2 or self.txtfield.get().find("1/cos(")==3 or self.txtfield.get().find("1/cos(")==4 or self.txtfield.get().find("1/cos(")==5 or self.txtfield.get().find("1/cos(")==6 or self.txtfield.get().find("1/cos(")==7 or self.txtfield.get().find("1/cos(")== 8 or self.txtfield.get().find("1/cos(")==9 or self.txtfield.get().find("1/cos(")==10 or self.txtfield.get().find("1/cos(")==11 or self.txtfield.get().find("1/cos(")==12 or self.txtfield.get().find("1/cos(")==13 or self.txtfield.get().find("1/cos(")==14 or self.txtfield.get().find("1/cos(")==15
            or self.txtfield.get().find("1/tan(") == 0 or self.txtfield.get().find("1/tan(") ==1 or self.txtfield.get().find("1/tan(") ==2 or self.txtfield.get().find("1/tan(") ==3 or self.txtfield.get().find("1/tan(") ==4 or self.txtfield.get().find("1/tan(") ==5 or self.txtfield.get().find("1/tan(") ==6 or self.txtfield.get().find("1/tan(") ==7 or self.txtfield.get().find("1/tan(") ==8 or self.txtfield.get().find("1/tan(") ==9 or self.txtfield.get().find("1/tan(") ==10 or self.txtfield.get().find("1/tan(") ==11 or self.txtfield.get().find("1/tan(") ==12 or self.txtfield.get().find("1/tan(") ==13 or self.txtfield.get().find("1/tan(") ==14 or self.txtfield.get().find("1/tan(") ==15)and self.txtfield.get()[len(self.txtfield.get()) - 1] != ")"):
                self.press(")",self.posi)
            elif(self.txtfield.get()[len(self.txtfield.get())-1]!=")"):
                self.press(")*", self.posi)
        except:
            self.press(")",'end')
    def evaluate(self):
#--------log()---------------------
        if ((self.txtfield.get().find("log10(") == 0 or self.txtfield.get().find("log10(") == 1 or self.txtfield.get().find("log10(") == 2 or self.txtfield.get().find("log10(") == 3 or self.txtfield.get().find("log10(") == 4 or self.txtfield.get().find("log10(") == 5 or self.txtfield.get().find("log10(") == 6 or self.txtfield.get().find("log10(") == 7 or self.txtfield.get().find("log10(") == 8 or self.txtfield.get().find("log10(") == 9 or self.txtfield.get().find("log10(") == 10 or self.txtfield.get().find("log10(") == 11 or self.txtfield.get().find("log10(") == 12 or self.txtfield.get().find("log10(") == 13 or self.txtfield.get().find("log10(") == 14 or self.txtfield.get().find("log10(") == 15) and self.txtfield.get()[len(self.txtfield.get()) - 1] != ")"):
            try:
                self.press(")", 'end')
            except:
                pass
#--------------expo()---------------
        if ((self.txtfield.get().find("exp(") == 0 or self.txtfield.get().find("exp(") == 1 or self.txtfield.get().find("exp(") == 2 or self.txtfield.get().find("exp(") == 3 or self.txtfield.get().find("exp(") == 4 or self.txtfield.get().find("exp(") == 5 or self.txtfield.get().find("exp(") == 6 or self.txtfield.get().find("exp(") == 7 or self.txtfield.get().find("exp(") == 8 or self.txtfield.get().find("exp(") == 9 or self.txtfield.get().find("exp(") == 10 or self.txtfield.get().find("exp(") == 11 or self.txtfield.get().find("exp(") == 12 or self.txtfield.get().find("exp(") == 13 or self.txtfield.get().find("exp(") == 14 or self.txtfield.get().find("exp(") == 15) and self.txtfield.get()[len(self.txtfield.get()) - 1] != ")"):
            try:
                self.press(")", 'end')
            except:
                pass
#----------------trigno()------------------
        if ((self.txtfield.get().find("sin(radians(") == 0 or self.txtfield.get().find("sin(radians(") == 1 or self.txtfield.get().find("sin(radians(") == 2 or self.txtfield.get().find("sin(radians(") == 3 or self.txtfield.get().find("sin(radians(") == 4 or self.txtfield.get().find("sin(radians(") == 5 or self.txtfield.get().find("sin(radians(") == 6 or self.txtfield.get().find("sin(radians(") == 7 or self.txtfield.get().find("sin(radians(") == 8 or self.txtfield.get().find("sin(radians(") == 9 or self.txtfield.get().find("sin(radians(") == 10 or self.txtfield.get().find("sin(radians(") == 11 or self.txtfield.get().find("sin(radians(") == 12 or self.txtfield.get().find("sin(radians(") == 13 or self.txtfield.get().find("sin(radians(") == 14 or self.txtfield.get().find("sin(radians(") == 15
            or self.txtfield.get().find("cos(radians(") == 0 or self.txtfield.get().find("cos(radians(") == 1 or self.txtfield.get().find("cos(radians(") == 2 or self.txtfield.get().find("cos(radians(") == 3 or self.txtfield.get().find("cos(radians(") == 4 or self.txtfield.get().find("cos(radians(") == 5 or self.txtfield.get().find("cos(radians(") == 6 or self.txtfield.get().find("cos(radians(") == 7 or self.txtfield.get().find("cos(radians(") == 8 or self.txtfield.get().find("cos(radians(") == 9 or self.txtfield.get().find("cos(radians(") == 10 or self.txtfield.get().find("cos(radians(") == 11 or self.txtfield.get().find("cos(radians(") == 12 or self.txtfield.get().find("cos(radians(") == 13 or self.txtfield.get().find("cos(radians(") == 14 or self.txtfield.get().find("cos(radians(") == 15
            or self.txtfield.get().find("tan(radians(") == 0 or self.txtfield.get().find("tan(radians(") == 1 or self.txtfield.get().find("tan(radians(") == 2 or self.txtfield.get().find("tan(radians(") == 3 or self.txtfield.get().find("tan(radians(") == 4 or self.txtfield.get().find("tan(radians(") == 5 or self.txtfield.get().find("tan(radians(") == 6 or self.txtfield.get().find("tan(radians(") == 7 or self.txtfield.get().find("tan(radians(") == 8 or self.txtfield.get().find("tan(radians(") ==  9 or self.txtfield.get().find("tan(radians(") == 10 or self.txtfield.get().find("tan(radians(") == 11 or self.txtfield.get().find("tan(radians(") == 12 or self.txtfield.get().find("tan(radians(") == 13 or self.txtfield.get().find("tan(radians(") == 14 or self.txtfield.get().find("tan(radians(") == 15
            or self.txtfield.get().find("1/sin(radians(") == 0 or self.txtfield.get().find("1/sin(radians(") ==1 or self.txtfield.get().find("1/sin(radians(") ==2 or self.txtfield.get().find("1/sin(radians(") ==3 or self.txtfield.get().find("1/sin(radians(") ==4 or self.txtfield.get().find("1/sin(radians(") ==5 or self.txtfield.get().find("1/sin(radians(") ==6 or self.txtfield.get().find("1/sin(radians(") ==7 or self.txtfield.get().find("1/sin(radians(") ==8 or self.txtfield.get().find("1/sin(radians(") ==9 or self.txtfield.get().find("1/sin(radians(") ==10 or self.txtfield.get().find("1/sin(radians(") ==11 or self.txtfield.get().find("1/sin(radians(") ==12 or self.txtfield.get().find("1/sin(radians(") ==13 or self.txtfield.get().find("1/sin(radians(") ==14 or self.txtfield.get().find("1/sin(radians(") ==15
            or self.txtfield.get().find("1/cos(radians(")==0 or self.txtfield.get().find("1/cos(radians(")==1 or self.txtfield.get().find("1/cos(radians(")==2 or self.txtfield.get().find("1/cos(radians(")==3 or self.txtfield.get().find("1/cos(radians(")==4 or self.txtfield.get().find("1/cos(radians(")==5 or self.txtfield.get().find("1/cos(radians(")==6 or self.txtfield.get().find("1/cos(radians(")==7 or self.txtfield.get().find("1/cos(radians(")== 8 or self.txtfield.get().find("1/cos(radians(")==9 or self.txtfield.get().find("1/cos(radians(")==10 or self.txtfield.get().find("1/cos(radians(")==11 or self.txtfield.get().find("1/cos(radians(")==12 or self.txtfield.get().find("1/cos(radians(")==13 or self.txtfield.get().find("1/cos(radians(")==14 or self.txtfield.get().find("1/cos(radians(")==15
            or self.txtfield.get().find("1/tan(radians(") == 0 or self.txtfield.get().find("1/tan(radians(") ==1 or self.txtfield.get().find("1/tan(radians(") ==2 or self.txtfield.get().find("1/tan(radians(") ==3 or self.txtfield.get().find("1/tan(radians(") ==4 or self.txtfield.get().find("1/tan(radians(") ==5 or self.txtfield.get().find("1/tan(radians(") ==6 or self.txtfield.get().find("1/tan(radians(") ==7 or self.txtfield.get().find("1/tan(radians(") ==8 or self.txtfield.get().find("1/tan(radians(") ==9 or self.txtfield.get().find("1/tan(radians(") ==10 or self.txtfield.get().find("1/tan(radians(") ==11 or self.txtfield.get().find("1/tan(radians(") ==12 or self.txtfield.get().find("1/tan(radians(") ==13 or self.txtfield.get().find("1/tan(radians(") ==14 or self.txtfield.get().find("1/tan(radians(") ==15
            or self.txtfield.get().find("radians(asin(")==0 or self.txtfield.get().find("radians(asin(")==1 or self.txtfield.get().find("radians(asin(")==2 or self.txtfield.get().find("radians(asin(")==3 or self.txtfield.get().find("radians(asin(")==4 or self.txtfield.get().find("radians(asin(")==5 or self.txtfield.get().find("radians(asin(")==6 or self.txtfield.get().find("radians(asin(")==7 or self.txtfield.get().find("radians(asin(")==8 or self.txtfield.get().find("radians(asin(")==9 or self.txtfield.get().find("radians(asin(")==10 or self.txtfield.get().find("radians(asin(")==11 or self.txtfield.get().find("radians(asin(")==12 or self.txtfield.get().find("radians(asin(")==13 or self.txtfield.get().find("radians(asin(")==14 or self.txtfield.get().find("radians(asin(")==15
            or self.txtfield.get().find("radians(acos(")==0 or self.txtfield.get().find("radians(acos(")==1 or self.txtfield.get().find("radians(acos(")==2 or self.txtfield.get().find("radians(acos(")==3 or self.txtfield.get().find("radians(acos(")==4 or self.txtfield.get().find("radians(acos(")==5 or self.txtfield.get().find("radians(acos(")==6 or self.txtfield.get().find("radians(acos(")==7 or self.txtfield.get().find("radians(acos(")==8 or self.txtfield.get().find("radians(acos(")==9 or self.txtfield.get().find("radians(acos(")==10 or self.txtfield.get().find("radians(acos(")==11 or self.txtfield.get().find("radians(acos(")==12 or self.txtfield.get().find("radians(acos(")==13 or self.txtfield.get().find("radians(acos(")==14 or self.txtfield.get().find("radians(acos(")==15
            or self.txtfield.get().find("radians(atan(")==0 or self.txtfield.get().find("radians(atan(")==1 or self.txtfield.get().find("radians(atan(")==2 or self.txtfield.get().find("radians(atan(")==3 or self.txtfield.get().find("radians(atan(")==4 or self.txtfield.get().find("radians(atan(")==5 or self.txtfield.get().find("radians(atan(")==6 or self.txtfield.get().find("radians(atan(")==7 or self.txtfield.get().find("radians(atan(")==8 or self.txtfield.get().find("radians(atan(")==9 or self.txtfield.get().find("radians(atan(")==10 or self.txtfield.get().find("radians(atan(")==11 or self.txtfield.get().find("radians(atan(")==12 or self.txtfield.get().find("radians(atan(")==13 or self.txtfield.get().find("radians(atan(")==14 or self.txtfield.get().find("radians(atan(")==15
            or self.txtfield.get().find("1/radians(asin(")==0 or self.txtfield.get().find("1/radians(asin(")==1 or self.txtfield.get().find("1/radians(asin(")==2 or self.txtfield.get().find("1/radians(asin(")==3 or self.txtfield.get().find("1/radians(asin(")==4 or self.txtfield.get().find("1/radians(asin(")==5 or self.txtfield.get().find("1/radians(asin(")==6 or self.txtfield.get().find("1/radians(asin(")==7 or self.txtfield.get().find("1/radians(asin(")==8 or self.txtfield.get().find("1/radians(asin(")==9 or self.txtfield.get().find("1/radians(asin(")==10 or self.txtfield.get().find("1/radians(asin(")==11 or self.txtfield.get().find("1/radians(asin(")==12 or self.txtfield.get().find("1/radians(asin(")==13 or self.txtfield.get().find("1/radians(asin(")==14 or self.txtfield.get().find("1/radians(asin(")==15
        or self.txtfield.get().find("1/radians(acos(")==0 or self.txtfield.get().find("1/radians(acos(")==1 or self.txtfield.get().find("1/radians(acos(")==2 or self.txtfield.get().find("1/radians(acos(")==3 or self.txtfield.get().find("1/radians(acos(")==4 or self.txtfield.get().find("1/radians(acos(")==5 or self.txtfield.get().find("1/radians(acos(")==6 or self.txtfield.get().find("1/radians(acos(")==7 or self.txtfield.get().find("1/radians(acos(")==8 or self.txtfield.get().find("1/radians(acos(")==9 or self.txtfield.get().find("1/radians(acos(")==10 or self.txtfield.get().find("1/radians(acos(")==11 or self.txtfield.get().find("1/radians(acos(")==12 or self.txtfield.get().find("1/radians(acos(")==13 or self.txtfield.get().find("1/radians(acos(")==14 or self.txtfield.get().find("1/radians(acos(")==15
        or self.txtfield.get().find("1/radians(atan(")==0 or self.txtfield.get().find("1/radians(atan(")==1 or self.txtfield.get().find("1/radians(atan(")==2 or self.txtfield.get().find("1/radians(atan(")==3 or self.txtfield.get().find("1/radians(atan(")==4 or self.txtfield.get().find("1/radians(atan(")==5 or self.txtfield.get().find("1/radians(atan(")==6 or self.txtfield.get().find("1/radians(atan(")==7 or self.txtfield.get().find("1/radians(atan(")==8 or self.txtfield.get().find("1/radians(atan(")==9 or self.txtfield.get().find("1/radians(atan(")==10 or self.txtfield.get().find("1/radians(atan(")==11 or self.txtfield.get().find("1/radians(atan(")==12 or self.txtfield.get().find("1/radians(atan(")==13 or self.txtfield.get().find("1/radians(atan(")==14 or self.txtfield.get().find("1/radians(atan(")==15
        or self.txtfield.get().find("degrees(asin(")==0 or self.txtfield.get().find("degrees(asin(")==1 or self.txtfield.get().find("degrees(asin(")==2 or self.txtfield.get().find("degrees(asin(")==3 or self.txtfield.get().find("degrees(asin(")==4 or self.txtfield.get().find("degrees(asin(")==5 or self.txtfield.get().find("degrees(asin(")==6 or self.txtfield.get().find("degrees(asin(")==7 or self.txtfield.get().find("degrees(asin(")==8 or self.txtfield.get().find("degrees(asin(")==9 or self.txtfield.get().find("degrees(asin(")==10 or self.txtfield.get().find("degrees(asin(")==11 or self.txtfield.get().find("degrees(asin(")==12 or self.txtfield.get().find("degrees(asin(")==13 or self.txtfield.get().find("degrees(asin(")==14 or self.txtfield.get().find("degrees(asin(")==15
        or self.txtfield.get().find("degrees(acos(")==0 or self.txtfield.get().find("degrees(acos(")==1 or self.txtfield.get().find("degrees(acos(")==2 or self.txtfield.get().find("degrees(acos(")==3 or self.txtfield.get().find("degrees(acos(")==4 or self.txtfield.get().find("degrees(acos(")==5 or self.txtfield.get().find("degrees(acos(")==6 or self.txtfield.get().find("degrees(acos(")==7 or self.txtfield.get().find("degrees(acos(")==8 or self.txtfield.get().find("degrees(acos(")==9 or self.txtfield.get().find("degrees(acos(")==10 or self.txtfield.get().find("degrees(acos(")==11 or self.txtfield.get().find("degrees(acos(")==12 or self.txtfield.get().find("degrees(acos(")==13 or self.txtfield.get().find("degrees(acos(")==14 or self.txtfield.get().find("degrees(acos(")==15
        or self.txtfield.get().find("degrees(atan(")==0 or self.txtfield.get().find("degrees(atan(")==1 or self.txtfield.get().find("degrees(atan(")==2 or self.txtfield.get().find("degrees(atan(")==3 or self.txtfield.get().find("degrees(atan(")==4 or self.txtfield.get().find("degrees(atan(")==5 or self.txtfield.get().find("degrees(atan(")==6 or self.txtfield.get().find("degrees(atan(")==7 or self.txtfield.get().find("degrees(atan(")==8 or self.txtfield.get().find("degrees(atan(")==9 or self.txtfield.get().find("degrees(atan(")==10 or self.txtfield.get().find("degrees(atan(")==11 or self.txtfield.get().find("degrees(atan(")==12 or self.txtfield.get().find("degrees(atan(")==13 or self.txtfield.get().find("degrees(atan(")==14 or self.txtfield.get().find("degrees(atan(")==15
        or self.txtfield.get().find("1/degrees(asin(")==0 or self.txtfield.get().find("1/degrees(asin(")==1 or self.txtfield.get().find("1/degrees(asin(")==2 or self.txtfield.get().find("1/degrees(asin(")==3 or self.txtfield.get().find("1/degrees(asin(")==4 or self.txtfield.get().find("1/degrees(asin(")==5 or self.txtfield.get().find("1/degrees(asin(")==6 or self.txtfield.get().find("1/degrees(asin(")==7 or self.txtfield.get().find("1/degrees(asin(")==8 or self.txtfield.get().find("1/degrees(asin(")==9 or self.txtfield.get().find("1/degrees(asin(")==10 or self.txtfield.get().find("1/degrees(asin(")==11 or self.txtfield.get().find("1/degrees(asin(")==12 or self.txtfield.get().find("1/degrees(asin(")==13 or self.txtfield.get().find("1/degrees(asin(")==14 or self.txtfield.get().find("1/degrees(asin(")==15
        or self.txtfield.get().find("1/degrees(acos(")==0 or self.txtfield.get().find("1/degrees(acos(")==1 or self.txtfield.get().find("1/degrees(acos(")==2 or self.txtfield.get().find("1/degrees(acos(")==3 or self.txtfield.get().find("1/degrees(acos(")==4 or self.txtfield.get().find("1/degrees(acos(")==5 or self.txtfield.get().find("1/degrees(acos(")==6 or self.txtfield.get().find("1/degrees(acos(")==7 or self.txtfield.get().find("1/degrees(acos(")==8 or self.txtfield.get().find("1/degrees(acos(")==9 or self.txtfield.get().find("1/degrees(acos(")==10 or self.txtfield.get().find("1/degrees(acos(")==11 or self.txtfield.get().find("1/degrees(acos(")==12 or self.txtfield.get().find("1/degrees(acos(")==13 or self.txtfield.get().find("1/degrees(acos(")==14 or self.txtfield.get().find("1/degrees(acos(")==15
        or self.txtfield.get().find("1/degrees(atan(")==0 or self.txtfield.get().find("1/degrees(atan(")==1 or self.txtfield.get().find("1/degrees(atan(")==2 or self.txtfield.get().find("1/degrees(atan(")==3 or self.txtfield.get().find("1/degrees(atan(")==4 or self.txtfield.get().find("1/degrees(atan(")==5 or self.txtfield.get().find("1/degrees(atan(")==6 or self.txtfield.get().find("1/degrees(atan(")==7 or self.txtfield.get().find("1/degrees(atan(")==8 or self.txtfield.get().find("1/degrees(atan(")==9 or self.txtfield.get().find("1/degrees(atan(")==10 or self.txtfield.get().find("1/degrees(atan(")==11 or self.txtfield.get().find("1/degrees(atan(")==12 or self.txtfield.get().find("1/degrees(atan(")==13 or self.txtfield.get().find("1/degrees(atan(")==14 or self.txtfield.get().find("1/degrees(atan(")==15)and self.txtfield.get()[len(self.txtfield.get()) - 1] != ")"):
            try:
                self.press("))", 'end')
            except:
                pass
        elif ((self.txtfield.get().find("sin(") == 0 or self.txtfield.get().find("sin(") == 1 or self.txtfield.get().find("sin(") == 2 or self.txtfield.get().find("sin(") == 3 or self.txtfield.get().find("sin(") == 4 or self.txtfield.get().find("sin(") == 5 or self.txtfield.get().find("sin(") == 6 or self.txtfield.get().find("sin(") == 7 or self.txtfield.get().find("sin(") == 8 or self.txtfield.get().find("sin(") == 9 or self.txtfield.get().find("sin(") == 10 or self.txtfield.get().find("sin(") == 11 or self.txtfield.get().find("sin(") == 12 or self.txtfield.get().find("sin(") == 13 or self.txtfield.get().find("sin(") == 14 or self.txtfield.get().find("sin(") == 15
            or self.txtfield.get().find("cos") == 0 or self.txtfield.get().find("cos(") == 1 or self.txtfield.get().find("cos(") == 2 or self.txtfield.get().find("cos(") == 3 or self.txtfield.get().find("cos(") == 4 or self.txtfield.get().find("cos(") == 5 or self.txtfield.get().find("cos(") == 6 or self.txtfield.get().find("cos(") == 7 or self.txtfield.get().find("cos(") == 8 or self.txtfield.get().find("cos(") == 9 or self.txtfield.get().find("cos(") == 10 or self.txtfield.get().find("cos(") == 11 or self.txtfield.get().find("cos(") == 12 or self.txtfield.get().find("cos(") == 13 or self.txtfield.get().find("cos(") == 14 or self.txtfield.get().find("cos(") == 15
            or self.txtfield.get().find("tan") == 0 or self.txtfield.get().find("tan(") == 1 or self.txtfield.get().find("tan(") == 2 or self.txtfield.get().find("tan(") == 3 or self.txtfield.get().find("tan(") == 4 or self.txtfield.get().find("tan(") == 5 or self.txtfield.get().find("tan(") == 6 or self.txtfield.get().find("tan(") == 7 or self.txtfield.get().find("tan(") == 8 or self.txtfield.get().find("tan(") ==  9 or self.txtfield.get().find("tan(") == 10 or self.txtfield.get().find("tan(") == 11 or self.txtfield.get().find("tan(") == 12 or self.txtfield.get().find("tan(") == 13 or self.txtfield.get().find("tan(") == 14 or self.txtfield.get().find("tan(") == 15
            or self.txtfield.get().find("1/sin(") == 0 or self.txtfield.get().find("1/sin(") ==1 or self.txtfield.get().find("1/sin(") ==2 or self.txtfield.get().find("1/sin(") ==3 or self.txtfield.get().find("1/sin(") ==4 or self.txtfield.get().find("1/sin(") ==5 or self.txtfield.get().find("1/sin(") ==6 or self.txtfield.get().find("1/sin(") ==7 or self.txtfield.get().find("1/sin(") ==8 or self.txtfield.get().find("1/sin(") ==9 or self.txtfield.get().find("1/sin(") ==10 or self.txtfield.get().find("1/sin(") ==11 or self.txtfield.get().find("1/sin(") ==12 or self.txtfield.get().find("1/sin(") ==13 or self.txtfield.get().find("1/sin(") ==14 or self.txtfield.get().find("1/sin(") ==15
            or self.txtfield.get().find("1/cos(")==0 or self.txtfield.get().find("1/cos(")==1 or self.txtfield.get().find("1/cos(")==2 or self.txtfield.get().find("1/cos(")==3 or self.txtfield.get().find("1/cos(")==4 or self.txtfield.get().find("1/cos(")==5 or self.txtfield.get().find("1/cos(")==6 or self.txtfield.get().find("1/cos(")==7 or self.txtfield.get().find("1/cos(")== 8 or self.txtfield.get().find("1/cos(")==9 or self.txtfield.get().find("1/cos(")==10 or self.txtfield.get().find("1/cos(")==11 or self.txtfield.get().find("1/cos(")==12 or self.txtfield.get().find("1/cos(")==13 or self.txtfield.get().find("1/cos(")==14 or self.txtfield.get().find("1/cos(")==15
            or self.txtfield.get().find("1/tan(") == 0 or self.txtfield.get().find("1/tan(") ==1 or self.txtfield.get().find("1/tan(") ==2 or self.txtfield.get().find("1/tan(") ==3 or self.txtfield.get().find("1/tan(") ==4 or self.txtfield.get().find("1/tan(") ==5 or self.txtfield.get().find("1/tan(") ==6 or self.txtfield.get().find("1/tan(") ==7 or self.txtfield.get().find("1/tan(") ==8 or self.txtfield.get().find("1/tan(") ==9 or self.txtfield.get().find("1/tan(") ==10 or self.txtfield.get().find("1/tan(") ==11 or self.txtfield.get().find("1/tan(") ==12 or self.txtfield.get().find("1/tan(") ==13 or self.txtfield.get().find("1/tan(") ==14 or self.txtfield.get().find("1/tan(") ==15)and self.txtfield.get()[len(self.txtfield.get()) - 1] != ")"):
            try:
                self.press(")",'end')
            except:
                pass
        try:
            if(self.click==True):
                self.resultset.set(self.percentage())
                self.click=False
            else:
                self.resultset.set(eval(self.txtfield.get()))

        except:
            self.resultset.set("INVALID EXPRESSION")
        return "called"

    def chkleftbracket(self):
        try:
            x = []
            for i in self.txtfield.get():
                x.append(i)
            if ((x[len(x)-1]=="+") or (x[len(x)-1]=="-") or (x[len(x)-1]=="*") or (x[len(x)-1]=="/")):
                num="("
                self.press(num,'end')
            else:
                num="*("
                self.press(num,'end')
        except:
            pass

    def press(self,num,pos):
        self.txtfield.insert(pos,num)
        return num
        #self.expression=self.expression+str(num)    #***********
        #self.txtentry.set(self.expression)          #************

    def __init__(self):
        self.click=False
        self.root=Tk()
        self.root.title("Scientific Calculator")
        self.posi='end'
        self.f1=Frame(self.root)
        self.f2=Frame(self.root)
        self.f3=Frame(self.root)
        self.f4=Frame(self.root)
        self.f5=Frame(self.root)
        self.fm=Frame(self.root)
        self.expression=""              #**************
        self.resultset=StringVar()
        #self.txtentry = StringVar()     #**************
        self.txtfield=Entry(self.f1,font="Calibri 12")#textvariable=self.txtentry #************
        self.txtfield.focus()
        self.result=Entry(self.f3,font="Calibri 12",textvariable=self.resultset)
        self.result.configure(state="disabled")

        self.btnback=Button(self.f1,text="<-",command=lambda :[self.backclear()])
        self.lb1=Label(self.f3,text="Result")
        self.btn1 = Button(self.f2, text="1", command=lambda: [self.press(1,self.posi)])
        self.btn2=Button(self.f2,text="2",command=lambda:[self.press(2,self.posi)])
        self.btn3 = Button(self.f2, text="3", command=lambda: [self.press(3,self.posi)])
        self.btn4 = Button(self.f2, text="4", command=lambda: [self.press(4,self.posi)])
        self.btn5 = Button(self.f2, text="5", command=lambda: [self.press(5,self.posi)])
        self.btn6 = Button(self.f2, text="6", command=lambda: [self.press(6,self.posi)])
        self.btn7 = Button(self.f2, text="7", command=lambda: [self.press(7,self.posi)])
        self.btn8 = Button(self.f2, text="8", command=lambda: [self.press(8,self.posi)])
        self.btn9 = Button(self.f2, text="9", command=lambda: [self.press(9,self.posi)])
        self.btn0 = Button(self.f2, text="0", command=lambda: [self.press(0,self.posi)])
        self.btnadd = Button(self.f2, text="+", command=lambda: [self.press("+",self.posi)])
        self.btnminus = Button(self.f2, text="-", command=lambda: [self.press("-",self.posi)])
        self.btnmultiply = Button(self.f2, text="x", command=lambda: [self.press("*",self.posi)])
        self.btndivide = Button(self.f2, text="/", command=lambda: [self.press("/",self.posi)])
        self.btnclear = Button(self.f2, text="Clear", command=lambda: [self.clear()])
        self.btnequate = Button(self.f2, text="=", command=lambda: [self.evaluate()])

#2222222222222222222222222222222222222222222222
        self.lbl=Label(self.f4,text="Special Symbols")
        self.btnleftbracket=Button(self.f2,text="(",command=lambda:[self.chkleftbracket()])
        self.btnrightbracket = Button(self.f2, text=")", command=lambda: [self.chkrightbracket()])
        self.btndot = Button(self.f2, text=".", command=lambda: [self.press(".",self.posi)])
        self.btnsquareroot = Button(self.f2, text="√", command=lambda:[self.press("**(0.5)",self.posi)])
        self.btnpower = Button(self.f2, text="^", command=lambda: [self.press("**",self.posi)])

        self.btnpie=Button(self.f2,text="∏",command=lambda:[self.press("(3.14)*",self.posi)])
#-------------===========----------------
        self.btnfactors = Button(self.f5, text="Factors", command=lambda: [self.factors()])
        self.btnfactorial = Button(self.f5, text="!", command=lambda: [self.factorial()])
        self.btnexp = Button(self.f5, text="e", command=lambda: [self.press("(2.718281828)",self.posi)])
        self.btnlog = Button(self.f5, text="log()", command=lambda: [self.log()])
        self.btnadvexpo=Button(self.f5,text="e^",command=self.advexpo)
        self.btnans = Button(self.f2, text="ANS", command=lambda:[self.ansbtn()])
        self.btnpercentage=Button(self.f2,text="%",command=lambda:[self.percentage()])

        #trigo
        self.ans=IntVar()

        self.degrad=Checkbutton(self.f5,text="Degrees",variable=self.ans,command=lambda:[self.trigno("","")])

        self.ans2=IntVar()
        self.inversetrigno=Checkbutton(self.f5,text="Inverse",variable=self.ans2,command=lambda:[self.trigno("","")])


        self.sinvalue=''
        self.cosvalue = ''
        self.tanvalue = ''
        self.cosecavlue = ''
        self.secavlue = ''
        self.cotvalue = ''

        self.btnsin = Button(self.f5, text="sin()", command=lambda: [self.trigno(self.sinvalue,'end')])
        self.btncos = Button(self.f5, text="cos()", command=lambda: [self.trigno(self.cosvalue, 'end')])
        self.btntan = Button(self.f5, text="tan()", command=lambda: [self.trigno(self.tanvalue, 'end')])
        self.btncosec = Button(self.f5, text="cosec()", command=lambda: [self.trigno(self.cosecavlue, 'end')])
        self.btnsec = Button(self.f5, text="sec()", command=lambda: [self.trigno(self.secavlue, 'end')])
        self.btncot = Button(self.f5, text="cot()", command=lambda: [self.trigno(self.cotvalue, 'end')])
        self.trigno("", "")


    #============================================
        self.txtfield.grid(row=0,column=0)
        self.txtfield.grid_configure(ipadx=100)
        self.lb1.grid(row=1,column=0)
        self.result.grid(row=1,column=1)
        self.result.grid_configure(ipadx=120, ipady=6)
        self.btnback.grid(row=0,column=1)
        #self.result.grid_configure(ipadx=50)


        self.btn1.grid(row=0,column=0)
        self.btn1.grid_configure(ipadx=5,ipady=6)
        self.btn2.grid(row=0, column=1)
        self.btn2.grid_configure(ipadx=5, ipady=6)
        self.btn3.grid(row=0, column=2)
        self.btn3.grid_configure(ipadx=5, ipady=6)
        self.btnadd.grid(row=0,column=3)
        self.btnadd.grid_configure(ipadx=5, ipady=6)

        self.btn4.grid(row=1, column=0)
        self.btn4.grid_configure(ipadx=5, ipady=6)
        self.btn5.grid(row=1, column=1)
        self.btn5.grid_configure(ipadx=5, ipady=6)
        self.btn6.grid(row=1, column=2)
        self.btn6.grid_configure(ipadx=5, ipady=6)
        self.btnminus.grid(row=1, column=3)
        self.btnminus.grid_configure(ipadx=5, ipady=6)

        self.btn7.grid(row=2, column=0)
        self.btn7.grid_configure(ipadx=5, ipady=6)
        self.btn8.grid(row=2, column=1)
        self.btn8.grid_configure(ipadx=5, ipady=6)
        self.btn9.grid(row=2, column=2)
        self.btn9.grid_configure(ipadx=5, ipady=6)
        self.btnmultiply.grid(row=2, column=3)
        self.btnmultiply.grid_configure(ipadx=5, ipady=6)

        self.btnclear.grid(row=3, column=0)
        self.btnclear.grid_configure(ipadx=5, ipady=6)
        self.btn0.grid(row=3, column=1)
        self.btn0.grid_configure(ipadx=5, ipady=6)
        self.btnequate.grid(row=3, column=2)
        self.btnequate.grid_configure(ipadx=5, ipady=6)
        self.btndivide.grid(row=3, column=3)
        self.btndivide.grid_configure(ipadx=5, ipady=6)

        self.btnleftbracket.grid(row=0, column=4)
        self.btnleftbracket.grid_configure(ipadx=5, ipady=6)

        self.btnrightbracket.grid(row=0, column=5)
        self.btnrightbracket.grid_configure(ipadx=5, ipady=6)

        self.btnpower.grid(row=1, column=4)
        self.btnpower.grid_configure(ipadx=5, ipady=6)
        self.btnsquareroot.grid(row=1, column=5)
        self.btnsquareroot.grid_configure(ipadx=5, ipady=6)

        self.btnpercentage.grid(row=2,column=4)
        self.btnpercentage.grid_configure(ipadx=5,ipady=6)
        self.btnans.grid(row=2,column=5)
        self.btnans.grid_configure(ipadx=5,ipady=6)
        self.btndot.grid(row=3, column=4)
        self.btndot.grid_configure(ipadx=5, ipady=6)
        self.btnpie.grid(row=3, column=5)
        self.btnpie.grid_configure(ipadx=5, ipady=6)

        self.lbl.grid(row=0, column=1)
        self.btnfactorial.grid(row=1, column=0)
        self.btnfactorial.grid_configure(ipadx=5, ipady=6)
        self.btnfactors.grid(row=1, column=1)
        self.btnfactors.grid_configure(ipadx=5, ipady=6)

        self.btnexp.grid(row=1, column=2)
        self.btnexp.grid_configure(ipadx=5, ipady=6)
        self.btnlog.grid(row=1, column=3)
        self.btnlog.grid_configure(ipadx=5, ipady=6)
        self.btnadvexpo.grid(row=1,column=4)
        self.btnadvexpo.grid_configure(ipadx=5,ipady=6)

        self.degrad.grid(row=2,column=0)
        self.inversetrigno.grid(row=3,column=0)
        self.btnsin.grid(row=2, column=1)
        self.btnsin.grid_configure(ipadx=5, ipady=6)
        self.btncos.grid(row=2, column=2)
        self.btncos.grid_configure(ipadx=5, ipady=6)
        self.btntan.grid(row=2, column=3)
        self.btntan.grid_configure(ipadx=5, ipady=6)
        self.btncosec.grid(row=3, column=1)
        self.btncosec.grid_configure(ipadx=5, ipady=6)
        self.btnsec.grid(row=3, column=2)
        self.btnsec.grid_configure(ipadx=5, ipady=6)
        self.btncot.grid(row=3, column=3)
        self.btncot.grid_configure(ipadx=5, ipady=6)



        #============================
        self.f1.pack()
        self.f3.pack()
        self.f2.pack()
        self.f4.pack()
        self.f5.pack()
        self.fm.pack()

    #============================
        self.root.mainloop()
#-------------
obj=calc()