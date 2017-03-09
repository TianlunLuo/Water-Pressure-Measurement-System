from __future__ import print_function
import GPIO_Detect
import ThingSpeak_Upload
import Save_Data

while True:
    # start to detect the readings
    voltage = GPIO_Detect.GPIO_readIn()
    pressure = GPIO_Detect.voltage_pressure_convert(voltage)
    depth = GPIO_Detect.pressure_depth_convert(pressure)

    voltage = str(round(voltage, 4))
    print("The voltage is: " + voltage + "V")

    pressure = str(round(pressure, 3))
    print("The pressure is: " + pressure + "Bar")

    depth = str(depth)
    print("The depth is: " + depth + "m")

    # start to upload data to the Internet
    ThingSpeak_Upload.connect_to_thingspeak(depth, pressure)

    # save all data to a csv file as a backup
    Save_Data.write_to_csvfile(depth,pressure)
