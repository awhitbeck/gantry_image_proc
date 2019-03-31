import zmq
import numpy as np

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

x_start=-100
x_stop=100
x_stride=10
y_start=-100
y_stop=100
y_stride=10

for x in np.arange(x_start,x_stop,x_stride):
	for y in np.arange(y_start,y_stop,y_stride):
	    socket.send(b"G0 X{0} Y{1} Z50 F50".format(x,y))
	    message = socket.recv()
	    print("Received reply [ %s ]" % (message))