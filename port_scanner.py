import socket
IP = input("Enter the IP address you want to scan:")
soket = socket.socket()
for port in range(1, 25):

    try:
        soket.connect((IP ,port))
        answer = soket.recv(1024)
        print(answer.decode("utf-8"))
        soket.close()
        if "22" in str(port):
            print("System can be linux or network device.\n")

    except:
        print(port,". port closed")
        pass

