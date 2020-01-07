def send_notification(temperature):
    status = 'Tempeaure too hot! CPU temp=' + str(temperature)
    data = urllib.urlencode({'api_key' : KEY_TWITTER, 'status': status})
    response = urllib2.urlopen(url=BASE_URL_TWITTER, data=data)
    print(response.read())