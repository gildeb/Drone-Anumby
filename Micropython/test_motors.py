from machine import PWM
from time import sleep

m3 = PWM(3, freq=1000);m3.duty_u16(0)
m4 = PWM(4, freq=1000);m4.duty_u16(0)
m1 = PWM(5, freq=1000);m1.duty_u16(0)
m2 = PWM(6, freq=1000);m2.duty_u16(0)

for m in (m3, m4, m1, m2):
    m.duty_u16(2**14)
    sleep(1)
    m.duty_u16(0)
    sleep(1)
