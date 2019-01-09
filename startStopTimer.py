#!usr/bin/python3

#import stuff
##import os
##import glob
import RPi.GPIO as GPIO
import time
from datetime import datetime
import json
##import tempTest
##
##
### init list pin numbers

GPIO.setmode(GPIO.BCM)

pinList = [18, 23, 24, 25, 12, 16, 20, 21]

# loop pins and the sleep time

for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)
GPIO.setup(17, GPIO.IN)

sleepTime = 1
ato_counter = 0
ato_max = 120



#datetime.strptime(input("End Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")

def reset_times():
        ssTimes = {
            "startTimes": {
                    "start1": '00:00:00',
                    "start2": '00:00:00',
                    "start3": '00:00:00',
                    "start4": '00:00:00',
                    "start5": '00:00:00',
                    "start6": '00:00:00',
                    "start7": '00:00:00',
                    "start8": '00:00:00'
                    },
            "endTimes": {
                    "end1": '23:59:59',
                    "end2": '23:59:59',
                    "end3": '23:59:59',
                    "end4": '23:59:59',
                    "end5": '23:59:59',
                    "end6": '23:59:59',
                    "end7": '23:59:59',
                    "end8": '23:59:59'
                    }
            }
        with open("times.txt","w") as f:
            s=json.dumps(ssTimes, f, ensure_ascii=False)
            f.write(s)
        with open("times.txt","r") as f:
            s=f.read()
            ssTimes=json.loads(s)
    
f=open("times.txt","r")
s=f.read()
ssTimes=json.loads(s)

start1 = datetime.strptime(ssTimes["startTimes"]["start1"],"%H:%M:%S").strftime("%H:%M:%S")
end1 = datetime.strptime(ssTimes["endTimes"]["end1"],"%H:%M:%S").strftime("%H:%M:%S")
start2 = datetime.strptime(ssTimes["startTimes"]["start2"],"%H:%M:%S").strftime("%H:%M:%S")
end2 = datetime.strptime(ssTimes["endTimes"]["end2"],"%H:%M:%S").strftime("%H:%M:%S")
start3 = datetime.strptime(ssTimes["startTimes"]["start3"],"%H:%M:%S").strftime("%H:%M:%S")
end3 = datetime.strptime(ssTimes["endTimes"]["end3"],"%H:%M:%S").strftime("%H:%M:%S")
start4 = datetime.strptime(ssTimes["startTimes"]["start4"],"%H:%M:%S").strftime("%H:%M:%S")
end4 = datetime.strptime(ssTimes["endTimes"]["end4"],"%H:%M:%S").strftime("%H:%M:%S")
start5 = datetime.strptime(ssTimes["startTimes"]["start5"],"%H:%M:%S").strftime("%H:%M:%S")
end5 = datetime.strptime(ssTimes["endTimes"]["end5"],"%H:%M:%S").strftime("%H:%M:%S")
start6 = datetime.strptime(ssTimes["startTimes"]["start6"],"%H:%M:%S").strftime("%H:%M:%S")
end6 = datetime.strptime(ssTimes["endTimes"]["end6"],"%H:%M:%S").strftime("%H:%M:%S")
start7 = datetime.strptime(ssTimes["startTimes"]["start7"],"%H:%M:%S").strftime("%H:%M:%S")
end7 = datetime.strptime(ssTimes["endTimes"]["end7"],"%H:%M:%S").strftime("%H:%M:%S")
start8 = datetime.strptime(ssTimes["startTimes"]["start8"],"%H:%M:%S").strftime("%H:%M:%S")
end8 = datetime.strptime(ssTimes["endTimes"]["end8"],"%H:%M:%S").strftime("%H:%M:%S")
f.close()



# Set up a another outlet

def another_outlet():
    set_another = input("would you like to set up another start stop timer? y/n: ").lower()
    if set_another == "y":
        outlet_number()
    if set_another == "n":
        main_loop()
    else:
        print ("Sorry, that is not a valid outlet, please try again")
        another_outlet()


# Input outlet number
def outlet_number():
    outlet = input("Which outlet(number) would you like to use, please choose from the list:\n\
one-eight, reset to reset times or run to skip to run\n\
").lower()
    if outlet == "one":
        outlet1_start()
        outlet1_stop()
    elif outlet == "two":
        outlet2_start()
        outlet2_stop()
    elif outlet == "three":
        outlet3_start()
        outlet3_stop()
    elif outlet == "four":
        outlet4_start()
        outlet4_stop()
    elif outlet == "five":
        outlet5_start()
        outlet5_stop()
    elif outlet == "six":
        outlet6_start()
        outlet6_stop()
    elif outlet == "seven":
        outlet7_start()
        outlet7_stop()
    elif outlet == "eight":
        outlet8_start()
        outlet8_stop()
    elif outlet == "reset":
        reset_times()
        outlet_number()
    elif outlet == "run":
        main_loop()
    else:
        print ("Idiot!! Pick a valid outlet!")
        outlet_number()

        

