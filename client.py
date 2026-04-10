import socket
 
# ===== CONFIGURAZIONE =====
ADDRESS_FAMILY = socket.AF_INET
SOCKET_TYPE = socket.SOCK_STREAM
SERVER_HOST = '10.4.54.13'  # IP del server
SERVER_PORT = 5000
 
print("\n=== CLIENT QUIZ TCP - Avvio ===")
 
# FASE 1: socket()
client = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
print("[1] Socket creato")
 
# FASE 2: connect()
client.connect((SERVER_HOST, SERVER_PORT))
print(f"[2] Connesso a {SERVER_HOST}:{SERVER_PORT}")
 
while True:
    # riceve messaggio
    data = client.recv(1024)
 
    if not data:
        break
 
    messaggio = data.decode('utf-8')
    print("\n[3] Messaggio:", messaggio)
 
    # se è finale = esci
    if "Quiz finito" in messaggio:
        break
 
    # input utente
    risposta = input("Risposta: ").lower().strip()
 
    # invia risposta
    client.send(risposta.encode('utf-8'))
    print("[4] Risposta inviata")
 
    # riceve feedback
    feedback = client.recv(1024).decode('utf-8')
    print("[5] Feedback:", feedback)
 
# chiusura
client.close()
print("[6] Client chiuso\n")
 