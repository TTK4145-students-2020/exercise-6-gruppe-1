
import subprocess
import time
import datetime
import sys
import os
import threading
import socket

local_path  = '~/Desktop/sanntid/exercise-6-gruppe-1/phoenix.py' ## edit this

local_ip    = 'localhost'
local_port  = 42069
buffer      = 1024

is_master   = 0
num         = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((local_ip,local_port))

sock.settimeout(3)

try:
    print("listening to socket...")
    sock.recvfrom(buffer)
    print("...is slave.")

except (socket.timeout):
    subprocess.call('gnome-terminal -- python3 ' + local_path, shell=True)
    print("...no master found. i am master.")
    is_master = 1


while(1):
    if (is_master):
        num += 1
        msg = str(num)
        print(num)
        sock.sendto(msg.encode(), (local_ip, local_port))
        time.sleep(1)

    else:
        try:
            data, addr = sock.recvfrom(buffer)
            num = int(data)
        except socket.timeout:
            subprocess.call('gnome-terminal -- python3 ' + local_path, shell=True)
            is_master = 1
            print("i am the master now.")
