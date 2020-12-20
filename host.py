import socket
h = '127.0.0.1'
p = 1234
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((h,p))
s.listen()
def baglanti():
    while 1:
        c,addr = s.accept()
        print(f' Baglanti kuruldu {addr}')
        while 1:
            message = input("mesajınız")
            c.send(message.encode('ascii'))
            print("İletildi")
            data = c.recv(1024) 
            print("Client :",data)
baglanti()
