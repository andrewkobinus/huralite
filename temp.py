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