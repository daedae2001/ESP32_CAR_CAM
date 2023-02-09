# Import necessary libraries
import machine
import time

# Define the pins for the two motors
motor1_pin1 = machine.Pin(5, machine.Pin.OUT)
motor1_pin2 = machine.Pin(18, machine.Pin.OUT)
motor2_pin1 = machine.Pin(19, machine.Pin.OUT)
motor2_pin2 = machine.Pin(21, machine.Pin.OUT)

# Function to control the motor movements


def motor_control(motor1_pin1, motor1_pin2, motor2_pin1, motor2_pin2, direction):
    if direction == "forward":
        motor1_pin1.value(1)
        motor1_pin2.value(0)
        motor2_pin1.value(1)
        motor2_pin2.value(0)
    elif direction == "backward":
        motor1_pin1.value(0)
        motor1_pin2.value(1)
        motor2_pin1.value(0)
        motor2_pin2.value(1)
    elif direction == "left":
        motor1_pin1.value(0)
        motor1_pin2.value(1)
        motor2_pin1.value(1)
        motor2_pin2.value(0)
    elif direction == "right":
        motor1_pin1.value(1)
        motor1_pin2.value(0)
        motor2_pin1.value(0)
        motor2_pin2.value(1)
    else:
        motor1_pin1.value(0)
        motor1_pin2.value(0)
        motor2_pin1.value(0)
        motor2_pin2.value(0)


# Control the car's movement
motor_control(motor1_pin1, motor1_pin2, motor2_pin1, motor2_pin2, "forward")
time.sleep(2)
motor_control(motor1_pin1, motor1_pin2, motor2_pin1, motor2_pin2, "left")
time.sleep(2)
motor_control(motor1_pin1, motor1_pin2, motor2_pin1, motor2_pin2, "right")
time.sleep(2)
motor_control(motor1_pin1, motor1_pin2, motor2_pin1, motor2_pin2, "backward")
time.sleep(2)
motor_control(motor1_pin1, motor1_pin2, motor2_pin1, motor2_pin2, "stop")
