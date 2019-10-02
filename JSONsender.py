# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, random, json

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)


#while 1:
#    print ("How any integers do you want to print?")
#    N = int(sys.stdin.readline().strip())
#    
for i in range(0, 10):
    x = {"name":"John", "age": str(30+i), "city":"New york"}
    
    print(x)
    if not len(x):
        print("AHHH were breakiNG uP!.")
        break
        #    s.sendall(data.encode('utf-8'))
    x = json.dumps(x)
    s.sendto(x.encode('utf-8'), server_address)
    

s.shutdown(1)
