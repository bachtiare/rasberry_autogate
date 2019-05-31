import requests
import pygame
import RPi.GPIO as GPIO
import time
from Tkinter import * 

GPIO.setmode(GPIO.BCM)
#power dan gagal
GPIO.setup(4, GPIO.OUT)
#koneksi ke server
GPIO.setup(17, GPIO.OUT)
#boarding sukses
GPIO.setup(27, GPIO.OUT)
#membuka gate
GPIO.setup(22, GPIO.OUT)
#led jikapower hidup
GPIO.output(4, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)

#check koneksi
try:
    url_api = "http://192.168.0.102:8002/"
    koneksi = requests.get(url = url_api)
  
    if koneksi.status_code == 200 :
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)
except:
    GPIO.output(17, GPIO.LOW)

#input boarding pass
root = Tk()
def check_data(boarding_pass):
    try:
        #mengecek koneksi server
        url_api = "http://192.168.0.102:8002"
        koneksi = requests.get(url = url_api)
        if koneksi.status_code == 200 :
            GPIO.output(17, GPIO.HIGH)
        else:
            GPIO.output(17, GPIO.LOW)
        if boarding_pass == 'BAU2111180000501':
            GPIO.output(22, GPIO.LOW)
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/Documents/raspi/accepted.wav')
            pygame.mixer.music.play()
            GPIO.output(27, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(27, GPIO.LOW)
            time.sleep(2)
            #membuka gate
            GPIO.output(22, GPIO.HIGH)
        else :
            if boarding_pass == '0002399200':
                GPIO.output(22, GPIO.LOW)
                pygame.mixer.init()
                pygame.mixer.music.load('/home/pi/Documents/raspi/accepted.wav')
                pygame.mixer.music.play()
                GPIO.output(27, GPIO.HIGH)
                time.sleep(2)
                GPIO.output(27, GPIO.LOW)
                time.sleep(2)
                #membuka gate
                GPIO.output(22, GPIO.HIGH)
            else:
                #print(porter.status_code)
                pygame.mixer.init()
                pygame.mixer.music.load('/home/pi/Documents/raspi/rejected.wav')
                pygame.mixer.music.play()
                GPIO.output(4, GPIO.LOW)
                time.sleep(1)
                GPIO.output(4, GPIO.HIGH)
                time.sleep(1)
            #print(params)
    except requests.exceptions.RequestException as e:
        pygame.mixer.init()
        pygame.mixer.music.load('/home/pi/Documents/raspi/rejected.wav')
        pygame.mixer.music.play()
        #terjadi kesalahan system
        GPIO.output(4, GPIO.LOW)
        time.sleep(1)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(4, GPIO.LOW)
        time.sleep(1)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(4, GPIO.LOW)
        time.sleep(1)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(17, GPIO.LOW)
        
        print(e)
def returnEntry(arg=None):
	result = myEntry.get()
	check_data(result)
	resultLabel.config(text=result)
	myEntry.delete(0,END)
 
# Create the Entry widget
myEntry = Entry(root, width=20)
myEntry.focus()
myEntry.bind("<Return>",returnEntry)
myEntry.pack()

# Create the Enter button
enterEntry = Button(root, text= "Enter", command=returnEntry)
enterEntry.pack(fill=X)
 
# Create and emplty Label to put the result in
resultLabel = Label(root, text = "")
resultLabel.pack(fill=X)
 
 
root.geometry("+750+400")
 
root.mainloop()



