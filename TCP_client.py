import socket

target_host = "0.0.0.0"
target_port = 9998

#Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the client
client.connect((target_host,target_port))

#send some data
client.send(b"ABCDEF")

#receive data
response = client.recv(4096)

print(response)
client.close()