import math
import threading
import socket

IPS_PER_THREAD = 20
NUMBER_OF_THREADS = 5
MAX_SUB_IP = 255


currentIP = socket.gethostbyname(socket.gethostname())
ipTemplate = currentIP[:currentIP.rfind('.')+1]

socket.setdefaulttimeout(3)


def pingIPs(start, port, validIPs):
    for i in range(start, min(start+IPS_PER_THREAD, MAX_SUB_IP)):
        ip = ipTemplate + str(i)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            conn = s.connect_ex((ip, port))
            if(conn == 0):
                validIPs.append(ip)


def scanNetwork(port):
    threads = []
    validIPs = []
    for i in range(math.ceil(MAX_SUB_IP / IPS_PER_THREAD)):
        thread = threading.Thread(
            target=pingIPs, args=(i * IPS_PER_THREAD, port, validIPs))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return validIPs ### dead ?