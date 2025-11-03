from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon, Side, Port
from pybricks.tools import wait
import arm, missions, timer, display, drive, battery, usys

hub = PrimeHub()
timer = timer.timer()
arm = arm.arm(Port.F, Port.D)
drive = drive.drive(Port.A, Port.B)
battery = battery.battery()

motionList = [
    pass, # Fill in with across code, do demo next meeting
    pass,
]

letterList = [
    "L",
    "R",
]

def menu():
    index = 0
    displayOn = False
    menuList = letterList
    menuList.extend(range(1, len(motionList)-len(letterList)+1))
    print("Generated list:", menuList)
    while not battery.charging():
        pressed = hub.buttons.pressed()
        if pressed:
            if Button.LEFT in pressed:
                hub.speaker.beep() 
                index = index - 1
                index = Math.constrain(index, 0, 100)
                display.number(menuList[index])
            if Button.RIGHT in pressed:
                hub.speaker.beep()
                index = index + 1
                index = Math.constrain(index, 0, len(menuList)-1)
                display.number(menuList[index])
            if Button.CENTER in pressed:
                hub.speaker.beep()
                print("Running:" + str(menuList[index]))
                display.number(menuList[index])
                timer.startMission()
                motionList[index]()
                drive.stop()
                arm.disable()
                print("Mission time:", str(Timer.mTime()*1000) + ", Total time:", str(Timer.time() * 1000))
                voltage = battery.voltage()
                print("Battery voltage:", str(voltage) + " mv, Battery percentage:", str(battery.percentage()))
        else:
            displayOn = display.number(menuList[index], displayOn)
        wait(100)
