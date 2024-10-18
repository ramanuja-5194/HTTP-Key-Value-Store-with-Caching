import socket
import time

def put(cache, key, value):
    request = "PUT /assignment1/{}/{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(key, value, cache_ip)
    start = time.time()
    cache.send(request.encode())
    resp = cache.recv(1024)
    end = time.time()
    print "time taken: {}".format(end-start)
    print resp.decode()

def get(cache, key):
    request = "GET /assignment1?request={} HTTP/1.1\r\nHost: {}\r\n\r\n".format(key, cache_ip)
    start = time.time()
    cache.send(request.encode())
    resp = cache.recv(1024)
    end = time.time()
    print "time taken: {}".format(end-start)
    print resp.decode()

cache_ip = "10.0.1.2"
dst_ip = "10.0.1.2"

cache = socket.socket()
print dst_ip

port = 12346

cache.connect((dst_ip, port))
cache.send('Hello cache'.encode())
print 'Client received: ' + cache.recv(1024).decode()

while True:
    query_type = raw_input("Enter PUT/GET/QUIT: ").upper()
    
    if query_type == 'PUT':
        key = raw_input("Enter key: ")
        value = raw_input("Enter value: ")
        put(cache, key, value)
    elif query_type == 'GET':
        key = raw_input("Enter key: ")
        get(cache, key)
    elif query_type == 'QUIT':
        break
    else:
        print "Wrong type of query"

cache.close()
