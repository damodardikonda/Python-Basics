import socket

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.connect("Localhost",'9999')
nme=input("enter teh name")
c.send(byte(nme),'utf=8')
print(c.resv(512).decode())
