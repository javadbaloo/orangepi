import time
import alsaaudio
import requests
import shutil
import subprocess


class Mixer:
    def __init__(self):
        self.mixer = alsaaudio.Mixer('Lineout volume control')
    
    def volume(self):
        return int(self.mixer.getvolume()[0])
    
    def volume_up(self):
        vol = self.volume()        
        self.mixer.setvolume( vol + 5 if vol < 95 else 100 )    
    
    def volume_down(self):
        vol = self.volume()     
        self.mixer.setvolume( vol - 5 if vol > 5 else 0 )

class Player:
    @staticmethod
    def play(filename):
        player = subprocess.Popen(["mpg123", filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        player.stdin.write("q")
    @staticmethod
    def speech(text):
        url_base = "https://translate.google.com"
        url = "%s/translate_tts?ie=UTF-8&client=tw-ob&q=%s&tl=ru&total=1&idx=0&textlen=%i" % (url_base, text, len(text) )

        response = requests.get(url, stream=True)
        with open('test.mp4', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)