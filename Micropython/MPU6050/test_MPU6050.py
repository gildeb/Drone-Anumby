from machine import Pin, I2C
from MPU6050dmp20 import *

def dataReadyInt(p):
    global new_data

    if mpu.getFIFOCount() != 42:
        mpu.resetFIFO()
        new_data = False
        return
    buf = mpu.getFIFOBytes(42)
    q = mpu.dmpGetQuaternion(buf)
    gx, gy, gz = mpu.dmpGetGravity(q)
#     mpu.yaw = atan2(2*qx*qy - 2*qw*qz, 2*qw**2 - 2*qx**2 - 1)*57.3
    try:
        mpu.pitch = atan(gx / (gy**2 + gz**2))*57.3
        mpu.roll = atan(gy / (gx**2 + gz**2))*57.3
    except:
        pass
    mpu.omy = unpack('>h', buf[20:22])[0]
    mpu.omz = unpack('>h', buf[24:26])[0]
    new_data = True

i2c = I2C(scl=10, sda=11, freq=400_000)
mpu = MPU6050dmp(i2c, axOff=2058, ayOff=-2414, azOff=1349, gxOff=31, gyOff=-23, gzOff=30)
# mpu.calibrate()
intPin = Pin(12, Pin.IN)
mpu.dmpInitialize()
mpu.setDMPEnabled(True)
mpu.getIntStatus()
mpu.resetFIFO()
intPin.irq(dataReadyInt, Pin.IRQ_FALLING)

from time import sleep_ms
sleep_ms(1000)

while True:
    try:
        print('pitch:{:5.1f}°  roll:{:5.1f}°'.format(mpu.pitch, mpu.roll))
        sleep_ms(300)
    except KeyboardInterrupt:
        break