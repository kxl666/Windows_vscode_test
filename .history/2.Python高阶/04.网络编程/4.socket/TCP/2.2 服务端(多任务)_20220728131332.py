import socket

# 1. 创建服务端套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口可重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 2. 绑定IP地址和端口号
tcp_server_socket.bind(("", 8888))  # 可以不指定IP地址
# 3. 开启监听，监听客户端连接,  128代表允许最大连接数
tcp_server_socket.listen(128)
# 4. 等待客户端连接请求 accept阻塞等待 返回一个用以和客户端进行通信socket对象, 和客户端的地址

while True:
    tcp_client_socket, client_addr = tcp_server_socket.accept()
    print("连接的客户端地址：", client_addr)
    # 5. 接收数据
    data = tcp_client_socket.recv(1024)
    print(data.decode("utf-8"))
    # 6. 发送数据
    tcp_client_socket.send("i know !".encode("utf-8"))
    # 7. 关闭套接字
    tcp_client_socket.close()

tcp_server_socket.close()
