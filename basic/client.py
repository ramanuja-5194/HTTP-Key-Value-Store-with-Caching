import socket
import time

def put(s, key, value):
    request = "PUT /assignment1/{}/{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(key, value, server_ip)
    start = time.time()
    s.send(request.encode())
    resp = s.recv(1024)
    end = time.time()
    print "time taken: {}".format(end-start)
    print resp.decode()

def get(s, key):
    request = "GET /assignment1?request={} HTTP/1.1\r\nHost: {}\r\n\r\n".format(key, server_ip)
    start = time.time()
    s.send(request.encode())
    resp = s.recv(1024)
    end = time.time()
    print "time taken: {}".format(end-start)
    print resp.decode()

def delete(s, key):
    request = "DEL /assignment1/{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(key, server_ip)
    start = time.time()
    s.send(request.encode())
    resp = s.recv(1024)
    end = time.time()
    print "time taken: {}".format(end-start)
    print resp.decode()

server_ip = "10.0.1.2"

dst_ip = "10.0.1.2"
s = socket.socket()

print dst_ip

port = 12346

s.connect((dst_ip, port))
s.send('Hello server'.encode())
print 'Client received: ' + s.recv(1024).decode()

while True:
    query_type = raw_input("Enter PUT/GET/DEL/QUIT: ").upper()
    
    if query_type == 'PUT':
        key = raw_input("Enter key: ")
        value = raw_input("Enter value: ")
        put(s, key, value)
    elif query_type == 'GET':
        key = raw_input("Enter key: ")
        get(s, key)
    elif query_type == 'DEL':
        key = raw_input("Enter key: ")
        delete(s, key)
    elif query_type == 'QUIT':
        break
    else:
        print "Wrong type of query"

s.close()

"""import socket

def put(s, key, value):
    request = f"PUT /assignment1/{key}/{value} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
    s.send(request.encode())
    print("Client received: " + s.recv(1024).decode())

def get(s, key):
    request = f"GET /assignment1?request={key} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
    s.send(request.encode())
    print("Client received: " + s.recv(1024).decode())

def delete(s, key):
    request = f"DEL /assignment1/{key} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
    s.send(request.encode())
    print("Client received: " + s.recv(1024).decode())

serverIP = "10.0.1.2"

dst_ip = str(input("Enter dstIP: "))
s = socket.socket()

print(dst_ip)

port = 12346

s.connect((dst_ip, port))

#Write your code here:
#1. Add code to send HTTP GET / PUT / DELETE request. The request should also include KEY.
#2. Add the code to parse the response you get from the server.
s.send('Hello server'.encode())
print ('Client received '+s.recv(1024).decode())
while True:
	query_type = input("enter PUT/GET/DEL/QUIT").upper()
	if query_type == 'PUT':
		key = input("enter key: ")
		value = input("enter value: ")
		put(s,key,value)
	elif query_type == 'GET':
		key = input("enter key: ")
		get(s,key)
	elif query_type == 'DEL':
		key = input("enter key: ")
		delete(s,key)
	elif query_type = 'QUIT':
		break
	else:
		print("wrong type of query")
s.close()"""
