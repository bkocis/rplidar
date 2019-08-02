
from adafruit_rplidar import RPLidar 


# Setup the RPLidar 
PORT_NAME = '/dev/ttyUSB0' 
lidar = RPLidar(None, PORT_NAME) 

lidar.stop_motor() 
