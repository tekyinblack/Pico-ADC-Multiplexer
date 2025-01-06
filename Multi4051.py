from machine import Pin, ADC
import time

# define addressing pins
S0 = Pin(21, Pin.OUT)
S1 = Pin(20, Pin.OUT)
S2 = Pin(19, Pin.OUT)

#define power pin
Power = Pin(22,Pin.OUT)

# define adc pin to be used 0
multiplex = ADC(Pin(26))

# list of addresses to be used, all in this case, update for actual 4051 pins used
addresses = [[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,0,1],[1,0,1],[0,1,1],[1,1,1]]

Power.value(1)    # Turn on the multiplexer
time.sleep(1)     # wait for power stable

try:
    while True:   # loop through the addresses and print the values
        for address in addresses:
            S0.value(address[0])
            S1.value(address[1])
            S2.value(address[2])
            time.sleep(0.001)
            print(multiplex.read_u16(), end = " ")
        print(" ")
        time.sleep(2)
except:
    Power.value(0)    # turn off the multiplexer
        
    


