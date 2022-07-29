import socket

# import threading


class WSGIServer(object):

    addressFamily = socket.AF_INET
    socketType = socket.SOCK_STREAM
    requestQueueSize = 10

    def __init__(self, server_address):
        self.serverSocket = socket.socket(self.addressFamily, self.socketType)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                     1)  # 设置端口可以立即重用
        self.serverSocket.bind((server_address))
        self.serverSocket.listen(self.requestQueueSize)

    def serve_forever(self):
        while True:
            self.clientSocket, self.clientAddr = self.serverSocket.accept()
            print(self.clientSocket)
            # clientP = threading.Thread(target=self.handleClient,
            #                            args=(self.clientSocket, ))
            self.handleClient(self.clientSocket)
            # clientP.start()
            # clientSocket.close()

    def handleClient(self):
        '用一个新的进程，为一个客户端进行服务'
        recvData = self.clientSocket.recv(1014).decode()
        requestHeaderLines = recvData.splitlines()
        request_data = recvData.split(" ")

        for line in requestHeaderLines:
            print(line)

        request_path = request_data[1]
        if request_path == "/":
            request_path = "\index.html"
        elif request_path not in ["/favicon.ico"]:
            request_path = request_path + ".html"

        try:
            f = open(documentRoot + request_path)
        except FileNotFoundError:
            responseHeaderLines = "HTTP/1.1 404 not found\r\n" + "\r\n"
            responseBody = "====sorry ,file not found===="
        else:
            responseHeaderLines = "HTTP/1.1 200 OK\r\n"
            responseBody = f.read()
            f.close()
        finally:
            responseHeader = "Server:pwd\r\n"
            response = (responseHeaderLines + responseHeader +
                        "\r\n") + responseBody
            self.clientSocket.send(response.encode())
            self.clientSocket.close()


# 设定服务器的端口
serverAddr = (HOST, PORT) = '', 8888
# 设置服务器服务静态资源时的路径
documentRoot = r'C:\Users\kxl666\Desktop\Python\2.Python高阶\04.网络编程\4.socket\Web静态服务器'


def makeServer(serverAddr):
    server = WSGIServer(serverAddr)
    return server


def main():
    '作为程序的主控制入口'
    httpd = makeServer(serverAddr)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
