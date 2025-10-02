from machine import ADC
from time import sleep

adc = ADC(2, atten=ADC.ATTN_11DB)

while True:
    try:
        print("battery : {:4.2f} V".format(2*adc.read_uv()/1e6))
        sleep(1)
    except KeyboardInterrupt:
        break