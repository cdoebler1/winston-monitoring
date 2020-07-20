from mycroft import MycroftSkill
import os
import time


class Winston_monitoring(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def measure_temp(self):
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=", ""))

        while True:
            print(temp())
            self.speak("My current core temperature is {} degress celsius.".format(temp))
            time.sleep(15)


def create_skill():
    return Winston_monitoring()
