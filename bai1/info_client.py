import socket

# Khởi tạo kết nối tới server
server_ip = '192.168.1.100'  # địa chỉ IP của info_server
server_port = 8888  # cổng kết nối
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Nhập tên máy tính và danh sách ổ đĩa
computer_name = input("Enter computer name: ")
drive_list = input("Enter drive list (separated by comma): ")

# Đóng gói dữ liệu và gửi tới server
data = computer_name + ';' + drive_list
client_socket.send(data.encode())

# Đóng kết nối
client_socket.close()
