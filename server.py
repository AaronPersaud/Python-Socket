import socket # imported socket module for creating and using sockets
import sys # sys is used to get command line arguments
import signal # imported to handle keyboard interruption

server_address = socket.gethostname() # determine the server's address
n_port = int(sys.argv[1]) # get port number from command line argument
BUFFER_SIZE = 1024 # buffer size
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
print "Socket Created"
s.bind((server_address, n_port)) # bind socket to server's address and n_port
print 'Socket bind complete'
s.listen(5) # listen for a connection
print 'Socket now listening'
conn, addr = s.accept() # accept the connection from client

def string_convert(s): # function that modifies the given message depending on given command 
	if data == "TOUPPERCASE": # if the command was "TOUPPERCASE"
		return s.upper() # make all letters in the string uppercase
	elif data == 'TOLOWERCASE': # if the command was "TOLOWERCASE"
		return s.lower() # make all letters in the string lowercase
	else: # failsafe, shouldn't hit this case
		return "ERROR" # returns "ERROR" to denote something went wrong

def receive_and_send(data): # function that receives the command from the client and receives the message and sends back the modified message
	print "command:", data # prints the command
	conn.send("OK")  # sends back "OK" to the client
	
	newinfo = conn.recv(1024) # receives information for the data connection from the client
	if not data: conn.close() # if there is no data, close the connection (failsafe, shouldn't happen)
	info =  newinfo.split(',') # parse the data into a list with the port and IP address
	newport = info[0] # set newport to the port received from the client
	newip = info[1] # set newip to the client_address
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket
	sock.connect((newip, int(newport))) # connect to client_address and r_port
	
	data2 = sock.recv(BUFFER_SIZE) # receive the message from the client
	print "received message from client:", data2 # print the message
	
	sock.send(string_convert(data2)) # send the modified string to the client
	sock.close() # close the data connection

def signal_handler(signal, frame): # function that's called when Ctrl-C is entered
	s.close() # close the control connection
	print "You have closed the connection. Goodbye!" 
	sys.exit(0) # exit the program

signal.signal(signal.SIGINT, signal_handler) #handler for keyboard interrupt

while 1: # infinite loop to receive continuous commands
	data = conn.recv(1024) # command received
	if not data: # if nothing is received
		conn, addr = s.accept() #break # break out of the loop
	else: # when data is received
		receive_and_send(data) # call function with command received


