import socket
import sys

# Lấy tên file từ dòng lệnh
file_name = sys.argv[1]

# Lấy địa chỉ IP và cổng từ dòng lệnh
ip_address = sys.argv[2]
port = int(sys.argv[3])

# Mở file và đọc nội dung vào biến
with open(file_name, 'rb') as file:
    file_content = file.read()

# Khởi tạo socket và gửi dữ liệu đến udp_file_receiver
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(file_name.encode(), (ip_address, port))
    s.sendto(file_content, (ip_address, port))
