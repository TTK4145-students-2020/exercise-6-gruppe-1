#using process pairing, we print numbers

import multiprocessing as mp
import socket
import time
import sys
import datetime

local_ip = "10.22.64.64"
local_port = 9000
buf = 1024

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    n = 3000
    for i in range(n):
        time.sleep(1.5)
        msg = str(i)
        s.sendto(msg.encode(), (local_ip,local_port))

        print(i)
