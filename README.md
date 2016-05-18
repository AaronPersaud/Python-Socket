* There should be 2 other files here, server.py and client.py
* All commands must be entered in the client side.
1.) Open a terminal and run the server file with desired port number, like so: python server <n_port> (Ensure it's greater than 1024)
2.) Open another terminal and run the client file with the same port as before and the server's address, like so: python client <server_address> <n_port>
3.) Enter a valid command in the client terminal. Entering EXIT will disconnect with the server and end the control connection.
4.) Otherwise, enter TOUPPERCASE or TOLOWERCASE.
The command will then be sent to the server, and the server will send "OK" to the client.
5.) Now, enter a string. This will be modified by the command accordingly sent in step 4.
The server will now receive the string, modify it and send it back. After the client receives the string, the data connection will close on both ends.
6.) Enter a valid command. Typing EXIT will close the control connection. If you don't type EXIT, return to step 4.
7.) The server is still open. You can either open a new client to connect to the server or close the server. To close the server, press Ctrl-C. Otherwise, you can return to step 2 and run the client file.

Code was built on my personal computer.
Code was tested on:
	 ubuntu1204-002.student.cs.uwaterloo.ca	
	 ubuntu1204-004.student.cs.uwaterloo.ca	
	 ubuntu1204-006.student.cs.uwaterloo.ca	
