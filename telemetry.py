import serial
import time

# Start and setup telemetry
def setup(_serial_port, _serial_baud_rate):
	global board
	board = serial.Serial(_serial_port, _serial_baud_rate, timeout=1)
	time.sleep(1.8) # Wait for connection

# Close telemetry
def end():
	board.close()

def read():
	return board.read()

class robot(object):
	"""declare a new robot"""
	def __init__(self, address):
		self.address = address
	def sendtoMotor(self, speed1, speed2):
		if speed1 >  1: speed1 =  1
		if speed1 < -1: speed1 = -1
		if speed2 >  1: speed2 =  1
		if speed2 < -1: speed2 = -1

		speed1 = str(int(speed1*255)).zfill(4)
		speed2 = str(int(speed2*255)).zfill(4)

		text_to_send = "?" + self.address + "," + speed1 + "," + speed2 + "!"
		board.write(text_to_send)

	def stop(self):
		self.sendtoMotor(0,0)