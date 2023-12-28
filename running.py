import os
import threading
import time
import sys
import ipaddress

ip_list = []

def run(start_ip, end_ip):
    #iterate over the ip address and add to list
    start_ip = ipaddress.IPv4Address(start_ip)
    end_ip = ipaddress.IPv4Address(end_ip)

    for ip_int in range(int(start_ip), int(end_ip) +1):
        ip_list.append(ipaddress.IPv4Address(ip_int))
    

    for ip in range(len(ip_list)):
        thread = threading.Thread(target=ping , args=(ip_list[ip],),)
        thread.start()
        time.sleep(0.5)
    


def ping(ip):
    print(os.popen(f"ping {ip}").read())

