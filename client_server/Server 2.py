import socket

hote = ''
port = 12816

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(1)
print("HELLO")

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b""
calcul=0
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    msg_recu=msg_recu.decode()
    msg_recu=msg_recu.split()
    if msg_recu[0]== ADD:
        calcul=str(float(msg_recu[1])+float(msg_recu[2]))
    if msg_recu[0]=="MIN":
        calcul=str(float(msg_recu[1])-float(msg_recu[2]))
    if msg_recu[0]=="DIV":
        calcul=str(float(msg_recu[1]) / float(msg_recu[2]))
    if msg_recu[0]=="TIM":
        calcul=str(float(msg_recu[1]) * float(msg_recu[2]))
    else:
        print("Try Again with real numbers")
    calcul= calcul.encode()
    connexion_avec_client.send(calcul)

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()