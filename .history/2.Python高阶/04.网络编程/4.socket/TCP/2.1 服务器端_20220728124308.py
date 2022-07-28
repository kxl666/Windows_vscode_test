import socket

# 1. 创建服务端套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定IP地址和端口号
tcp_server_socket.bind(("", 8080))