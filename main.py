import httplib
import urllib2
import os
import urllib

key = "PDBRLD1GR2VX5V1G"  # Put your API Key here
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key 

MAX_TEMP = 50.0
MIN_T_BETWEEN_WARNINGS = 60 # Minutes

BASE_URL_TWITTER = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update/'
KEY_TWITTER = '2LU2MP6EX2X1RKW9'


import time
from gpiozero import Buzzer, InputDevice
import RPi.GPIO as GPIO
import Adafruit_DHT
 
no_rain = InputDevice(23)
als = True


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)


def send_notification(temperature):
    status = 'Tempeaure too hot! CPU temp=' + str(temperature)
    data = urllib.urlencode({'api_key' : KEY_TWITTER, 'status': status})
    response = urllib2.urlopen(url=BASE_URL_TWITTER, data=data)
    print(response.read())

def cpu_temp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp = dev.read()[5:-3]
    return cpu_temp





def temp():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)
    if humidity is not None and temperature is not None:
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        
        if temperature < MAX_TEMP:
            send_notification(temperature)
            print ("here")
            
        
        
        print ('{0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity))
    else:
        print ('can not connect to the sensor!')

    conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (temperature, humidity))
    print conn.read()
    # Closing the connection
    conn.close()
    

def rain(no_rain):
    if no_rain.is_active:
        print("no rain")
        rainv = 0
        conn = urllib2.urlopen(baseURL + '&field3=%s' % (rainv))
        print conn.read()
        # Closing the connection
        conn.close()
        

    if not no_rain.is_active:
        print("It's raining")
        rainv = 1
        conn = urllib2.urlopen(baseURL + '&field3=%s' % (rainv))
        print conn.read()
        # Closing the connection
        conn.close()
    



def light():
    if (GPIO.input(4)) < 1:
        print ("its bright here")
        light = 1
        conn = urllib2.urlopen(baseURL + '&field4=%s' % (light))
        print conn.read()
        # Closing the connection
        conn.close()
    else:
        print ("its dark here")
        light = 0
        conn = urllib2.urlopen(baseURL + '&field4=%s' % (light))
        print conn.read()
        # Closing the connection
        conn.close()

good = True
while good:
    print("temperature")   
    temp()
    print("weather")
    rain(no_rain)
    print("light")
    light()
    time.sleep(.1)
    good = False


