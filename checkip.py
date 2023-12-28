import ipaddress
import sys


def check(ip):

    try:
        ip_obj = ipaddress.ip_address(ip)
        return True
    except ValueError:
        print(f"ERROR: {ip} is not a valid IP address!")
        sys.exit()
        
