import RPi.GPIO as GPIO
import time

R = 40

ONESEC = 0.5

DO = 2093
RE = 2349
MI = 2637
FA = 2794
SO = 3136
LA = 3520
XI = 3951
DO1 = 4186
RI1 = 4698

music = [
    [DO,ONESEC],
    [DO,ONESEC],
    [SO,ONESEC],
    [SO,ONESEC],
    [LA,ONESEC],
    [LA,ONESEC],
    [SO,ONESEC*2],

    [FA,ONESEC],
    [FA,ONESEC],
    [MI,ONESEC],
    [MI,ONESEC],
    [RE,ONESEC],
    [RE,ONESEC],
    [DO,ONESEC*2],

    [SO,ONESEC],
    [SO,ONESEC],
    [FA,ONESEC],
    [FA,ONESEC],
    [MI,ONESEC],
    [MI,ONESEC],
    [RE,ONESEC*2],

    [SO,ONESEC],
    [SO,ONESEC],
    [FA,ONESEC],
    [FA,ONESEC],
    [MI,ONESEC],
    [MI,ONESEC],
    [RE,ONESEC*2],
    
    [DO,ONESEC],
    [DO,ONESEC],
    [SO,ONESEC],
    [SO,ONESEC],
    [LA,ONESEC],
    [LA,ONESEC],
    [SO,ONESEC*2],

    [FA,ONESEC],
    [FA,ONESEC],
    [MI,ONESEC],
    [MI,ONESEC],
    [RE,ONESEC],
    [RE,ONESEC],
    [DO,ONESEC*2],
]

def beep(freq, t_ms):
    if freq < 2000 or freq > 5000:
        return

    #range1 = 600000 / freq
    pwm.ChangeFrequency(freq)
    pwm.ChangeDutyCycle(50)
    time.sleep(t_ms)
    print 'freq = ' + str(freq) + ", t_ms = " + str(t_ms)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(R, GPIO.OUT)

#50 is frequency, GPIO.ChangeFrequency(freq): change frequency
pwm = GPIO.PWM(R, 2000)
# start pwm
pwm.start(50)

try:
    print 'len = ', len(music)
    for index in music:
        beep(index[0], index[1])
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
