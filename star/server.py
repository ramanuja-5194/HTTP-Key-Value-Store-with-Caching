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

# this part has to be changed
dst_ip = "10.0.1.3"
s = socket.socket()
print "Socket successfully created"

dport = 12345
s.bind((dst_ip, dport))
print ("Socket binded to port: {}".format(dport))

s.listen(5)
print "Socket is listening"
#--------

def helper(recvmsg):
    try:
        method, path, version = recvmsg.splitlines()[0].split()
        if method == 'PUT':
            response = put(path)
        elif method == 'GET':
            response = get(path)
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