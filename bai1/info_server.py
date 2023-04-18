import socket

# Khởi tạo server
server_ip = '192.168.1.100'  # địa chỉ IP của info_server
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

# Tách dữ liệu và in ra màn hình
computer_name, drive_list = data.split(';')
print('Computer name:', computer_name)
print('Drive list:')
for drive in drive_list.split(','):
    print('- Drive', drive[0], 'has size', drive[1:])
    
# Đóng kết nối
client_socket.close()
server_socket.close()
