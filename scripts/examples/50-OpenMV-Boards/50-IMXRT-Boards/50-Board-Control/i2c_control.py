# This work is licensed under the MIT license.
# Copyright (c) 2013-2024 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# I2C Control
#
# This example shows how to use the i2c bus on your OpenMV Cam by dumping the
# contents on a standard EEPROM. To run this example either connect the
# Thermopile Shield to your OpenMV Cam or an I2C EEPROM to your OpenMV Cam.

from machine import I2C

i2c = I2C(1)  # The i2c bus must always be 1.
print(i2c.scan())  # Show attached devices.
mem = i2c.readfrom_mem(0x50, 0, 256)  # The eeprom slave address is 0x50.

print("\n[")
for i in range(16):
    print("\t[", end="")
    for j in range(16):
        print("%03d" % mem[(i * 16) + j], end="")
        if j != 15:
            print(", ", end="")
    print("]," if i != 15 else "]")
print("]")
