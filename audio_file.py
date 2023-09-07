import pyttsx3
class playaudio:
    def __init__(self,voice='female',speakstatus=True):
        self.voice=voice
        self.speakstatus=speakstatus
        self.speakword={
            '1':'one',
            '2':'two',
            '3':'three',
            '4':'four',
            '5':'five',
            '6':'six',
            '7':'seven',
            '8':'eight',
            '9':'nine',
            '+':'plus',
            '-':'minus',
            'x':'multiply',
            '/':'divide',
            '=':'equal to',
            '.':'point',
            '0':'zero',
            'AC':'all clear',
            '<--':'one clear',
            'Bin To Dec':'binary to decimal',
            'Dec To Bin':'decimal to biary'
            }
        self.engine=pyttsx3.init()
        v=self.engine.getProperty('voices')
        self.engine.setProperty('voice',v[1].id)
        
    def speak(self,content):
        if self.speakstatus==True:
            self.engine.say(self.speakword[content])
            self.engine.runAndWait()


























        
        
