#################################################################
# Author: Tianlun Luo                                           #
# This moduel contains SPI interface interaction functions      #
#################################################################

import RPi.GPIO as GPIO

def GPIO_readIn():
    # set up pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(9,GPIO.IN)
    GPIO.setup(8,GPIO.OUT)

    # name pins
    clock = 11
    miso = 9
    cs = 8

    # the array used to save the read in data
    dataList = []

    # read in 8000 data and then
    # calculate the average value
    while len(dataList) != 8000:

        GPIO.output(cs,False)  # bring cs low
        data = str()

        for i in range(15):
            # bring clock low
            GPIO.output(clock, False)
            # read miso pin
            if GPIO.input(miso):
                data += "1"
            else:
                data += "0"
            # bring clock high
            GPIO.output(clock, True)
        # remove the first 3 bits from the data
        data = data.replace(' ','')[3:14]
        # convert the data from binary to decimal
        data = int(data,2)*3.3/2045

        if data != 0:
            dataList.append(data)

        # bring cs high
        GPIO.output(cs, True)

    # start to convert the voltage to
    # pressure and depth
    sum = 0.0

    for voltage in dataList:
        sum = sum + voltage

    # convert voltage to pressure
    if len(dataList) != 0:
        accurateVoltage = sum/len(dataList)
    else:
        accurateVoltage = sum

    return accurateVoltage


def voltage_pressure_convert(accurateVoltage_float):

    voltDiff = (accurateVoltage_float-0.8749)/0.011 #0.011
    pressure = voltDiff*0.084 #0.0689

    return pressure

def pressure_depth_convert(pressure_float):
    # convert pressure to depth
    # 1 bar = 10 meter water
    depth = round(pressure_float,3)*10

    return depth
