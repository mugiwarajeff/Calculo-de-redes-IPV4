"""
Projeto de programa para calculo de redes IPV4

IP: exemplo: 10.20.12.45/26
Rede: 10.20.12.0/26
Broadcast: 10.20.12.63/26
Máscara:255.255.255.192
Primeiro IP 10.20.12.1/26
Último IP:10.20.12.62/26
nº de IPs: 62


"""

from classes import IPV4

try:
    ip = IPV4(input("digite o seu ip:"))
    ip.calcular()
except Exception:
    print("você digitou um ip de formato invalido")


