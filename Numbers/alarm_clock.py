#!/usr/bin/python3

import threading
import os



def set_timer(time):
    alarm_file = 'alarm.wav'
    def alarm():
        os.popen('aplay -q ' + alarm_file)

    t = threading.Timer(time, alarm)
    t.start()

time_input = input('enter time(min.sec)\n')
try:
    time  = time_input.split('.')
    if time.length() != 2 : raise
    print('alarm after', time[0], 'minite and', time[1], 'second')
    set_timer(int(time[0]) * 60 + int(time[1]))
except:
    print('input error.')


