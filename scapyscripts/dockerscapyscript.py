from scapy.all import * 
A = '192.168.101.101' # spoofed source IP address 
B = 'DST_IP_OF_FLASK_SCAPY_DEPLOYMENT' # destination IP address 
C = 80 # source port 
D = 7000 # destination port \
spoofed_packet = IP(src=A, dst=B) / TCP( dport=D) / payload 
send(spoofed_packet) 