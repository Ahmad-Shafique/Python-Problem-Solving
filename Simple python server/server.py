
# reference : https://stackoverflow.com/questions/10091271/how-can-i-implement-a-simple-web-server-using-python-without-using-any-libraries

from socket import *
def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind(('localhost',9000))
    serversocket.listen(5)
    while(1):
        (clientsocket, address) = serversocket.accept()
        clientsocket.send("It works".encode())

        
createServer()
