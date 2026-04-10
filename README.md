# Socket-quiz
Componenti del gruppo: Boglioni Gabriele, Grossi Andrea
# 🎯 Quiz Client/Server TCP in Python
 
## 📌 Descrizione

Questo progetto implementa un'applicazione Client/Server in Python che permette di svolgere un quiz testuale tramite rete utilizzando il protocollo TCP.
 
Il sistema è composto da due programmi:

- Server: gestisce le domande, controlla le risposte e calcola il punteggio

- Client: gestisce l'interfaccia utente e la comunicazione con il server
 
---
 
## ⚙️ Funzionamento
 
1. Il server viene avviato e resta in ascolto su una porta.

2. Il client si connette all'indirizzo IP del server.

3. Il server invia una domanda alla volta.

4. Il client:

   - visualizza la domanda

   - inserisce la risposta da tastiera

   - invia la risposta al server

5. Il server:

   - verifica la risposta

   - invia un feedback ("Corretto" / "Sbagliato")

6. Al termine del quiz:

   - il server invia il punteggio finale

   - la connessione viene chiusa
 
---
 
## 🧠 Struttura del Quiz
 
Le domande sono memorizzate nel server usando una lista di dizionari:
 
```python

domande = [

    {"domanda": "Capitale d'Italia?", "risposta": "roma"},

    {"domanda": "2 + 2?", "risposta": "4"},

    {"domanda": "Colore del cielo?", "risposta": "blu"},

    {"domanda": "Capitale della Francia?", "risposta": "parigi"},

    {"domanda": "5 * 3?", "risposta": "15"},

    {"domanda": "Lingua parlata in Italia?", "risposta": "italiano"},

    {"domanda": "Opposto di caldo?", "risposta": "freddo"}

]
 
