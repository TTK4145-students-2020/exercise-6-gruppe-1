import datetime
import socket
import threading
import time

local_ip = "10.22.64.64"
local_port = 9000
buf = 1024
skrr = True

class RepeatingTimer(object):

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
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    n = 3000
    for o in range(backup_count,n):
        time.sleep(1.5)
        # msg = str(o)
        # s2.sendto(msg.encode(), (local_ip,local_port+1))
        print(o)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((local_ip,local_port))

    backup_count = 0;


    while (skrr):
        timer = RepeatingTimer(2, backup, s, backup_count)
        timer.start()

        data, addr = s.recvfrom(buf)
        backup_count = int(data)
        timer.cancel()

main()
