#using machine and utime Micropython libraries
import machine
import utime

buzzer = machine.Pin(2,machine.Pin.OUT) #The buzzer is attached to pin D4 on the NodeMCU

motor = machine.PWM(machine.Pin(14), freq = 50) #The motor driver is attached to pin D5 on the NodeMCU

#time parameters defined as empty arrays
first_release_time = []
hours_until_release = []

#This function defines what happens in the event of a pill release
def pill_release():
   motor.duty(200)
   utime.sleep(3.75)
   motor.duty(0)
   buzzer.value(1)
   utime.sleep(2)
   buzzer.value(0)

n = 1 #n is a factor that is used in definint the release_time varible
first_release_time = 10 #defines how long to wait before releasing the first pill
hours_until_release = 10 #defines how often the medication must be taken
number_of_pills = 20
did_first_action = False #an extra condition that corrects for delays in timing

#main loop of the code. A pill is released after user-specified intervals
while True:
   current_time = utime.ticks_ms()
   release_time = first_release_time + hours_until_release*n
   motor.duty(0)
   buzzer.value(0)
   if current_time/1000 >= first_release_time and did_first_action == False:
       pill_release()
       did_first_action = True
       utime.sleep(hours_until_release - 5.75)
   if current_time >= release_time and did_first_action == True:
       pill_release()
       n = n + 1
       utime.sleep(hours_until_release - 5.75)
    if n > (number_of_pills - 1):
        buzzer.value(1)
        utime.sleep(2)
        buzzer.value(0)
        utime.sleep(1)
        buzzer.value(1)
        utime.sleep(2)
        buzzer.value(0)
        utime.sleep(1)
        buzzer.value(1)
        utime.sleep(2)
        buzzer.value(0)
        break





