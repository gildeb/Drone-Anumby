import network
import espnow
from machine import PWM

# motors init
m3 = PWM(3, freq=1000);m3.duty_u16(0)
m4 = PWM(4, freq=1000);m4.duty_u16(0)
m1 = PWM(5, freq=1000);m1.duty_u16(0)
m2 = PWM(6, freq=1000);m2.duty_u16(0)

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()   # Because ESP8266 auto-connects to last Access Point

e = espnow.ESPNow()
e.active(True)

host, msg = e.recv()
e.add_peer(host)
print(host, msg)

while True:
    host, msg = e.recv()
    if msg:             # msg == None if timeout in recv()
        print(msg)
        exec(msg)