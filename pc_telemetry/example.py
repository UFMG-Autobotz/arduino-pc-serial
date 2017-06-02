import telemetry

# Start and setup telemetry
# telemetry.setup(SERIAL PORT, BAUD RATE)
telemetry.setup('/dev/ttyACM0', 115200)

'''
'''

# Declare new robots
# telemetry.robot("robot_address")
robotA = telemetry.robot("A1")
robotB = telemetry.robot("B1")

# Send speed to motors: left, right
# Speed range between -1:1
robotA.sendtoMotor(-0.783,0.295)

# Stop robot
robotA.stop()

'''
'''

# Directly send without sendtoMotor() protocol
telemetry.write("Hello World!")

'''
'''

# Close communication channel
# Shall be used in the end of the code to finish communication
telemetry.end()
