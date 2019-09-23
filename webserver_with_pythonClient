from socket import *
import sys
import select

host="120.0.0.1"
port=6544

serverSocket=socket(AF_INET,SOCK_STREAM)


print("Socket Instance Made")

serverSocket.bind(('',port))
print("Socket bound")

# Prepare a server socket

serverSocket.listen(1)
# serverSocket.setblocking(0)
# serverSocket.settimeout(None)

while True:
    print ('Ready to serve')
    connectionSocket,addr=serverSocket.accept()
    print (addr[0]+"connected")
    try:
   
        message = connectionSocket.recv(1024)
        if not message:
            break
        print ('message:  ', message)
        #decode message in str from bytes
        message=message.decode('utf-8')
        filename = message.split()[1]
        
        print (filename)
        f = open(filename[1:])
        outputdata = f.read()
        #while outputdata:
          #  outputdata = f.read()
           # pr
        #print("outputdata:",outputdata)
       
        #f.close()
        first_header = "HTTP/1.1 200 OK"

        header_info = {
                    "Content-Length": len(outputdata),
                    "Keep-Alive": "timeout=%d,max=%d" %(10,100),
                    "Connection": "Keep-Alive",
                    "Content-Type": "text/html"
                }
        # concatenating th header info
        following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
        #print ("following_header:", following_header)
        str_to_send = "%s\r\n%s\r\n\r\n" %(first_header, following_header)
        connectionSocket.send(bytes(str_to_send, 'utf-8'))
        #Send one HTTP header line into socket
        #connectionSocket.send(b'HTTP/1.0 200 OK\r\n\r\n')
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i],'utf-8'))

        #connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send(b'404 Not Found')
        #Close client socketq
        connectionSocket.close()
serverSocket.close() 
