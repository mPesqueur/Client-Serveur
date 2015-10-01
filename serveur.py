import socket

host = ''
port = 12800

##Construction du socket
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

##Connexion du socket
connexion.bind((host, port))

##Ecoute du port
connexion.listen(5)

print("Server is listenning on port {}".format(port))

##Accepter la connexion du client
connexion_au_client, infos_connexion = connexion.accept()

msg_recu = b""
while msg_recu !=b"fin":
    print(msg_recu.decode())
    connexion_au_client.send(b"5/5")

print("Fermeture de la connexion")
connexion_au_client.close()
connexion.close()
