"""
The constants contained in this module are from the Reachy Mini
hardware specification (https://huggingface.co/docs/reachy_mini/en/platforms/reachy_mini/hardware)

They should be evaluated against the robot and the sim to ensure they are correct and the
clamping behavior is at the expecting values.
"""

from math import pi

# X, Y, Z are all expressed milimeter (mm) units
X_MIN = -15
X_MAX = 25

Y_MIN = -40
Y_MAX = 40

Z_MIN = -40
Z_MAX = 25

# PITCH, ROLL, YAW in degrees
# Using the `create_head_pose` util from ReachyMini SDK you can set the `degrees` flag to
# True alloing you to use degree values. Added both degree and radian min, max pairs
PITCH_MIN = -40
PITCH_MAX = 40

ROLL_MIN = -40
ROLL_MAX = 40

YAW_MIN = -60
YAW_MAX = 60

PITCH_RADIANS_MIN = -0.6981317
PITCH_RADIANS_MAX = 0.6981317

ROLL_RADIANS_MIN = -0.6981317
ROLL_RADIANS_MAX = 0.6981317

YAW_RADIANS_MIN = -1.047198
YAW_RADIANS_MAX = 1.047198


BODY_YAW_MIN = -2.70526
BODY_YAW_MAX = 2.70526

# ANTENNA ranges are in radians
ANTENNA_MIN = -pi
ANTENNA_MAX = pi