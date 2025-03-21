# PingSYN-ACK

- 1. Ping-Typ auswählen (SYN oder ACK)
Der Benutzer kann entscheiden, ob er einen SYN-Ping oder einen ACK-Ping senden möchte.
SYN Ping: Wird verwendet, um festzustellen, ob ein Port auf einem Zielserver offen ist, indem ein SYN-Paket gesendet wird (Teil des TCP-Handshake).
ACK Ping: Wird verwendet, um zu testen, ob ein Port für eingehende Verbindungen offen ist, indem ein ACK-Paket gesendet wird (mit der Erwartung eines RST-ACK bei einem geschlossenen Port).
- 2. Ziel-IP und Zielport angeben
Der Benutzer gibt die Ziel-IP-Adresse und den Zielport an. Das Skript sendet dann die Pings an diese Adresse und diesen Port.
- 3. Anzahl der Pings angeben
Der Benutzer kann festlegen, wie viele SYN- oder ACK-Pings an das Ziel gesendet werden sollen. Das Skript sendet diese Anzahl von Anfragen hintereinander.

pip install scapy colorama
