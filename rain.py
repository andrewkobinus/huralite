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