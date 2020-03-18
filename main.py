#using process pairing, we print numbers

import multiprocessing as mp
import socket
import time
import threading
import sys
import datetime

local_ip = "localhost"
local_port = 9000
buf = 1024

class RepeatingTimer(object):   # repeating timer for restarting it
    def __init__(self, interval, f, arg1, arg2):
        self.interval = interval
        self.f = f
        self.arg1 = arg1
        self.arg2 = arg2
        self.timer = None
    def callback(self):
        self.f(self.arg1, self.arg2)
        self.start()
    def cancel(self):
        self.timer.cancel()
    def start(self):
        self.timer = threading.Timer(self.interval, self.callback)
        self.timer.start()

def backup(s,backup_count):
    skrr = False
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    n = 3000
    for o in range(backup_count,n):
        time.sleep(1.5)
        msg = str(o)
        sock.sendto(msg.encode(), (local_ip,local_port))

        print(o)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((local_ip,local_port))
    backup_count = 0;
    while (skrr):
        timer = RepeatingTimer(2, backup, sock, backup_count)
        timer.start()

        data, addr = sock.recvfrom(buf)
        backup_count = int(data)
        timer.cancel()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((local_ip,local_port))
    s.settimeout(2)

    n = 3000
    for i in range(n):
        time.sleep(1.5)
        msg = str(i)
        #s.sendto(msg.encode(), (local_ip,local_port))
        print(i)
        data,addr = s.recvfrom(buf)

main()
