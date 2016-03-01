# -*- coding: utf-8 -*-
import uuid
import pymongo
from pymongo import Connection
from Peripherals import Camera

c = Camera("/dev/v4l/by-id/usb-PixArt_Imaging_Inc._FaceCam_311-video-index0")
connection = Connection()

def motion_prevent(event):
    filename = "/home/orangepi/camera/" + str(uuid.uuid4())  + ".jpg"
    c.capture(filename)
    
    event['image'] = filename
    print event
    
    connection.stage.events.insert( event )
    


from Sensors import Motion
from pyA20.gpio import port


m = Motion(port.PA1, 10)
m.add_event(1, motion_prevent )
m.wait_event()