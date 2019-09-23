from socket import *
import sys
import time
# Set up a TCP/IP socket
ip_address=sys.argv[1]
port=sys.argv[2]
path=sys.argv[3]
port=int(port)
s = socket(AF_INET,SOCK_STREAM)

#port=1221
# Connect as client
s.connect((ip_address,port))
print ("connected")
path='GET '+path+' HTTP/1.1\r\nHost: 127.0.0.1:6549\r\n'
s.send(bytes(path,'utf-8'))
#s.send(b'GET s')
print ("sent")
resp = s.recv(1024)
resp=resp.decode('utf-8')
print( resp)
time.sleep(2)
while True:
    if not resp:
        break
    resp = s.recv(1024)
        # decoding the received bytes message into utf-8
    resp=resp.decode('utf-8')
    print (resp)


# Close the connection when completed
s.close()
