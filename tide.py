import urllib2
import re
import calendar
def pull():
    url = "https://www.tide-forecast.com/locations/Swansea-Wales/tides/latest"
    page = urllib2.urlopen(url)
    content = page.readlines()
    
    return content

def read(content):
    out = []
    for line in content:
        lineS = line.strip()
        if any(ext in lineS for ext in list(calendar.day_name)) or '<td class="time tide">' in lineS or '<td class="tide">High Tide' in lineS or '<td class="tide">Low Tide'in lineS:
            out.append(format(line))
    return out




def format(input_string):
    out_string = re.sub(r'<.*?>', '', input_string)
    return out_string.strip()

def display(times):
    for lines in times:
        print(lines)

display(read(pull()))



