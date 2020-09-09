#Statemachine til beskrivelse af livets gang
from gpiozero import LED
from time import sleep

NSred= LED(13)
NSgul=LED(19)
NSgreen=LED(26)
EVred=LED(21)
EVgul=LED(20)
EVgreen=LED(16)


print("Test!")
EVred.on()
sleep(1)
EVgreen.on()
sleep(1)
EVgul.on()
sleep(1)
NSred.on()
sleep(1)
NSgreen.on()
sleep(1)
NSgul.on()
sleep(1)
EVred.off()
EVgreen.off()
EVgul.off()
NSred.off()
NSgreen.off()
NSgul.off()

def redred(x):# Udgangs punkt for lyskrydset
    if x=="NS": #Hvis lyskrydset kommer fra NS skal den gå til EV
        x="EV"
        print("NS RED   EV RED")
        NSred.on()
        EVred.on()
        sleep(2)
        return EV(x)
    elif x=="EV": #Hvis lyskrydset kommer fra EV skal den gå til NS
        x="NS"
        print("NS red   EV red")
        NSred.on()
        EVred.on()
        sleep(2)
        return NS(x)
def NS(x):
    NSred.on()
    NSgul.on()
    EVred.on()
    sleep(2)
    return NS_green(x)

def NS_green(x):
    NSgreen.on()
    EVred.on()
    NSgul.off()
    NSred.off
    sleep(2)
    return NS_gul(x)

def NS_gul(x):
    NSgul.on()
    EVred.on()
    NSgreen.off()
    Sleep(2)
    return redred(x)

def EV(x):
    EVred.on()
    EVgul.on()
    NSred.on()
    sleep(2)
    return EV_green(x)

def EV_green(x):
    EVgreen.on()
    NSred.on()
    EVgul.off()
    EVred.off
    sleep(2)
    return EV_gul(x)

def EV_gul(x):
    EVgul.on()
    NSred.on()
    EVgreen.off()
    Sleep(2)
    return redred(x)


state=redred(x="EV")
while state: state=redred(x="EV")
