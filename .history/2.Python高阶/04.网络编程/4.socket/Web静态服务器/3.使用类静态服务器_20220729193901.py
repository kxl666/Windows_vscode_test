import socket
import threading


class WSGIServer(object):

    def __init__(self, server_address):
        self.

    def serve_forever(self):
        while True:
          clientSocket, clientAddr = serverSocket.accept()
          clientP = threading.Thread(target=handleClient, args=(clientSocket, ))
          # handleClient(clientSocket)
          clientP.start()
          # clientSocket.close()

    def handleClient(clientSocket):
        '用一个新的进程，为一个客户端进行服务'
        recvData = clientSocket.recv(1014).decode()
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
            f = open(
                r'C:\Users\kxl666\Desktop\Python\2.Python高阶\04.网络编程\4.socket\Web静态服务器'
                + request_path)
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
            clientSocket.send(response.encode())
            clientSocket.close()


def main():
    '作为程序的主控制入口'

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                            1)  # 设置端口可以立即重用
    serverSocket.bind(("", 7788))
    serverSocket.listen(10)



if __name__ == '__main__':
    main()
