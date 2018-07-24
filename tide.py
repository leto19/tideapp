import re
import calendar
from urllib.request import urlopen
import lib2to3
import dateparser
from datetime import datetime
from icalendar import Event, Calendar
def pull():
    url = "https://www.tide-forecast.com/locations/Swansea-Wales/tides/latest"
    page = urlopen(url)
    content = page.readlines()
    return content

def read(content):
    out = []
    for line in content:
        lineS = line.strip().decode('utf_8')
        if any(ext in lineS for ext in list(calendar.day_name)) or '<td class="time tide">' in lineS or '<td class="tide">High Tide' in lineS or '<td class="tide">Low Tide'in lineS:
            out.append(remove_tags(lineS))
    return out


def format_list(in_list):
    out_dict = dict()
    for i in range(len(in_list)):
        if any(ext in in_list[i] for ext in list(calendar.day_name)):
            if any(ext in in_list[i+7] for ext in list(calendar.day_name)):
                out_dict.update({in_list[i]:[(in_list[i+1],in_list[i+2]),(in_list[i+3],in_list[i+4]),(in_list[i+5],in_list[i+6])]})
            else:
                out_dict.update({in_list[i]:[(in_list[i+1],in_list[i+2]),(in_list[i+3],in_list[i+4]),(in_list[i+5],in_list[i+6]),(in_list[i+7],in_list[i+8])]})
            #this is very messy, but it works
    return out_dict

def create_cal(in_dict):
    cal = Calendar()
    for date in in_dict.keys():
        print(date)
        for i in range(len(in_dict[date])):
            print(in_dict[date][i])
        # event = Event()
        # day = dateparser.parse(date + in_dict[date][0][0])
        # event.add('summary', in_dict[date][0][1])
        # event.add('dtstart', day)
        # print(event)
def remove_tags(input_string):
    out_string = re.sub(r'<.*?>', '', input_string)
    return out_string.strip()

def display(times):
    for lines in times:
        print(lines)

a = read(pull())
display(a)
b = format_list(a)
create_cal(b)

