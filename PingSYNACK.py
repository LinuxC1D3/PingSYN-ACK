import argparse
from scapy.all import *
from colorama import init, Fore
import time

# Initialisiere colorama
init(autoreset=True)

# ASCII Art - Willkommenstext
print(r"""
                                   Created by
  _       _________ _                            _______  __    ______   ______  
 ( \      \__   __/( (    /||\     /||\     /|  (  ____ \/  \  (  __  \ / ___  \ 
 | (         ) (   |  \  ( || )   ( |( \   / )  | (    \/\/) ) | (  \  )\/   \  \
 | |         | |   |   \ | || |   | | \ (_) /   | |        | | | |   ) |   ___) /
 | |         | |   | (\ \) || |   | |  ) _ (    | |        | | | |   | |  (___ ( 
 | |         | |   | | \   || |   | | / ( ) \   | |        | | | |   ) |      ) \
 | (____/\___) (___| )  \  || (___) |( /   \ )  | (____/\__) (_| (__/  )/\___/  /
 (_______/\_______/|/    )_)(_______)|/     \|  (_______/\____/(______/ \______/ 
""")

# Funktion zum Senden eines SYN-Pings
def send_syn_ping(target_ip, target_port, count):
    for _ in range(count):
        ip = IP(dst=target_ip)  # Ziel-IP
        syn = TCP(dport=target_port, flags="S")  # SYN-Flag setzen
        pkt = ip/syn
        response = sr1(pkt, timeout=1, verbose=False)

        if response:  # Wenn eine Antwort zurückkommt
            if response.haslayer(TCP) and response[TCP].flags == 0x12:  # SYN-ACK Antwort
                print(Fore.GREEN + f"SYN Ping an {target_ip}:{target_port} erfolgreich, Verbindung geöffnet.")
            else:
                print(Fore.RED + f"SYN Ping an {target_ip}:{target_port} geschlossen.")
        else:
            print(Fore.RED + f"SYN Ping an {target_ip}:{target_port} geschlossen (keine Antwort).")
        
        time.sleep(1)  # Pause von 1 Sekunde zwischen den Pings

# Funktion zum Senden eines ACK-Pings
def send_ack_ping(target_ip, target_port, count):
    for _ in range(count):
        ip = IP(dst=target_ip)  # Ziel-IP
        ack = TCP(dport=target_port, flags="A")  # ACK-Flag setzen
        pkt = ip/ack
        response = sr1(pkt, timeout=1, verbose=False)

        if response:  # Wenn eine Antwort zurückkommt
            if response.haslayer(TCP) and response[TCP].flags == 0x14:  # RST-ACK Antwort
                print(Fore.GREEN + f"ACK Ping an {target_ip}:{target_port} erfolgreich, Verbindung geöffnet.")
            else:
                print(Fore.RED + f"ACK Ping an {target_ip}:{target_port} geschlossen.")
        else:
            print(Fore.RED + f"ACK Ping an {target_ip}:{target_port} geschlossen (keine Antwort).")
        
        time.sleep(1)  # Pause von 1 Sekunde zwischen den Pings

# Hauptfunktion, die Argumente aus der Konsole liest
def main():
    # Argumente parsen
    parser = argparse.ArgumentParser(description="Sende SYN oder ACK Pings an ein Ziel.")
    parser.add_argument("ping_type", choices=["SYN", "ACK"], help="Der Typ des Pings (SYN oder ACK).")
    parser.add_argument("target_ip", help="Die Ziel-IP-Adresse.")
    parser.add_argument("target_port", type=int, help="Der Zielport.")
    parser.add_argument("count", type=int, help="Die Anzahl der zu sendenden Pings.")

    args = parser.parse_args()

    # Basierend auf dem gewählten Ping-Typ den entsprechenden Ping senden
    if args.ping_type == "SYN":
        send_syn_ping(args.target_ip, args.target_port, args.count)
    elif args.ping_type == "ACK":
        send_ack_ping(args.target_ip, args.target_port, args.count)

if __name__ == "__main__":
    main()
