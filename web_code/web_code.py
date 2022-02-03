import socket

from sqlalchemy import true

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.bilibili.com', 80))

s.send(b'GET / HTTP/1.1\r\nHost: www.bilibili.com\r\nConnection: close\r\n\r\n')

buffer = []

while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()

header, html = data.split(b'\r\n\r\n', 1)

print(header.decode('utf-8'))

with open('bilibili.html', 'wb') as f:
    f.write(html)