import os
import smtplib
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import dweepy


#LDR=[0,0]
#LDR_status=[]
smoke_status=[]
motion_status=[]
GPIO.setmode(GPIO.BCM)
#GPIO.setup(2, GPIO.IN)
#GPIO.setup(3, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(17, GPIO.IN)


from email.mime.text import MIMEText
while True:
    humidity,temperature=Adafruit_DHT.read_retry(11,4)
##    LDR[0]=GPIO.input(2)
##    LDR[1]=GPIO.input(3)
##    if LDR==11:
##        LDR_status="Too much light"
##    elif LDR==10:
##        LDR_status="Enough light"
##    elif LDR==01:
##        LDR_status="Not enough light"
##    else:
##        LDR_status="Too dark"
    smoke=GPIO.input(14)
    if smoke==0:
        smoke_status="Safe"
    else:
        smoke_status="Danger"
    motion=GPIO.input(17)
    if motion==1:
        motion_status="There was movement"
    else:
        motion_status="There was no movement"
    #dweepy.dweet_for('Monitoring',{'Temperature':temperature,'Humidity':humidity,'Smoke Detection':smoke_status,'Motion Detection':motion_status})
    dweepy.dweet_for('Monitoring',{'Temperature':temperature,'Humidity':humidity})
    text_file = open("output.txt", "w")
    text_file.write("Temperature = ")
    text_file.write(str(temperature))    
    text_file.write(' C   ')
    text_file.write("\n")
    text_file.write("Humidity = ")
    text_file.write(str(humidity))
    text_file.write("\n")
##    text_file.write("Light Detection: ")
##    text_file.write(LDR_status)
##    print LDR_status
    text_file.write("\n")
    text_file.write("Smoke Detection: ")
    text_file.write(smoke_status)
    
    text_file.write("\n")
    text_file.write("Motion Detection: ")
    text_file.write(motion_status)
    text_file.write("\n")
    print motion_status
    text_file.close()
    if (int(temperature)>30.0 or int(temperature)<20.0 or int(humidity)<40.0 or int(humidity)>60.0 or smoke==1 or motion==1):
        os.system("mpack -s \"Sensor Data\" /home/pi/output.txt trkulakarni@gmail.com")
