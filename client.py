import socket # imported socket module for creating and using sockets
import sys # sys is used to get command line arguments
 
server_address = sys.argv[1] # first command line argument
n_port = int(sys.argv[2]) # second command line argument
BUFFER_SIZE = 1024 # buffer size

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
s.connect((server_address, n_port)) # connect to IP == server_address and port == n_port

def send_and_receive(command): # function that sends command to server, sends message to server, and receives modified message from server
	s.send(command) # send command to server
	
	data = s.recv(BUFFER_SIZE) # receives message from server (should be "OK")
	print "received data from server:", data # print data received
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create another socket (data connection)
	client_address = socket.gethostname() # determine the client's address
	sock.bind((client_address, 0)) # bind socket to the client_address and any available port 
	
	s.send(str(sock.getsockname()[1]) + "," + sock.getsockname()[0]) # send the client_address and port to the server
	
	sock.listen(5) # listen for a connection
	
	conn, addr = sock.accept() # accept the connection from server
	msg = raw_input() # message is from the keyboard
	conn.send(msg) # send the message to the server
	
	modified = conn.recv(BUFFER_SIZE) # receives modified message
	if not data: conn.close() # if no data is sent, close connection (just a failsafe, shouldn't happen)
	print "modified message:", modified # print the modified message
	
	sock.close() # close the data connection

while 1: #infinite loop to handle ongoing commands, breaks if "EXIT" command is entered
	print "Enter a command:"
	command = raw_input() # command takes input from the keyboard
	if command == "TOUPPERCASE" or command == "TOLOWERCASE": # valid commands
		send_and_receive(command) # call function with the command as the parameter
	elif command == "EXIT": # command to end connection/close program
 		break # breaks out of the loop
	else:
		print "Invalid command. Please try again." # any other command would be deemed invalid
s.close() # after breaking out of the loop (EXIT), end the control connection