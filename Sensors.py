from time import gmtime, strftime, sleep, localtime, time

from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector 

class Motion:
    def __init__(self, port, timeout):
        self.port = port
        self.timeout = timeout
        self.timers = {'last' : 0}
        self.events = {}
        
        gpio.init() 
        gpio.setcfg(port, gpio.INPUT) #Configure PE11 as input
        gpio.setcfg(port, 0) #Same as above
    
    def add_event(self, data, handler):
        self.events[data] = handler
    
    def wait_event(self):
        
        while True:
            state = gpio.input(self.port)
            if state == 1:
                if 'last' in self.timers:
                    if (time() - self.timers['last']) > self.timeout:
                    
                        self.timers['last'] = time()
                        
                        event = { 
                            'date': strftime("%Y-%m-%d %H:%M:%S", gmtime()),    
                            'name':'motion',    
                            'level':3
                        }
                        
                        self.events[state](event)

                    else:
                        pass
                else:
                    self.timers['last'] = time()
                    

   

