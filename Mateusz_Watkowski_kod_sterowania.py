#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import RPi.GPIO as GPIO
import time
import zbar
import Tkinter as tk
from Tkinter import Label
from Tkinter import *
import threading
import xlwt
import os

global a
global symbol
it=0
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Raport zbiorczy")
sheet1.write(0, 0, "Numer paczki")
sheet1.write(0, 1, "Data")
sheet1.write(0, 2, "Godzina")
sheet1.write(0, 3, "Odczytany kod")
GPIO.setmode(GPIO.BCM)
root = tk.Tk()

flag_blinking = False   
flag_exiting = False

#komentarze
kom1="Powrot do pozycji poczatkowej"
kom2="Oczekiwanie na przeciecie wiazki podczerwieni"

pinwyj=5
pinwej=4


print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
nazwa_bazy=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
zawartosc="/home/pi/Desktop/"

GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)

def wiazka():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(5,GPIO.OUT)
    GPIO.output(5, GPIO.HIGH)
    i=1
    w=0
    while True:
        GPIO.wait_for_edge(4, GPIO.FALLING)
        print ("Wiazka przecieta, numer:", i)
        t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(t)
        i=i+1
        return 1
    #except KeyboardInterrupt:
        #GPIO.cleanup()
        #return 0
    
def czytnik():
    a=''
    ts=time.strftime("%H:%M:%S", time.localtime())
#zdefiniowanie zmiennej do ktorej wczytana zostala funkcja odczytywania kodu
    proc = zbar.Processor()

# zdefiniowanie wyjscia video, ktore jest zrodlem pochodzenia obrazu
    device = '/dev/video0'
    proc.init(device)

# wlaczenie okna z aktualnym obrazem z kamery
    proc.visible = True

# odczytanie jednego kodu i zamkniecie procesu
    proc.process_one(5)

# wypianie wynikow
    for symbol in proc.results:
        #print ('Odczytane haslo: "%s"' % symbol.data)
        a=symbol.data
    if a == '':
        print "Nie znaleziono"
        labelkom = Label(root, text="                                                        ")
        labelkom.grid(row=2, column=1)
        labelkom = Label(root, text="Nie znaleziono")
        labelkom.grid(row=2, column=1)
        #sheet1.write(nr1, 0, it)
        #sheet1.write(nr1, 1, ts)
        #sheet1.write(nr1, 2, "Nie znaleziono")
        #book.save(zawartosc)
        return 0
    else:
        print("Odczytano kod QR: ")
        print(a)
        labelkom = Label(root, text="                                                      ")
        labelkom.grid(row=2, column=1)
        labelkom = Label(root, text=a)
        labelkom.grid(row=2, column=1)
        #sheet1.write(1, 0, 1)
        #sheet1.write(1, 1, ts)
        #sheet1.write(1, 2, a)
        #book.save(zawartosc)
        return a

def pozycja0():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    #GPIO.setup(13,GPIO.OUT)
    #GPIO.setup(6,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    pwm26=GPIO.PWM(26,50)
    pwm19=GPIO.PWM(19,50)
    #pwm13=GPIO.PWM(13,50)
    #pwm6=GPIO.PWM(6,50)
    pwm20=GPIO.PWM(20,50)
    pwm21=GPIO.PWM(21,50)
    pwm26.start(15)
    time.sleep(1)
    pwm21.start(11)
    time.sleep(0.5)
    pwm20.start(5.5)
    pwm19.start(7.5)
    time.sleep(1)
    GPIO.cleanup()

def pozycja1():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    #GPIO.setup(13,GPIO.OUT)
    #GPIO.setup(6,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    pwm26=GPIO.PWM(26,50)
    pwm19=GPIO.PWM(19,50)
    #pwm13=GPIO.PWM(13,50)
    #pwm6=GPIO.PWM(6,50)
    pwm20=GPIO.PWM(20,50)
    pwm21=GPIO.PWM(21,50)
    pwm26.start(15)
    pwm20.start(10.2)
    time.sleep(0.5)
    pwm19.start(4.2)
    #pwm13.start(10)
    #pwm6.start(7.5)
    pwm21.start(10.2)
    time.sleep(1)
    GPIO.cleanup()

def pozycja2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    #GPIO.setup(13,GPIO.OUT)
    #GPIO.setup(6,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    pwm26=GPIO.PWM(26,50)
    pwm19=GPIO.PWM(19,50)
    #pwm13=GPIO.PWM(13,50)
    #pwm6=GPIO.PWM(6,50)
    pwm20=GPIO.PWM(20,50)
    pwm21=GPIO.PWM(21,50)
    pwm26.start(10.5)
    pwm20.start(10.2)
    pwm19.start(4.2)
    #pwm13.start(10)
    #pwm6.start(7.5)
    pwm21.start(10.2)
    time.sleep(1)
    GPIO.cleanup()
    
