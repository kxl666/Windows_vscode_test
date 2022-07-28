import socket

# 1. 创建服务端套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定IP地址和端口号
tcp_server_socket.bind(("", 8080))
# 3. 开启监听，监听客户端连接,  128代表允许最大连接数
tcp_server_socket.listen(128)
# 4. 等待客户端连接