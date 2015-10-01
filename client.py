import socket

host = "localhost"
port = 12800

##Construction du socket
connexion_au_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

##Connexion du client
connexion_au_serveur.connect((host, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = b""
while msg_a_envoyer !=b"fin":
    msg_a_envoyer = input("> ")
    msg_a_envoyer = msg_a_envoyer.encode()
    connexion_au_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode())

print("Fermeture de la connexion")
connexion_avec_serveur.close()