def pozycja3():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    #GPIO.setup(13,GPIO.OUT)
    #GPIO.setup(6,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    pwm26=GPIO.PWM(26,50)
    pwm19=GPIO.PWM(19,50)
    #pwm13=GPIO.PWM(13,50)
    #pwm6=GPIO.PWM(6,50)
    pwm20=GPIO.PWM(20,50)
    pwm21=GPIO.PWM(21,50)
    pwm26.start(7.5)
    pwm20.start(10.2)
    pwm19.start(4.2)
    #pwm13.start(10)
    #pwm6.start(7.5)
    pwm21.start(10.2)
    time.sleep(1)
    GPIO.cleanup()   

def pozycja4():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    #GPIO.setup(13,GPIO.OUT)
    #GPIO.setup(6,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    pwm26=GPIO.PWM(26,50)
    pwm19=GPIO.PWM(19,50)
    #pwm13=GPIO.PWM(13,50)
    #pwm6=GPIO.PWM(6,50)
    pwm20=GPIO.PWM(20,50)
    pwm21=GPIO.PWM(21,50)
    pwm26.start(5)
    pwm20.start(10.2)
    pwm19.start(4.2)
    #pwm13.start(10)
    #pwm6.start(7.5)
    pwm21.start(10.2)
    time.sleep(1)
    GPIO.cleanup()

def program():
    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(5,GPIO.OUT)
    pozycja0()
    w=1
    i=1
    global it
    ts=time.strftime("%H:%M:%S", time.localtime())
    data=time.strftime("%Y-%m-%d", time.localtime())
    while w!=0:
        w=wiazka()
        print ("Wiazka przecieta, numer:", i)
        i=i+1
        it=it+1
        p=czytnik()
        #print(p)
        if p==0:
            pozycja1()
            print("Przesuniecie do pozycji nr 1")
            print("Druga proba odczytu kodu QR w pozycji nr 1")
            k=czytnik()
            if k==0:
                pozycja2()
                print("Przesuniecie do pozycji nr 2")
                print("Trzecia proba odczytu kodu QR w pozycji nr 2")
                q=czytnik()
                if q==0:
                    pozycja3()
                    print("Przesuniecie do pozycji nr 3")
                    print("Czwarta proba odczytu kodu QR w pozycji nr 3")
                    l=czytnik()
                    if l==0:
                        pozycja4()
                        print("Przesuniecie do pozycji nr 4")
                        print("Piata proba odczytu kodu QR w pozycji nr 4")
                        z=czytnik()
                        if z==0:
                            print("W zadnej pozycji nie znaleziono kodu QR")
                            pozycja0()
                            print(kom1)
                            data=time.strftime("%Y-%m-%d", time.localtime())
                            ts=time.strftime("%H:%M:%S", time.localtime())
                            sheet1.write(it, 0, it)
                            sheet1.write(it, 1, data)
                            sheet1.write(it, 2, ts)
                            sheet1.write(it, 3, "Nie znaleziono")
                            book.save(zawartosc+str(nazwa_bazy)+".xls")
                        else:
                            pozycja0()
                            print(kom1)
                            data=time.strftime("%Y-%m-%d", time.localtime())
                            ts=time.strftime("%H:%M:%S", time.localtime())
                            sheet1.write(it, 0, it)
                            sheet1.write(it, 1, data)
                            sheet1.write(it, 2, ts)
                            sheet1.write(it, 3, z)
                            book.save(zawartosc+str(nazwa_bazy)+".xls")
                    else:
                        pozycja0()
                        print(kom1)
                        data=time.strftime("%Y-%m-%d", time.localtime())
                        ts=time.strftime("%H:%M:%S", time.localtime())
                        sheet1.write(it, 0, it)
                        sheet1.write(it, 1, data)
                        sheet1.write(it, 2, ts)
                        sheet1.write(it, 3, l)
                        book.save(zawartosc+str(nazwa_bazy)+".xls")
                else:
                    pozycja0()
                    print(kom1)
                    data=time.strftime("%Y-%m-%d", time.localtime())
                    ts=time.strftime("%H:%M:%S", time.localtime())
                    sheet1.write(it, 0, it)
                    sheet1.write(it, 1, data)
                    sheet1.write(it, 2, ts)
                    sheet1.write(it, 3, q)
                    book.save(zawartosc+str(nazwa_bazy)+".xls")
            else:
                pozycja0()
                print(kom1)
                data=time.strftime("%Y-%m-%d", time.localtime())
                ts=time.strftime("%H:%M:%S", time.localtime())
                sheet1.write(it, 0, it)
                sheet1.write(it, 1, data)
                sheet1.write(it, 2, ts)
                sheet1.write(it, 3, k)
                book.save(zawartosc+str(nazwa_bazy)+".xls")
        else:
            pozycja0()
            print(kom1)
            data=time.strftime("%Y-%m-%d", time.localtime())
            ts=time.strftime("%H:%M:%S", time.localtime())
            sheet1.write(it, 0, it)
            sheet1.write(it, 1, data)
            sheet1.write(it, 2, ts)
            sheet1.write(it, 3, p)
            book.save(zawartosc+str(nazwa_bazy)+".xls")
    return it

