import socket

# 1. 创建客户端套接字对象
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器
tcp_client_socket.connect(("", 8080))
# 3. 发送数据
tcp_client_socket.send("hello".encode("utf-8"))
# 4. 接收数据
data = tcp_client_socket.recv(1024)
print(data.decode("utf-8"))
# 5. 关闭套接字
tcp_client_socket.close()
