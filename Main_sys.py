import serial, time
import RPi.GPIO as GPIO
from gpiozero import AngularServo
from time import sleep

# Open Serial
ser = serial.Serial(
    port="/dev/ttyS0",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)
print(ser.name)  # check which port was really used

# Parameter for stepper motor
PUL = 17  # GPIO 17
DIR = 27  # GPIO 27
ENA = 22  # GPIO 22

# Setup-Board and GPIO
GPIO.setmode(GPIO.BCM)
# Stepper motor
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
print("PUL = GPIO 17 - RPi 4B-Pin #11")
print("DIR = GPIO 27 - RPi 4B-Pin #13")
print("ENA = GPIO 22 - RPi 4B-Pin #15")

print("Initialization Completed")
# Could have usesd only one DURATION constant but chose two. This gives play options.
durationFwd = (
    5000  # This is the duration of the motor spinning. used for forward direction
)
durationBwd = (
    5000  # This is the duration of the motor spinning. used for reverse direction
)
print("Duration Fwd set to " + str(durationFwd))
print("Duration Bwd set to " + str(durationBwd))

delay = 0.0000001  # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
print("Speed set to " + str(delay))

cycles = 1000  # This is the number of cycles to be run once program is started.
cyclecount = 0  # This is the iteration of cycles to be run once program is started.
print("number of Cycles to Run set to " + str(cycles))


# Forward-function for stepper motor
def forward():
    GPIO.output(ENA, GPIO.HIGH)
    # GPIO.output(ENAI, GPIO.HIGH)
    print("ENA set to HIGH - Controller Enabled")
    #
    # sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.LOW)
    # GPIO.output(DIRI, GPIO.LOW)
    print("DIR set to LOW - Moving Forward at " + str(delay))
    print("Controller PUL being driven.")
    for x in range(durationFwd):
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    GPIO.output(ENA, GPIO.LOW)
    # GPIO.output(ENAI, GPIO.LOW)
    print("ENA set to LOW - Controller Disabled")
    # sleep(.5) # pause for possible change direction
    return


# Reverse-function for stepper motor
def reverse():
    GPIO.output(ENA, GPIO.HIGH)
    # GPIO.output(ENAI, GPIO.HIGH)
    print("ENA set to HIGH - Controller Enabled")
    #
    # sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.HIGH)
    # GPIO.output(DIRI, GPIO.HIGH)
    print("DIR set to HIGH - Moving Backward at " + str(delay))
    print("Controller PUL being driven.")
    #
    for y in range(durationBwd):
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    GPIO.output(ENA, GPIO.LOW)
    # GPIO.output(ENAI, GPIO.LOW)
    print("ENA set to LOW - Controller Disabled")
    # sleep(.5) # pause for possible change direction
    return


