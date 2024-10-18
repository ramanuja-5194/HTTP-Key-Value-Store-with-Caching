import socket
dictionary = {}

def put(path):
    parts = path[1:].split('/')
    if len(parts) == 3:
        di, key, val = parts
        dictionary[key] = val
        print(dictionary)
        return "HTTP/1.1 200 OK\r\n"
    else:
        return "HTTP/1.1 400 Bad Request\r\nInvalid Request Format\r\n"

def get(path):
    if '?' in path:
        base, req = path.split('?')
        if 'request=' in req:
            key = req.split('=')[1]
            if key in dictionary:
                return "HTTP/1.1 200 OK\r\nValue: {}\r\n".format(dictionary[key])
            else:
                return "HTTP/1.1 404 Not Found\r\n"
    return "HTTP/1.1 400 Bad Request\r\nInvalid Request Format\r\n"

def delete(path):
    parts = path[1:].split('/')
    if len(parts) == 2:
        di, key = parts
        if key in dictionary:
            del dictionary[key]
            print(dictionary)
            return "HTTP/1.1 200 OK\r\n"
        else:
            return "HTTP/1.1 404 Not Found\r\n"
    return "HTTP/1.1 400 Bad Request\r\nInvalid Request Format\r\n"

dst_ip = "10.0.1.2"

s = socket.socket()
print "Socket successfully created"

dport = 12346
s.bind((dst_ip, dport))
print ("Socket binded to port: {}".format(dport))

s.listen(5)
print "Socket is listening"

def helper(recvmsg):
    try:
        method, path, version = recvmsg.splitlines()[0].split()
        if method == 'PUT':
            response = put(path)
        elif method == 'GET':
            response = get(path)
        elif method == 'DEL':
            response = delete(path)
        else:
            response = "Wrong method."
    except Exception, e:
        response = "Error occurred: " + str(e)
    return response

c, addr = s.accept()
print 'Got connection from', addr
recvmsg = c.recv(1024).decode()
print 'Server received: ' + recvmsg
c.send('Hello client'.encode())

while True:
    recvmsg = c.recv(1024).decode()
    if not recvmsg:
        break
    res = helper(recvmsg)
    c.send(res.encode())

c.close()

"""import socket

#WRITE CODE HERE:
#1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).
dictionary = {} # creating a dictionary
def put(path):
	parts = path[1:].split('/')
	if len(parts) == 3:
		di,key,val = parts
		dictionary[key] = val
		return "key value pair is stored."
	else:
		return "invalid format."

def get(path):
	if '?' in path:
		base, req = path.split('?')
		if 'request=' in req:
			key = req.split('=')[1]
			if key in dictionary:
				return f"val is  {dictionary[key]}"
			else:
				return "key is not present in the dictionary."
	else:
		return "invalid format."

def delete(path):
	parts = path[1:].split('/')
	if len(parts) == 2:
		di,key = parts
		if key in dictionary:
			del dictionary[key]
			return "key val pair is deleted."
		else:
			return "key is not present in the dictionary."
	else:
		return "invalid format."



dst_ip = str(input("Enter Server IP: "))

s = socket.socket()
print ("Socket successfully created")

dport = 12346
s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("socket is listening")

def helper(recvmsg):
	try:
		method, path, version = recvmsg.splitlines()[0].split()
		if method == 'PUT':
			response = put(path)
		elif method == 'GET':
			response = get(path)
		elif method = 'DEL':
			response = delete(path)
		else response = "wrong method."
	except Exception as e:
		response = "error has occured" + str(e)
	return response

c, addr = s.accept()
print ('Got connection from', addr)
recvmsg = c.recv(1024).decode()
print('Server received '+recvmsg)
c.send('Hello client'.encode())
while True:
  recvmsg = c.recv(1024).decode()
  res = helper(recvmsg)
  c.send(res.encode())
  #Write your code here
  #1. Uncomment c.send 
  #2. Parse the received HTTP request
  #3. Do the necessary operation depending upon whether it is GET, PUT or DELETE
  #4. Send response
  ##################

c.close()
  #break"""


