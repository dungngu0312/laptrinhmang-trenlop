import socket

# Khởi tạo server
server_ip = '192.168.1.100'  # địa chỉ IP của server
server_port = 8888  # cổng kết nối
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen()

# Chấp nhận kết nối từ client
print('Waiting for connection...')
client_socket, client_address = server_socket.accept()
print(f'Connection from {client_address}')

# Nhận dữ liệu từ client
data = client_socket.recv(1024).decode()

# Đếm số lần xuất hiện của chuỗi '0123456789'
count = 0
temp = ''
for c in data:
    temp += c
    if '0123456789' in temp:
        count += 1
        temp = ''

# In số lần xuất hiện của chuỗi '0123456789' ra màn hình
print('Number of occurrences of "0123456789":', count)

# Đóng kết nối
client_socket.close()
server_socket.close()