def check_state():
    code = str(received_data)
    print("RECEIVED Serial")
    print("code is {}".format(code), type(code))

    a = code[2]
    b = code[3]
    c = code[4]
    d = code[5]
    e = code[6]
    f = code[7]
    g = code[8]
    h = code[9]

    # Check Machine
    if a == "0" and b == "0" and c == "1":
        print("Machine 001 Start!")

    # Check CH
    global CH
    global SM  # SM is GPIO each Servo Motor
    if d == "0" and e == "1":
        CH = 1
        SM = 26
        print("CH 01")
    elif d == "0" and e == "2":
        CH = 2
        SM = 19
        print("CH 02")
    elif d == "0" and e == "3":
        CH = 3
        SM = 13
        print("CH 03")
    elif d == "0" and e == "4":
        CH = 4
        SM = 6
        print("CH 04")
    elif d == "0" and e == "5":
        CH = 5
        SM = 21
        print("CH 05")
    elif d == "0" and e == "6":
        CH = 6
        SM = 20
        print("CH 06")
    elif d == "0" and e == "7":
        CH = 7
        SM = 16
        print("CH 07")
    elif d == "0" and e == "8":
        CH = 8
        SM = 12
        print("CH 08")
    elif d == "0" and e == "9":
        CH = 9
        SM = 5
        print("CH 09")
    elif d == "1" and e == "0":
        CH = 10
        SM = 11
        print("CH 10")
    elif d == "1" and e == "1":
        CH = 11
        SM = 9
        print("CH 11")
    elif d == "1" and e == "2":
        CH = 12
        SM = 4
        print("CH 12")
    elif d == "1" and e == "3":
        CH = 13
        SM = 7
        print("CH 13")
    elif d == "1" and e == "4":
        CH = 14
        SM = 8
        print("CH 14")
    elif d == "1" and e == "5":
        CH = 15
        SM = 25
        print("CH 15")
    elif d == "1" and e == "6":
        CH = 16
        SM = 24
        print("CH 16")

    # Check QTY
    global qty
    if f == "0" and g == "1":
        qty = 1
        print("QTY 01")
    elif f == "0" and g == "2":
        qty = 2
        print("QTY 02")
    elif f == "0" and g == "3":
        qty = 3
        print("QTY 03")
    elif f == "0" and g == "4":
        qty = 4
        print("QTY 04")
    elif f == "0" and g == "5":
        qty = 5
        print("QTY 05")
    elif f == "0" and g == "6":
        qty = 6
        print("QTY 06")
    elif f == "0" and g == "7":
        qty = 7
        print("QTY 07")
    elif f == "0" and g == "8":
        qty = 8
        print("QTY 08")
    elif f == "0" and g == "9":
        qty = 9
        print("QTY 09")
    elif f == "1" and g == "0":
        qty = 10
        print("QTY 10")


def run_machine():
    print("CH = {} and QTY = {}".format(CH, qty))  # For check parameter CH and qty

    ### Check CH for drive Stepping Motor
    # DRIVE UP!!!
    # For CH 1-4
    if CH == 1 or CH == 2 or CH == 3 or CH == 4:
        print("Stepping Motor Drive 3 Rounds!")
        for i in range(3):
            reverse()
    # For CH 5-8
    elif CH == 5 or CH == 6 or CH == 7 or CH == 8:
        print("Stepping Motor Drive 2 Round!")
        for i in range(2):
            reverse()
    # For CH 9-12
    elif CH == 9 or CH == 10 or CH == 11 or CH == 12:
        print("Stepping Motor Drive 1 Rounds!")
        for i in range(1):
            reverse()
    # For CH 13-16
    elif CH == 13 or CH == 14 or CH == 15 or CH == 16:
        print("Stepping Motor not RUN!")

    ### Check QTY for drive Servo Motor
    # Servo Motor 1-16
    servo = AngularServo(SM, min_angle=-180, max_angle=180)
    amount = qty
    amount = (int(amount) * 3) + 1
    print(amount)  # For Check Round of Servo Motor
    servo.angle = -180
    sleep(1.1 * float(amount))
    servo.angle = 0
    # sleep(1.1*float(amount))

    ### Check CH for drive Stepping Motor
    # DRIVE DOWN!!!
    # For CH 1-4
    if CH == 1 or CH == 2 or CH == 3 or CH == 4:
        print("Stepping Motor Drive 3 Rounds!")
        for i in range(3):
            forward()
    # For CH 5-8
    elif CH == 5 or CH == 6 or CH == 7 or CH == 8:
        print("Stepping Motor Drive 2 Round!")
        for i in range(2):
            forward()
    # For CH 9-12
    elif CH == 9 or CH == 10 or CH == 11 or CH == 12:
        print("Stepping Motor Drive 1 Rounds!")
        for i in range(1):
            forward()
    # For CH 13-16
    elif CH == 13 or CH == 14 or CH == 15 or CH == 16:
        print("Stepping Motor not RUN!")


while True:
    received_data = ser.read()
    time.sleep(0.03)
    data_left = ser.inWaiting()
    received_data += ser.read(data_left)
    # print(received_data) # for check serial code

    # Main system
    check_state()
    run_machine()
