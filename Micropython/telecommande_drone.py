import network
import espnow
from machine import Pin, ADC
from time import sleep_ms, ticks_ms
from math import sqrt

#
DroneAddr = b'\xec\xda;\xe3\x0bF' # replace with drone mac address

#
red, green, blue, white, black = (0, 128, 0), (128, 0, 0), (0, 0, 128), (32, 32, 32), (0, 0, 0)

#
def normalize(x, amp=2**14):
    ''' resize x -> [-amp;+amp] '''
    x -= midadc
    if x > dzw:
        x = int(amp*(x-dzw)/szw)
    elif x < -dzw:
        x = int(amp*(x+dzw)/szw)
    else:
        x = 0
    return x

# init ADC
a0 = ADC(0, atten=ADC.ATTN_11DB)
a1 = ADC(1, atten=ADC.ATTN_11DB)
midadc = 1450         # adc middle
maxadc = 2900         # adc max
dzw    = 200          # dead zone width
szw    = midadc - dzw # sensitive zone width

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()      # For ESP8266

# init espnow
e = espnow.ESPNow()
e.active(True)
print("telecommande_drone.py : Network active, Espnow ok")

try:
    e.add_peer(DroneAddr)      # Must add_peer() before send()
except:
    pass
print("telecommande_drone.py : robot added to peers")
#
while True:
    try:
        r, s = a0.read_uv()/1000, a1.read_uv()/1000
        r = normalize(r)     # r in [-2**14,+2**14]
        s = normalize(s)     # s in [-2**14,+2**14]
        speed = int(sqrt(r**2 + s**2))
        if r >= 0:
            if s >=0:
                motor = 1
            else:
                motor = 2
        elif s>= 0:
            motor = 4
        else:
            motor = 3
        cmd = ''
        for n in range(1, 5):
            if n==motor:
                duty = speed
            else:
                duty = 0
            cmd += 'm' + str(n) + '.duty_u16(' + str(duty) + ')\r'
        e.send(DroneAddr, cmd.encode(), False)
        print(cmd.encode())
        sleep_ms(100)
    except:
        break