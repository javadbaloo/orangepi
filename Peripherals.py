from evdev import InputDevice
from select import select
from types import *

import pygame
import pygame.camera



class Camera:
    def __init__(self, device):
        pygame.camera.init()
        self.camera = pygame.camera.Camera(device,(640,480))
    def capture(self, filename):
        self.camera.start()
        img = self.camera.get_image()
        pygame.image.save(img,filename)
        self.camera.stop()
    def quit(self):
        pygame.quit()


        
class Irda: 
    def __init__(self, device):
        self.events = {}
        self.device = InputDevice(device)
    
    def add_event(self, event, values, handler):
        self.events[event] = [handler, values]

    def event(self):
        return self.event
    
    def listen(self):        
        while True:
            r,w,x = select([self.device], [], [])
            for event in self.device.read():
                self.event = event
                try:
                    handler, v = self.events[event.code]                    
                    for x in v:
                        if event.value == x:
                            handler()
                            
                except KeyError:
                    print event
                    pass