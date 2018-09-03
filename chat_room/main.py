from socket import *


def udp_send(udp_socket):
    # 发送消息 接收用户输入内容
    send_mes = input("请输入发送内容:")
    # 接收用户输入ip
    ip = input("请输入ip地址:")
    # 接收用户输入端口号
    port = int(input("请输入端口号"))
    # 发送消息 内容进行编码
    udp_socket.sendto(send_mes.encode("gbk"), (ip, port))


def udp_recvfrom(udp_socket):
    # 接收消息 最多4096个字节
    get_mes, get_ip = udp_socket.recvfrom(4096)
    print("收到来自%s的消息:%s" % (str(get_ip), get_mes.decode("gbk")))


def main():
    # 创建套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 设置固定端口
    udp_socket.bind(("", 8888))

    while True:
        print("*" * 50)
        print("----------无敌聊天器----------")
        print("1.发送消息")
        print("2.接收消息")
        print("0.退出系统")
        print("*" * 50)

        user = input("请输入要执行的操作:")

        if user == "1":

            udp_send(udp_socket)

        elif user == "2":

            udp_recvfrom(udp_socket)

        elif user == "0":
            break

        else:

            print("输入有误")
    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
