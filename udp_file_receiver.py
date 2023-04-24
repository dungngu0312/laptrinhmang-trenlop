import socket
import sys

# Lấy cổng chờ từ dòng lệnh
port = int(sys.argv[1])

# Khởi tạo socket và lắng nghe kết nối đến cổng chờ
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('localhost', port))
    print('udp_file_receiver is waiting for data...')

    # Nhận tên file và nội dung của file từ udp_file_sender
    file_name, addr = s.recvfrom(1024)
    file_content, addr = s.recvfrom(1024)

    # Ghi nội dung file vào file
    with open(file_name.decode(), 'wb') as file:
        file.write(file_content)

    print(f'{file_name.decode()} has been received and saved.')
