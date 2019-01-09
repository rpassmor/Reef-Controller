#!usr/bin/python3
import startStopTimer
import time
##import tempTest

# Welcome Message
print ("Hello and welcome to your Reef Controller!!")
time.sleep(1);

def set_up():

    startStopTimer
##    tempTest.temp()
    time.sleep(5);
            

    
    
# Run user input
try:
    while True:
        
        set_up()
        
except KeyboardInterrupt:
        print("Quit")
        # Reset GPIO Pins
        GPIO.cleanup()




