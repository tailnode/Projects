#!/usr/bin/python3

import threading
import os
from time import mktime
from time import localtime



def alarm():
    alarm_file = 'alarm.wav'
    os.popen('aplay -q ' + alarm_file)

def set_timer(time):
    t = threading.Timer(time, alarm)
    t.start()

output_string = {'1':'after', '2':'at'}
try:
    mode = input('enter mode\n1.alarm after input time\n2.alarm at input time\n')
    if (mode not in ['1', '2']) : raise

    time_input = input('enter time(hour.min.sec)\n')
    time  = time_input.split('.')
    if len(time) != 3 : raise

    print('alarm', output_string[mode], time[0], 'hour', time[1], 'minite and', time[2], 'second')
    if mode == '1':
        set_timer(int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2]))
    else:
        time_alarm = list(localtime())
        for i in range(3):
            time_alarm[i+3] = int(time[i])
        seconds = mktime(tuple(time_alarm)) - mktime(localtime())
        if seconds <= 0 : raise
        set_timer(seconds)
except:
    print('input error.')
