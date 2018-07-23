import urllib2
def pull():
    url = "https://www.tide-forecast.com/locations/Swansea-Wales/tides/latest"
    page = urllib2.urlopen(url)
    content= page.read()
    print(content)

    for line in content:
        if 
pull()