def outlet1_start():
    global start1
    global ssTimes
    try:
        ssTimes["startTimes"]["start1"] = datetime.strptime(input("Start Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                start1 = datetime.strptime(ssTimes["startTimes"]["start1"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet1_start()
def outlet1_stop():
    global end1
    global ssTimes
    try:
        ssTimes["endTimes"]["end1"] = datetime.strptime(input("End Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                end1 = datetime.strptime(ssTimes["endTimes"]["end1"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet1_stop()
    if start1 > end1:
        print ("I'm sorry, your end time is before your start time, please input a new start time")
        outlet1_start()
    else:
        another_outlet()   
def outlet2_start():
    global start2
    global ssTimes
    try:
        ssTimes["startTimes"]["start2"] = datetime.strptime(input("Start Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                start2 = datetime.strptime(ssTimes["startTimes"]["start2"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet2_start()
def outlet2_stop():
    global end2
    global ssTimes
    try:
        ssTimes["endTimes"]["end2"] = datetime.strptime(input("End Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                end2 = datetime.strptime(ssTimes["endTimes"]["end2"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet2_stop()
    if start2 > end2:
        print ("I'm sorry, your end time is before your start time, please input a new start time")
        outlet1_start()
    else:
        another_outlet() 
def outlet3_start():
    global start3
    global ssTimes
    try:
        ssTimes["startTimes"]["start3"] = datetime.strptime(input("Start Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                start3 = datetime.strptime(ssTimes["startTimes"]["start3"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet3_start()
def outlet3_stop():
    global end3
    global ssTimes
    try:
        ssTimes["endTimes"]["end3"] = datetime.strptime(input("End Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                end3 = datetime.strptime(ssTimes["endTimes"]["end3"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet3_stop()
    if start3 > end3:
        print ("I'm sorry, your end time is before your start time, please input a new start time")
        outlet1_start()
    else:
        another_outlet() 
def outlet4_start():
    global start4
    global ssTimes
    try:
        ssTimes["startTimes"]["start4"] = datetime.strptime(input("Start Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                start4 = datetime.strptime(ssTimes["startTimes"]["start4"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet4_start()
def outlet4_stop():
    global end4
    global ssTimes
    try:
        ssTimes["endTimes"]["end4"] = datetime.strptime(input("End Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                end4 = datetime.strptime(ssTimes["endTimes"]["end4"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet4_stop()
    if start4 > end4:
        print ("I'm sorry, your end time is before your start time, please input a new start time")
        outlet1_start()
    else:
        another_outlet() 
def outlet5_start():
    global start5
    global ssTimes
    try:
        ssTimes["startTimes"]["start5"] = datetime.strptime(input("Start Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                start5 = datetime.strptime(ssTimes["startTimes"]["start5"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet5_start()
def outlet5_stop():
    global end5
    global ssTimes
    try:
        ssTimes["endTimes"]["end5"] = datetime.strptime(input("End Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                end5 = datetime.strptime(ssTimes["endTimes"]["end5"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet6_stop()
    if start5 > end5:
        print ("I'm sorry, your end time is before your start time, please input a new start time")
        outlet1_start()
    else:
        another_outlet() 
def outlet6_start():
    global start6
    global ssTimes
    try:
        ssTimes["startTimes"]["start6"] = datetime.strptime(input("Start Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                start6 = datetime.strptime(ssTimes["startTimes"]["start6"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet6_start()
def outlet6_stop():
    global end6
    global ssTimes
    try:
        ssTimes["endTimes"]["end6"] = datetime.strptime(input("End Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                end6 = datetime.strptime(ssTimes["endTimes"]["end6"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet6_stop()
    if start6 > end6:
        print ("I'm sorry, your end time is before your start time, please input a new start time")
        outlet1_start()
    else:
        another_outlet() 
def outlet7_start():
    global start7
    global ssTimes
    try:
        ssTimes["startTimes"]["start7"] = datetime.strptime(input("Start Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                start7 = datetime.strptime(ssTimes["startTimes"]["start7"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet7_start()
def outlet7_stop():
    global end7
    global ssTimes
    try:
        ssTimes["endTimes"]["end7"] = datetime.strptime(input("End Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                end7 = datetime.strptime(ssTimes["endTimes"]["end7"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet7_stop()
    if start7 > end7:
        print ("I'm sorry, your end time is before your start time, please input a new start time")
        outlet1_start()
    else:
        another_outlet()
def outlet8_start():
    global start8
    global ssTimes
    try:
        ssTimes["startTimes"]["start8"] = datetime.strptime(input("Start Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                start8 = datetime.strptime(ssTimes["startTimes"]["start8"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet8_start()
def outlet8_stop():
    global end8
    global ssTimes
    try:
        ssTimes["endTimes"]["end8"] = datetime.strptime(input("End Time HH:MM:SS format: "),"%H:%M:%S").strftime("%H:%M:%S")
        with open("times.txt","w") as f:
                s=json.dumps(ssTimes, f, ensure_ascii=False)
                f.write(s)
        with open("times.txt","r") as f:
                s=f.read()
                ssTimes=json.loads(s)
                end8 = datetime.strptime(ssTimes["endTimes"]["end8"],"%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print ("Not in valid date format, please try again ")
        outlet8_stop()
    if start8 > end8:
        print ("I'm sorry, your end time is before your start time, please input a new start time")
        outlet1_start()
    else:
        another_outlet()



# Main Loop
try:

    def main_loop():
        global ato_counter
        global ato_max
        #hour is equal to the current time in %H:%M:%S format
        hour = time.strftime("%T")
        def time_in_range(start,end,x):
            if start <= end:
                return start <= x <= end
            else:
                return start <= x or x <= end
        
        input_state = GPIO.input(17)

        while hour <= "23:59:59":
            print (time.strftime("%T"))
            if time_in_range(start1,end1,time.strftime("%T")):
                print ("Pin One is ON")
                #print (start1)
                #print (end1)
                GPIO.output(18, GPIO.LOW)
            else:
                print ("Pin one is OFF")
                #print (start1)
                #print (end1)
                GPIO.output(18, GPIO.HIGH)
            if time_in_range(start2,end2,time.strftime("%T")):
                print ("Pin two is ON")
                #print (start2)
                #print (end2)
                GPIO.output(23, GPIO.LOW)
            else:
                print ("Pin two is OFF")
                #print (start2)
                #print (end2)
                GPIO.output(23, GPIO.HIGH)
            if time_in_range(start3,end3,time.strftime("%T")):
                print ("Pin three is ON")
                #print (start3)
                #print (end3)
                GPIO.output(24, GPIO.LOW)
            else:
                print ("Pin three is OFF")
                #print (start3)
                #print (end3)
                GPIO.output(24, GPIO.HIGH)
            if time_in_range(start4,end4,time.strftime("%T")):
                print ("Pin four is ON")
                #print (start4)
                #print (end4)
                GPIO.output(25, GPIO.LOW)
            else:
                print ("Pin four is OFF")
                #print (start4)
                #print (end4)
                GPIO.output(25, GPIO.HIGH)
            if time_in_range(start5,end5,time.strftime("%T")):
                print ("Pin five is ON")
                #print (start5)
                #print (end5)
                GPIO.output(12, GPIO.LOW)
            else:
                print ("Pin five is OFF")
                #print (start5)
                #print (end5)
                GPIO.output(12, GPIO.HIGH)
            if time_in_range(start6,end6,time.strftime("%T")):
                print ("Pin six is ON")
                #print (start6)
                #print (end6)
                GPIO.output(16, GPIO.LOW)
            else:
                print ("Pin six is OFF")
                #print (start6)
                #print (end6)
                GPIO.output(16, GPIO.HIGH)
            if time_in_range(start7,end7,time.strftime("%T")):
                print ("Pin seven is ON")
                #print (start7)
                #print (end7)
                GPIO.output(20, GPIO.LOW)
            else:
                print ("Pin seven is OFF")
                #print (start7)
                #print (end7)
                GPIO.output(20, GPIO.HIGH)
            if time_in_range(start8,end8,time.strftime("%T")) & input_state == False & ato_counter < ato_max & ato_counter >= 0:
                print ("Pin eight is ON")
                #print (start8)
                #print (end8)
                print (ato_counter)
                print (ato_max)
                ato_counter += 1
                GPIO.output(21, GPIO.LOW)
            elif ato_counter > ato_max & input_state == False:
                ato_counter = -120
                print (ato_counter)
                GPIO.output(21, GPIO.HIGH)
            elif ato_counter < 0 & input_state == False or input_state == True:
                ato_counter += 1
                print (ato_counter)
                print ("counting")
                GPIO.output(21, GPIO.HIGH)
            else:
                print ("Pin eight is OFF")
                #print (start8)
                #print (end8)
                print (ato_counter)
                #print (input_state)
                ato_counter = 0
                GPIO.output(21, GPIO.HIGH)
            break
        

# End program cleanly

except KeyboardInterrupt:
    print ("Quit")
# Reset GPIO Pins
    GPIO.cleanup()

outlet_number()
try:
        while True:
            main_loop()
            time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()

