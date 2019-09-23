from socket import *
import threading



# creating a client thread class for the connecting to socket server
class ClientThread(threading.Thread):
    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address
    def run(self):
        while True:
            try:
                message = connectionSocket.recv(1024)
                if not message:
                    break
                print ("message: \n", message)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read() 
                #print ("outputdata:", outputdata)
    

                first_header = "HTTP/1.1 200 OK"

                header_info = {
                    "Content-Length": len(outputdata),
                    "Keep-Alive": "timeout=%d,max=%d" %(10,100),
                    "Connection": "Keep-Alive",
                    "Content-Type": "text/html"
                }
                # concatenating th header info
                following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
                print ("following_header:", following_header)
                str_to_send = "%s\r\n%s\r\n\r\n" %(first_header, following_header)
                connectionSocket.send(bytes(str_to_send, 'utf-8'))

            
                for i in range(0, len(outputdata)):
                    connectionSocket.send(bytes(outputdata[i], 'utf-8'))
            except IOError:

                connectionSocket.send(b"404 Not Found\r\n\r\n")


# Creating the main thread for initiating socket here
if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM) 
   
    serverPort = 6789
    serverSocket.bind(('',serverPort))
    serverSocket.listen(5)
    threads=[]
   
    while True:
  
        print ('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print ("addr:", addr)

        client_thread = ClientThread(connectionSocket,addr)
        client_thread.setDaemon(True)
        client_thread.start()
        threads.append(client_thread)

    #main thread wait all threads finish then close the connection
    serverSocket.close()
