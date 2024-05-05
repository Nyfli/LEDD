from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import time # importe dans le code la lib qui permet de gerer le temps

pwm_led = PWM(Pin(17,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_led.freq(1_000) # dont la frequence est de 1000 (default)
pwm_led.duty_u16(0)

while True:
    for i in range(200):
        pwm_led.duty_u16(i*100)
        time.sleep(0.1)
    for i in range(200):
        pwm_led.duty_u16(20000 - i*100)
        time.sleep(0.01)
