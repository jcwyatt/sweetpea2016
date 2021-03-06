import time
import picamera
from datetime import datetime, timedelta

def wait():
    # Calculate the delay to the start of the next hour
    next_hour = (datetime.now() + timedelta(hours=1)).replace(
        minute=0, second=0, microsecond=0)   #in the original code online, hours=1 was hour=1 and caused an error.
    delay = (next_hour - datetime.now()).seconds
    time.sleep(delay)

with picamera.PiCamera() as camera:
    camera.start_preview()
    wait()
    for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
        print('Captured %s' % filename)
        wait()
