# -*- coding: utf-8 -*-
import random


from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

gpio.init()  

from Peripherals import Irda
   
irda = Irda('/dev/input/event2')

from Audio import Mixer
from Audio import Player

m = Mixer()

def Weather():
    rand = random.randint(1, 20)
    Player.speech("%i градусов тепла" % rand)
    Player.play("/root/test.mp4")

irda.add_event(10, [0,1], lambda: gpio.output(port.PA0, irda.event.value) )
irda.add_event(11, [1], lambda: m.volume_up()  )
irda.add_event(14, [1], lambda: m.volume_down()  )
irda.add_event(13, [1], lambda: Player.play("/home/orangepi/sound/alert1.mp3")  )
irda.add_event(64, [1], lambda:  Weather() )
irda.listen()



        
