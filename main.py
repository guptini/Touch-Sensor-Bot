#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
left_touch = TouchSensor(Port.S1)
right_touch = TouchSensor(Port.S4)
robot = DriveBase(left_motor, right_motor, wheel_diameter = 45, axle_track = 100)

# Write your program here.
while True:
    if right_touch.pressed() and left_touch.pressed() == True:
        robot.drive(-1000, 0)
    elif left_touch.pressed() == True:
        robot.drive(-100, 100)
    elif right_touch.pressed() == True:
        robot.drive(-100, -100)
    else:
        robot.stop()
