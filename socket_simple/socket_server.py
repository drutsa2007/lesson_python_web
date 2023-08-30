import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    text = data.decode()
    if not data:
        break
    send_text = 'Данные: ' + text + ' обработаны'
    conn.send(send_text.encode())

conn.close()
