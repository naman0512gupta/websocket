from client import sendSocketMessage
import sys

if len(sys.argv) == 2:
	sendSocketMessage(sys.argv[1])
else:
	print "No Message Input"