from mycroft import MycroftSkill, intent_file_handler
import subprocess


class Winston(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('winston.about.intent')
    def winston_about(self, message):
        self.speak_dialog('winston.about')

    @intent_file_handler('winston.temp.intent')
    def winston_temp(self, message):
        self.speak_dialog('winston.temp')
        temp = subprocess.Popen(['/opt/vc/bin/vcgencmd', 'measure_temp'],
                                stdout=subprocess.PIPE)
        temp = temp.communicate()[0].decode('ascii')[5:-3]
        self.speak("My current core temperature is {} degrees celsius."
                   .format(temp))

    @intent_file_handler('winston.uptime.intent')
    def winston_uptime(self, message):
        uptime = subprocess.Popen(['uptime', '-p'], stdout=subprocess.PIPE)
        uptime = uptime.communicate()[0].decode('ascii')[:-1]
        self.speak("I have been {}".format(uptime))

    @intent_file_handler('winston.sexy.intent')
    def winston_sexy(self, message):
        self.speak_dialog('winston.sexy')

    def stop(self):
        pass


def create_skill():
    return Winston()
