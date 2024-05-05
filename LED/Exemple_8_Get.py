import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
from machine import Pin, PWM
import time

pin = [17,18,19]

leds = [PWM(Pin(17, mode=Pin.OUT)),PWM(Pin(18, mode=Pin.OUT)),PWM(Pin(19, mode=Pin.OUT))]

maison = {"Gryffindor" : [170,0,0],
           "Slytherin" : [0,170,0],
           "Ravenclaw" : [0,0,170],
           "Hufflepuff" : [150,150,0],
           "off" : [0,0,0]}


for i in leds:
    i.freq(1_000)
    i.duty_u16(0)

def off():
    for i in leds:
        i.duty_u16(0)
        
colors = [100,255,170]

def setColor(color):
    index = 0
    for i in color:
        leds[index].duty_u16(i*50)
        index+=1

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'ECSSO'
password = 'motdepasse'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.lainocs.fr/characters/harry-potter"



while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()["house"])
        if r.json()["house"] == "Gryffindor":
            setColor(maison["Gryffindor"])
            
        elif r.json()["house"] == "Slytherin":
            setColor(maison["Slytherin"])
            
        elif r.json()["house"] == "Ravenclaw":
            setColor(maison["Ravenclaw"])
        
        elif r.json()["house"] == "Hufflepuff":
            setColor(maison["Hufflepuff"])
        r.close() # ferme la demande
        utime.sleep(1)  
    except Exception as e:
        print(e)
    
