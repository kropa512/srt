__author__ = 'jurek'
import re
import sys
import os

def timetext_to_tseconds(time_text):
    return (int(time_text[0:2])*3600 + int(time_text[3:5])*60 + int(time_text[6:8])) * 1000 + int(time_text[9:12])

def time_tseconds_to_timetext(timesecond):
    tsdseconds = timesecond % 1000
    timesecond = timesecond / 1000
    seconds = timesecond % 60
    timesecond -= (timesecond % 60)
    minutes = (timesecond / 60) % 60
    timesecond -= ((timesecond / 60) % 60) * 60
    hours = (timesecond / 3600) % 3600
    return "{0:02d}:{1:02d}:{2:02d},{3:03d}".format(hours, minutes, seconds, tsdseconds)

def shiftedTime(timetext, shift):
    return str(time_tseconds_to_timetext(timetext_to_tseconds(timetext) + shift))

def bothshift(liste, shift):
    return [shiftedTime(m, shift) for m in liste]

SHIFT = 1000
handle = open(sys.argv[1],"r")
if os._exists(sys.argv[2]):
    os.remove(sys.argv[2])
handle_out = open(sys.argv[2], "w")
SHIFT = int(sys.argv[3])

for lines in handle:
    mm = re.findall('\d\d:\d\d:\d\d\,\d\d\d', lines)
    if len(mm) == 2:
        shifted = bothshift(mm, SHIFT)
        handle_out.write(shifted[0] + ' --> ' + shifted[1] + '\n')
        print shifted[0] + ' --> ' + shifted[1] + '\n'
    else:
        print lines
        handle_out.write(lines)
handle_out.close()