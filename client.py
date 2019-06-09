from socket import AF_INET, socket, SOCK_STREAM, SHUT_WR
import subprocess
import time

host = input("ip addr: ")
port = input("port no: ")

buff = 4096
addr = (host, int(port))


print("connecting... " + str(addr))
c_sock = socket(AF_INET, SOCK_STREAM)
c_sock.connect(addr)
print("connected(check)")
c_sock.send(bytes("client", "utf8"))

def rec():
	while True:
		try:
			print('Waiting for msg....')
			msg = c_sock.recv(buff).decode('utf8')
			
			if msg:
				print('Display ~>' + msg)
				subprocess.run(['notify-send', msg])
			
			elif msg == '':
				raise RuntimeError('connection broken')
				c_sock.close()
				break
			
			if msg == 'quit':
				print('breaking out')
				c_sock.shutdown(SHUT_WR)
				
			"""if msg == 'file':
				f = open(testfile.mp4, 'wb')
				data = c_sock.recv(buff)
				print('data = ', (data))
				if not data:
					break
				f.write(data)
				f.close()
				subprocess.run(['xdg-open', name])
				c_sock.close()
				break """
			if msg == 'video':
				conn, addr = serv.accept()
				v = open(testvideo.mp4, 'wb')
				while True:
					data = conn.recv(BUFSIZE)
    					if not data:
    						break
    					v.write(data)
    					print 'writing file ....'
    				v.close()
    				conn.close()
		except OSError:
			print('error')
			c_sock.shutdown(SHUT_WR)
			c_sock.close()
			break

rec()
			
			
			
				
				
				
				
				
				
				