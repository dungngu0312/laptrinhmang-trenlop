import socket

# Khởi tạo kết nối tới server
server_ip = '192.168.1.100'  # địa chỉ IP của server
server_port = 8888  # cổng kết nối
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Đọc nội dung file và gửi tới server
with open('file.txt', 'r') as f:
    data = f.read()
    client_socket.send(data.encode())

# Đóng kết nối
client_socket.close()
