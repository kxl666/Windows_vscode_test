import socket

# 1. 创建套接字
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 准备接收方的地址
sendAddr = ('', 7788)

# 3. 从键盘获取数据
sendData = str(input("请输入要发送的数据:"))

# 4. 发送数据到指定的电脑上
udpSocket.sendto(sendData, sendAddr)

# 5. 等待接收对方发送的数据
recvData = udpSocket.recvfrom(1024)  # 1024表示本次接收的最大字节数

# 6. 显示对方发送的数据
print(recvData)

# 7. 关闭套接字
udpSocket.close()
