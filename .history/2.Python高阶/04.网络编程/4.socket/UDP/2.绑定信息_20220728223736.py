import socket

# 1. 创建套接字
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bindAddr = ('', 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udpSocket.bind(bindAddr)
