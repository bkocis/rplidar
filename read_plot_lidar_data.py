
from adafruit_rplidar import RPLidar 
from math import cos, sin, pi, floor 
import matplotlib.pyplot as plt
import numpy as np


def plot_lidar_rad( x, y):
	ax = plt.subplot(111, projection = 'polar')
	ax = plt.polar( x, y,'ro')
	plt.draw()
	plt.pause( sp )
	plt.clf()


def get_plot_data():
	scan_data = np.zeros((360,2))
	try: 
		print(lidar.info)
		a=0
		c=0
		for scan in lidar.iter_scans(): 
			for (_, angle, distance) in scan:
				if distance < horizon :
					#scan_data[min([359, floor(angle)])] = [ -(floor(angle)-90)*pi/180 , distance ]
					scan_data[ c ] = [ (-1*( min([359, floor(angle)])-85)) *(pi/180) , distance ]
				else:
					scan_data[ c ] = [ (-1*( min([359, floor(angle)])-85)) *(pi/180) , horizon ]
					#scan_data[min([359, floor(angle)])] = distance 
				c += 1
				if c==360:
					c=0
			a +=1
			lidar_dist = scan_data
			print(a)			
			plot_lidar_rad(lidar_dist[:,0], lidar_dist[:,1])
		#	scan_data = np.zeros((360,2))
	 
	 
	except KeyboardInterrupt: 
		print('Stoping.') 

if __name__=='__main__':

	PORT_NAME = '/dev/ttyUSB0' 
	lidar = RPLidar(None, PORT_NAME) 
	lidar.connect() 

	sp =0.45
	horizon = 2000 #14000 #2000 #[mm]
	fig, ax  = plt.subplots(nrows=1,ncols=1, figsize=(5,5))


	get_plot_data()
