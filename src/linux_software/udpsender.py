import socket
import sys
import time


if len(sys.argv) != 3:
    print("Usage: python3 udpsender.py <DEST_IP> <NUM_PACKETS>")
    sys.exit(1)

UDP_IP = sys.argv[1]
try:
    NUM_PACKETS = int(sys.argv[2])
except ValueError:
    print("Error: NUM_PACKETS must be an integer.")
    sys.exit(1)

UDP_PORT = 25344  #port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Sending {NUM_PACKETS} UDP packets to {UDP_IP}:{UDP_PORT}...")

for i in range(NUM_PACKETS):
    #example
    message = f"Packet {i:04d} - Hello from Zybo!"
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
    print(f"Sent: {message}")
    time.sleep(0.01)  #delay so Wireshark can catch them 
    
sock.close()
print("Done.")