def manual():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    pwm26=GPIO.PWM(26,50)
    pwm19=GPIO.PWM(19,50)
    pwm20=GPIO.PWM(20,50)
    pwm21=GPIO.PWM(21,50)
    pwm26.start(float(a.get()))
    pwm21.start(float(b.get()))
    pwm20.start(float(c.get()))
    pwm19.start(float(d.get()))
    time.sleep(1)
    GPIO.cleanup()            
  
def blink():    
    global flag_blinking    
    global flag_exiting     
    while ( True ):  
        if (flag_blinking == True):    
            program()  
        if (flag_exiting == True):  
            return   
        time.sleep(1.0)

def switchon():
    GPIO.setmode(GPIO.BCM)
    global flag_blinking    
    flag_blinking = True    
    print ('Program wznowiony')
    GPIO.setup(5,GPIO.OUT)
    GPIO.output(pinwyj, GPIO.HIGH)
    
def switchoff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5,GPIO.OUT)
    global flag_blinking    
    flag_blinking = False        
    print ('Program zatrzymany')
    #GPIO.cleanup()
    GPIO.output(pinwyj, GPIO.LOW)

def kill():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5,GPIO.OUT)
    global flag_exiting     
    flag_exiting = True
    #GPIO.cleanup()
    GPIO.output(pinwyj, GPIO.LOW)
    root.destroy()
    raise SystemExit

#thread = threading.Thread(target=blink)    
#thread.start()  

  
naglowek1 = Label(root, text="Interfejs uzytkownika manipulatora z kamera ", width=40, bg="blue", fg="white")
naglowek1.grid(row=0)
onbutton = tk.Button(root, text = "Start", command = switchon)      
onbutton.grid(row=1)            
stopbutton = tk.Button(root, text = "Stop", command = switchoff)      
stopbutton.grid(row=2)
killbutton = tk.Button(root, text = "Zamknij", command = kill)      
killbutton.grid(row=9)
#labelkom = Label(root, text=a)
#labelkom.grid(row=1, column=1)
#manualbutton = tk.Button(root, text = "Tryb reczny", command = manual)      
#manualbutton.pack()
naglowek2 = Label(root, text="Tryb reczny", width=40, bg="green", fg="white")
naglowek2.grid(row=4)
naglowek_zmienne = Label(root, text="Wprowadz wartosci od 0.1 do 15", width=40, bg="yellow", fg="black")
naglowek_zmienne.grid(row=4, column=1)
naglowek3 = Label(root, text="Obrot manipulatora: ").grid(row=5, column=0)
a = DoubleVar()
zmienna_a = Entry(root, textvariable=a, width=25, bg="lightyellow").grid(row=5, column=1)
naglowek4 = Label(root, text="Pierwsze ramie: ").grid(row=6, column=0)
b = DoubleVar()
zmienna_b = Entry(root, textvariable=b, width=25, bg="lightyellow").grid(row=6, column=1)
naglowek5 = Label(root, text="Drugie ramie: ").grid(row=7, column=0)
c = DoubleVar()
zmienna_c = Entry(root, textvariable=c, width=25, bg="lightyellow").grid(row=7, column=1)
naglowek6 = Label(root, text="Ramie z kamera: ").grid(row=8, column=0)
d = DoubleVar()
zmienna_d = Entry(root, textvariable=d, width=25, bg="lightyellow").grid(row=8, column=1)


####manual

thread = threading.Thread(target=blink)    
thread.start() 

manualbotton = tk.Button(root, text = "Przesun manipulator", command = manual)      
manualbotton.grid(row=9, column=1)
#czytanie = tk.Button(root, text = "Skanuj kod", command = czytnik)      
#czytanie.grid(row=9, column=1)
root.mainloop() 
