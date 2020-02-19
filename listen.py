import socket

local_ip = "10.22.64.64"
local_port = 9000
buf = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((local_ip,local_port))

while True:
    data, addr = s.recvfrom(buf)
    print("received: ", int(data), "-- from",addr)
