import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def write_to_file(filename, ip):
	f = open(filename, "w")
	f.write(ip)
	f.write("\n")
	f.close()


if __name__ == "__main__":
	file_for_writing_ip = "README.md"
	ip = get_ip_address('eth0')  # '192.168.0.2'
	write_to_file(file_for_writing_ip, ip)
