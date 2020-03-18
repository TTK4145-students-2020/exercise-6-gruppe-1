
import subprocess
import time
import datetime
import sys
import os
import threading
import socket

local_path = "python C:\\Users\jeg_j\Desktop\exercise-6-gruppe-1 phoenix.py"

local_ip    = 'localhost'
local_port  = 9000
buffer      = 1024

#local_path = os.path.dirname(os.path.realpath(__file__))


is_master   = 0
num         = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('localhost', 9000))

sock.settimeout(3)

try:
    print("listening to socket")
    sock.recvfrom(buffer)
    num = int(data)

except (socket.timeout):                 # no one is sending
    subprocess.call(['start',"python phoenix.py", 'python','phoenix.py'], shell=True)
    print("spawned subprocess")
    is_master = 1


while(1):
    if (is_master):
        num += 1
        msg = str(num)
        print("is master: ", num)
        sock.sendto(msg.encode(), (local_ip, local_port))
        time.sleep(1)

    else:
        print("is slave")
        try:
            data, addr = socket.recvfrom(buffer)
            num = int(data)
        except socket.timeout:
            is_master = 1
            subprocess.call(['start',"python phoenix.py", 'python',"phoenix.py"], shell=True)
