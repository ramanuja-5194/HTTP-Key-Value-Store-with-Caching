import socket

cache_dict = {}
#connection with server
server_ip = "10.0.1.3"

server = socket.socket()
print server_ip

server_port = 12345

server.connect((server_ip,server_port))
server.send('Hello server'.encode())
print 'Server received: ' + server.recv(1024).decode()

#connection with client
dst_ip = "10.0.1.2"

cache = socket.socket()
print "Socket successfully created"

dport = 12346
cache.bind((dst_ip, dport))
print ("Socket binded to port: {}".format(dport))

cache.listen(5)
print "cache is listening"
client, addr = cache.accept()
print 'Got connection from', addr
recvmsg = client.recv(1024).decode()
print 'Cache received: ' + recvmsg
client.send('Hello client'.encode())

#---------------


while True:
    recvmsg = client.recv(1024).decode()
    if not recvmsg:
        break
    try:
        method, path, version = recvmsg.splitlines()[0].split()
        if method == 'PUT':
            server.send(recvmsg.encode())
            resp = server.recv(1024)
            client.send(resp)
        elif method == 'GET':
            if '?' in path:
                base, req = path.split('?')
                if 'request=' in req:
                    key = req.split('=')[1]
                    if key in cache_dict:
                        response = "HTTP/1.1 200 OK\r\nValue: {}\r\n".format(cache_dict[key])
                        client.send(response.encode())
                    else:
                        server.send(recvmsg.encode())
                        resp = server.recv(1024)
                        value = resp.decode().split("\r\n")[1].split("Value: ")[1]
                        cache_dict[key] = value
                        print(cache_dict)
                        client.send(resp)
            else:
                response = "HTTP/1.1 400 Bad Request\r\nInvalid Request Format\r\n"
                client.send(response.encode())
        else:
            response = "HTTP/1.1 405 Method Not Allowed\r\n\r\n"
            client.send(response.encode())
    except Exception as e:
        response = "HTTP/1.1 500 Internal Server Error\r\nError occurred: {}\r\n".format(str(e))
        client.send(response.encode())

server.close()
client.close()
"""while True:
	recvmsg = client.recv(1024).decode()
	if not recvmsg:
		break
    try:
        method, path, version = recvmsg.splitlines()[0].split()
        if method == 'PUT':
            server.send(recvmsg.encode())
    		resp = server.recv(1024)
    		client.send(resp)
        elif method == 'GET':
            if '?' in path:
        		base, req = path.split('?')
        		if 'request=' in req:
            		key = req.split('=')[1]
            		if key in cache_dict:
            			response =  "HTTP/1.1 200 OK\r\nValue: {}\r\n".format(cache_dict[key])
            			client.send(response.encode())
            		else:
            			server.send(recvmsg.encode())
            			resp = server.recv(1024)
            			value = resp.decode().split("\r\n")[1].split("Value: ")[1]
            			cache_dict[key] = value
            			client.send(resp)
            response = "HTTP/1.1 400 Bad Request\r\nInvalid Request Format\r\n"
            client.send(response.encode())

        else:
            response = "Wrong method."
    except Exception, e:
        response = "Error occurred: " + str(e)
    client.send(response.encode())"""

