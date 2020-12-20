import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',1234))
while 1:
    print (s.recv(1024))
    message = input("mesajınız")
    try:
        s.send(message.encode('ascii'))
        print("İletildi")
    except socket.error:
        print("HATA")

