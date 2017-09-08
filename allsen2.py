import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import dweepy
LDR=[]
LDR_status=[]
smoke_status=[]
motion_status=[]
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(17, GPIO.IN)

while True:
    humidity,temperature=Adafruit_DHT.read_retry(11,4)
    LDR[1]=GPIO.input(2)
    LDR[2]=GPIO.input(3)
    if LDR==11:
        LDR_status="Too much light"
    elif LDR==10:
        LDR_status="Enough light"
    elif LDR==01:
        LDR_status="Not enough light"
    else:
        LDR_status="Too dark"
    smoke=GPIO.input(14)
    if smoke==1:
        smoke_status="Danger"
    else:
        smoke_status="Safe"
    motion=GPIO.input(17)
    if motion==1:
        motion_status="There was movement"
    else:
        motion_status="There was no movement"
    dweepy.dweet_for('Monitoring',{'Temperature':temperature,'Humidity':humidity,'Light Detection':LDR_status,'Smoke Detection':smoke_status,'Motion Detection':motion_status})
