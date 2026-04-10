import socket
 
# ===== CONFIGURAZIONE =====

ADDRESS_FAMILY = socket.AF_INET

SOCKET_TYPE = socket.SOCK_STREAM

SERVER_HOST = '0.0.0.0'

SERVER_PORT = 5000
 
print("\n=== SERVER QUIZ TCP - Avvio ===")
 
# Domande

domande = [

    {"domanda": "Capitale d'Italia?", "risposta": "roma"},

    {"domanda": "2 + 2?", "risposta": "4"},

    {"domanda": "Colore del cielo?", "risposta": "blu"},

    {"domanda": "Capitale della Francia?", "risposta": "parigi"},

    {"domanda": "5 * 3?", "risposta": "15"},

    {"domanda": "Lingua parlata in Italia?", "risposta": "italiano"},

    {"domanda": "Opposto di caldo?", "risposta": "freddo"}

]
 
# FASE 1: socket()

server = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)

print("[1] Socket creato")
 
# FASE 2: bind()

server.bind((SERVER_HOST, SERVER_PORT))

print(f"[2] Bind su {SERVER_HOST}:{SERVER_PORT}")
 
# FASE 3: listen()

server.listen(1)

print("[3] Server in ascolto...")
 
# FASE 4: accept()

conn, addr = server.accept()

print(f"[4] Connesso a {addr}")
 
punteggio = 0
 
for q in domande:

    # invia domanda

    conn.send(q["domanda"].encode('utf-8'))

    print("[5] Domanda inviata")
 
    # riceve risposta

    data = conn.recv(1024)

    risposta = data.decode('utf-8').lower().strip()

    print("[6] Risposta ricevuta:", risposta)
 
    # controllo

    if risposta == q["risposta"]:

        feedback = "Corretto"

        punteggio += 1

    else:

        feedback = "Sbagliato. Risposta giusta: " + q["risposta"]
 
    # invia feedback

    conn.send(feedback.encode('utf-8'))

    print("[7] Feedback inviato")
 
# risultato finale

risultato = "Quiz finito! Punteggio: " + str(punteggio) + "/" + str(len(domande))

conn.send(risultato.encode('utf-8'))

print("[8] Risultato inviato")
 
# chiusura

conn.close()

server.close()

print("[9] Server chiuso\n")
 